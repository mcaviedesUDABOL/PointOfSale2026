# dao/base_dao.py
from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Generic
from data.connection.database_manager import DatabaseManager

T = TypeVar('T')


class BaseDAO(ABC, Generic[T]):
    """Base DAO con operaciones CRUD"""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager
    
    @abstractmethod
    def get_table_name(self) -> str:
        """Retorna el nombre de la tabla"""
        pass
    
    @abstractmethod
    def row_to_dto(self, row: dict) -> T:
        """Convierte una fila de la base de datos a DTO"""
        pass
    
    @abstractmethod
    def model_to_dict(self, model: T) -> dict:
        """Convierte un model a diccionario para inserción/actualización"""
        pass
    
    def find_by_id(self, id: int) -> Optional[T]:
        """Busca por ID"""
        query = f"SELECT * FROM {self.get_table_name()} WHERE id = ?"
        results = self.db_manager.execute_query(query, (id,))
        return self.row_to_dto(results[0]) if results else None
    
    def find_all(self, limit: Optional[int] = None, offset: int = 0) -> List[T]:
        """Obtiene todos los registros"""
        query = f"SELECT * FROM {self.get_table_name()}"
        params = []
        
        if limit:
            query += " LIMIT ? OFFSET ?"
            params.extend([limit, offset])
        
        results = self.db_manager.execute_query(query, tuple(params))
        return [self.row_to_dto(row) for row in results]
    
    def insert(self, model: T) -> int:
        """Inserta un nuevo registro"""
        data = self.model_to_dict(model)
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?' for _ in data])
        query = f"INSERT INTO {self.get_table_name()} ({columns}) VALUES ({placeholders})"
        return self.db_manager.execute_insert(query, tuple(data.values()))
    
    def update(self, id: int, model: T) -> bool:
        """Actualiza un registro existente"""
        data = self.model_to_dict(model)
        # Remover id si existe
        data.pop('id', None)
        
        set_clause = ', '.join([f"{key} = ?" for key in data.keys()])
        query = f"UPDATE {self.get_table_name()} SET {set_clause}, updated_at = CURRENT_TIMESTAMP WHERE id = ?"
        params = list(data.values()) + [id]
        
        rows_affected = self.db_manager.execute_update(query, tuple(params))
        return rows_affected > 0
    
    def delete(self, id: int) -> bool:
        """Elimina un registro"""
        query = f"DELETE FROM {self.get_table_name()} WHERE id = ?"
        rows_affected = self.db_manager.execute_update(query, (id,))
        return rows_affected > 0
    
    def count(self) -> int:
        """Cuenta el número de registros"""
        query = f"SELECT COUNT(*) as count FROM {self.get_table_name()}"
        results = self.db_manager.execute_query(query)
        return results[0]['count'] if results else 0
    
    def exists(self, id: int) -> bool:
        """Verifica si existe un registro"""
        return self.find_by_id(id) is not None

