from models.rol_model import Rol
from data.dao.base_dao import BaseDAO
from data.dao.rol_dao import RolDAO
from data.connection.database_manager import DatabaseManager

class RolController:


    def __init__(self):
        self.__roles = {}
        self.__db_manager = DatabaseManager()
        self.__rol_dao = RolDAO(self.__db_manager)
        self.__roles = {rol.id: rol for rol in self.__rol_dao.find_all_ordered()}
        

    def create_rol(self, name: str) -> dict:
        """Crea un nuevo rol"""
        rol = self.__rol_dao.insert(name)
        return self.__rol_dao.model_to_dict(rol)
    

    def get_all_roles(self) -> list:
        """Obtiene todos los roles"""
        roles = self.__rol_dao.find_all()
        return [self.__rol_dao.model_to_dict(rol) for rol in roles]
    

    def get_rol_by_id(self, id: int) -> dict:
        """Obtiene un rol por su ID"""
        rol = self.__rol_dao.find_by_id(id)
        return self.__rol_dao.model_to_dict(rol) if rol else {}
    

    def update_rol(self, id: int, name: str) -> dict:
        """Actualiza un rol existente"""
        updated_rol = self.__rol_dao.update(id, name)
        return self.__rol_dao.model_to_dict(updated_rol) if updated_rol else {}
    

    def delete_rol(self, id: int) -> bool:
        """Elimina un rol por su ID"""
        return self.__rol_dao.delete(id)