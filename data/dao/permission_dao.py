from typing import List, Optional
from data.connection.database_manager import DatabaseManager
from data.dao.base_dao import BaseDAO
from models.permission_model import Permission


class PermissionDAO(BaseDAO[Permission]):


    def __init__(self, db_manager: DatabaseManager):
        super().__init__(db_manager)

    
    
    def get_table_name(self) -> str:
        return "permissions"
    
    
    def row_to_model(self, row: dict) -> Permission:
        """Convierte una fila de la base de datos a Permission"""
        return Permission(
            id=int(row['id']) if 'id' in row and row['id'] is not None else -1,
            permission_name=row['permission_name'] if 'permission_name' in row else "",
            activate=row['activate'] if 'activate' in row else True
        )
    
    
    def model_to_dict(self, model: Permission) -> dict:
        """Convierte PermissionModel a diccionario"""
        data = {}
        if model.id != -1:
            data['id'] = model.id
        if model.permission_name is not None:
            data['permission_name'] = model.permission_name
        if model.activate is not None:
            data['activate'] = model.activate            
        return data
    
    
    # Métodos específicos para permission
    def find_by_name(self, name: str) -> Optional[Permission]:
        """Busca permiso por nombre exacto"""
        query = "SELECT * FROM permissions WHERE permission_name = ?"
        results = self.db_manager.execute_query(query, (name,))
        return self.row_to_model(results[0]) if results else None
    

    def search_by_name(self, search_term: str) -> List[Permission]:
        """Busca permisos por nombre parcial"""
        query = "SELECT * FROM permissions WHERE permission_name LIKE ? ORDER BY permission_name"
        results = self.db_manager.execute_query(query, (f"%{search_term}%",))
        return [self.row_to_model(row) for row in results]
    

    def find_all_ordered(self, order_by: str = "permission_name", ascending: bool = True) -> List[Permission]:
        """Obtiene todos los permisos ordenados"""
        direction = "ASC" if ascending else "DESC"
        query = f"SELECT * FROM permissions where activate = 1 ORDER BY {order_by} {direction}"
        results = self.db_manager.execute_query(query)
        return [self.row_to_model(row) for row in results]
    
