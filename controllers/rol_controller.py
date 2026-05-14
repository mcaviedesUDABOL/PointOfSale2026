from controllers.audit_controller import AuditController
from models.rol_model import Rol
from data.dao.base_dao import BaseDAO
from data.dao.rol_dao import RolDAO
from data.connection.database_manager import DatabaseManager
from interfaces.auditable import Auditable
from controllers.audit_controller import AuditController
from utils.session import Session 

class RolController:


    def __init__(self):        
        #sesion
        self.__session = Session()    
        self.__data = {}
        self.__db_manager = DatabaseManager()
        self.__dao = RolDAO(self.__db_manager)
        self.__data = {obj.id: obj for obj in self.__dao.find_all_ordered()}
        self.__audit_controller = AuditController()
        
    
         # CREATE
    def create(self, new_obj)->bool:
        self.__audit_controller.register_creation(new_obj, id_user= self.__session.get_user_id())  # Simulamos un ID de usuario        
        self.__dao.insert(new_obj)
        self.__load_dict()
        print(f"Se agrego un nuevo registro")
        return True

    def __load_dict(self):
        self.__data = {obj.id: obj for obj in self.__dao.find_all_ordered()}

    # READ
    def find(self, id:int):
        return self.__data.get(id, "Registro no encontrado.")

    def read(self, only_active=False):
        return self.__data.values()
    
    # UPDATE
    def update(self, update_obj)->bool:
        self.__audit_controller.register_update(update_obj, id_user=self.__session.get_user_id())  # Simulamos un ID de usuario 
        result =self.__dao.update(update_obj.id, update_obj)
        if result == True:
            self.__load_dict()
        print(f"Registro Actualizado")
        return result

    # DELETE (Borrado Lógico)
    def is_deleted(self, id:int)->bool:
        obj = self.__data.get(id)
        self.__audit_controller.mark_as_deleted(obj, id_user=self.__session.get_user_id())  # type: ignore # Simulamos un ID de usuario
        result = self.__dao.update(obj.id, obj) # type: ignore
        if result:
            self.__load_dict()
        print(f"Registro borrado logicamente")
        return result

    # DELETE (Borrado Lógico)
    def delete(self, id:int)->bool:
        result = False
        if id in self.__data:
            result = self.__dao.delete(id)            
            print(f"registro borrado permanentemente")
        else:
            print("Error: ID inexistente.")
        return result