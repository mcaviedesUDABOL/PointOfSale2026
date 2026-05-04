from typing import List, Optional
from data.connection.database_manager import DatabaseManager
from data.dao.base_dao import BaseDAO
from models.user_model import User 

class UserDAO(BaseDAO[User]):
    
    def __init__(self, db_manager: DatabaseManager):
        super().__init__(db_manager)
    
    def get_table_name(self) -> str:
        return "users"
    def row_to_model(self, row: dict) -> User:
        """Convierte una fila de la base de datos a User"""
        return User(
            id=int(row['id']) if 'id' in row and row['id'] is not None else -1,
            name=row['name'] if 'name' in row else "",
            username=row['username'] if 'username' in row else "",
            password=row['password'] if 'password' in row else "",
            activate=row['activate'] if 'activate' in row else True
        )
    def model_to_dict(self, model: User) -> dict:
        """Convierte UserModel a diccionario"""
        data = {}
        if model.id != -1:
            data['id'] = model.id
        if model.name is not None:
            data['name'] = model.name
        if model.username is not None:
            data['username'] = model.username
        if model.password is not None:
            data['password'] = model.password
        if model.activate is not None:
            data['activate'] = model.activate            
        return data
    
    
    # Métodos específicos para User
    def find_by_username(self, username: str) -> Optional[User]:
        """Busca usuario por nombre de usuario exacto"""
        query = "SELECT * FROM users WHERE username = ?"
        results = self.db_manager.execute_query(query, (username,))
        return self.row_to_model(results[0]) if results else None
    
    
    def search_by_username(self, search_term: str) -> List[User]:
        """Busca usuarios por nombre de usuario parcial"""
        query = "SELECT * FROM users WHERE username LIKE ? ORDER BY username"
        results = self.db_manager.execute_query(query, (f"%{search_term}%",))
        return [self.row_to_model(row) for row in results]
    
    
    def find_all_ordered(self, order_by: str = "username", ascending: bool = True) -> List[User]:
        """Obtiene todos los usuarios ordenados"""
        direction = "ASC" if ascending else "DESC"
        query = f"SELECT * FROM users where activate = 1 ORDER BY {order_by} {direction}"
        results = self.db_manager.execute_query(query)
        return [self.row_to_model(row) for row in results]

    
    
    