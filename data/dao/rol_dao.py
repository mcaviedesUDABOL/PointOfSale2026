from typing import List, Optional
from data.connection.database_manager import DatabaseManager
from data.dao.base_dao import BaseDAO
from models.rol_model import Rol


class RolDAO(BaseDAO[Rol]):
    
    def __init__(self, db_manager: DatabaseManager):
        super().__init__(db_manager)
    
    def get_table_name(self) -> str:
        return "roles"
    
    def row_to_model(self, row: dict) -> Rol:
        """Convierte una fila de la base de datos a Rol"""
        return Rol(
            id=int(row['id']) if 'id' in row and row['id'] is not None else -1,
            name=row['name'] if 'name' in row else "",
            activate=row['activate'] if 'activate' in row else True
        )
    

    def model_to_dict(self, model: Rol) -> dict:
        """Convierte RolModel a diccionario"""
        data = {}
        if model.id != -1:
            data['id'] = model.id
        if model.name is not None:
            data['name'] = model.name
        if model.activate is not None:
            data['activate'] = model.activate            
        return data
    

    # Métodos específicos para Rol
    def find_by_name(self, name: str) -> Optional[Rol]:
        """Busca rol por nombre exacto"""
        query = "SELECT * FROM roles WHERE name = ?"
        results = self.db_manager.execute_query(query, (name,))
        return self.row_to_model(results[0]) if results else None
    

    def search_by_name(self, search_term: str) -> List[Rol]:
        """Busca roles por nombre parcial"""
        query = "SELECT * FROM roles WHERE name LIKE ? ORDER BY name"
        results = self.db_manager.execute_query(query, (f"%{search_term}%",))
        return [self.row_to_model(row) for row in results]
    

    def find_all_ordered(self, order_by: str = "name", ascending: bool = True) -> List[Rol]:
        """Obtiene todos los roles ordenados"""
        direction = "ASC" if ascending else "DESC"
        query = f"SELECT * FROM roles where activate = 1 ORDER BY {order_by} {direction}"
        results = self.db_manager.execute_query(query)
        return [self.row_to_model(row) for row in results]
    

    
