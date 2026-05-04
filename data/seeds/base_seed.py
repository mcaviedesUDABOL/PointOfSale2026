from abc import ABC, abstractmethod
from venv import logger

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from data.connection.database_manager import DatabaseManager

class BaseSeed(ABC):
    """Clase base para seeds"""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager
    
    @abstractmethod
    def up(self):
        """Crea las tablas y estructura"""
        pass
    
    @abstractmethod
    def down(self):
        """Elimina las tablas"""
        pass
    
    @abstractmethod
    def seed(self):
        """Puebla la base de datos con datos iniciales"""
        pass
    
    def run(self):
        """Ejecuta el seed completo"""
        try:
            logger.info(f"Running seed for {self.__class__.__name__}")
            self.up()
            self.seed()
            logger.info(f"Seed completed successfully for {self.__class__.__name__}")
        except Exception as e:
            logger.error(f"Error running seed: {e}")
            self.down()
            raise
    
    def execute_sql(self, sql: str, params: tuple = ()):
        """Ejecuta SQL directamente"""
        return self.db_manager.execute_update(sql, params)
    
    def execute_query(self, sql: str, params: tuple = ()):
        """Ejecuta una consulta SQL"""
        return self.db_manager.execute_query(sql, params)

