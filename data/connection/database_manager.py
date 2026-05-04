import sqlite3
import os
from typing import Optional, List, Dict, Any
from contextlib import contextmanager
from pathlib import Path
import logging
from data.seeds.base_seed import BaseSeed
from data.seeds.category_seed import CategorySeed

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DatabaseManager:
    """Manejador de conexión a base de datos SQLite"""    
    _instance: Optional['DatabaseManager'] = None
    _connection: Optional[sqlite3.Connection] = None
    
    def __new__(cls, db_path: str = "data/database/point_of_sale_database.db"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self, db_path: str = "data/database/point_of_sale_database.db"):
        if self._initialized:
            return
        
        self.db_path = db_path
        self._initialized = True
        
        # Verificar si la base de datos existe
        self._db_exists = os.path.exists(db_path)
        
        # Conectar y verificar estructura
        self._connect()
        self._verify_database()
    
    def _connect(self):
        """Establece la conexión a la base de datos"""
        try:
            self._connection = sqlite3.connect(
                self.db_path,
                check_same_thread=False,
                detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
            )
            self._connection.row_factory = sqlite3.Row
            logger.info(f"Connected to database: {self.db_path}")
        except Exception as e:
            logger.error(f"Error connecting to database: {e}")
            raise
    
    def _verify_database(self):
        """Verifica si la base de datos tiene las tablas necesarias"""
        required_tables = ['categories']
        
        with self.get_cursor() as cursor:
            # Obtener tablas existentes
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            existing_tables = [row['name'] for row in cursor.fetchall()]
            
            # Verificar tablas faltantes
            missing_tables = [table for table in required_tables if table not in existing_tables]
            
            if missing_tables:
                logger.warning(f"Missing tables: {missing_tables}")
                self._initialize_database()
    
    def _initialize_database(self):
        """Inicializa la base de datos llamando al Seed si es necesario"""
        if not self._db_exists or self._needs_seeding():
            logger.info("Database needs seeding. Calling seed...")
            self._call_seed()
        else:
            logger.info("Database structure is valid")
    
    def _needs_seeding(self) -> bool:
        """Verifica si la base de datos necesita ser sembrada"""
        with self.get_cursor() as cursor:
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = cursor.fetchall()
            return len(tables) == 0
    
    def _call_seed(self):
        """Llama a la clase semilla para poblar la base de datos"""
        try:           
            seed = CategorySeed(self)
            seed.run()
            logger.info("Database seeded successfully")
        except ImportError as e:
            logger.error(f"Could not import seed class: {e}")
            # Crear estructura básica si no hay semilla
            self._create_basic_structure()
    
    def _create_basic_structure(self):
        """Crea la estructura básica de la base de datos"""
        with self.get_cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS categories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    active_1 BOOLEAN NOT NULL DEFAULT 1,            
                    description TEXT                    
                )
            """)
            logger.info("Basic database structure created")
    
    @contextmanager
    def get_cursor(self):
        """Context manager para manejar cursores"""
        if not self._connection:
            self._connect()
        
        cursor = self._connection.cursor() # type: ignore
        try:
            yield cursor
            self._connection.commit() # type: ignore
        except Exception as e:
            self._connection.rollback() # type: ignore
            logger.error(f"Database error: {e}")
            raise
        finally:
            cursor.close()
    
    def execute_query(self, query: str, params: tuple = ()) -> List[Dict[str, Any]]:
        """Ejecuta una consulta y retorna resultados"""
        with self.get_cursor() as cursor:
            cursor.execute(query, params)
            return [dict(row) for row in cursor.fetchall()]
    
    def execute_update(self, query: str, params: tuple = ()) -> int:
        """Ejecuta una actualización y retorna número de filas afectadas"""
        with self.get_cursor() as cursor:
            cursor.execute(query, params)
            return cursor.rowcount
    
    def execute_insert(self, query: str, params: tuple = ()) -> int:
        """Ejecuta un insert y retorna el ID generado"""
        with self.get_cursor() as cursor:
            cursor.execute(query, params)
            return cursor.lastrowid # type: ignore
    
    def close(self):
        """Cierra la conexión a la base de datos"""
        if self._connection:
            self._connection.close()
            self._connection = None
            logger.info("Database connection closed")
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
