from models.user_model import User
from data.dao.user_dao import UserDAO
from data.connection.database_manager import DatabaseManager
from controllers.audit_controller import AuditController
from typing import Optional
from utils.session import Session  
from typing import cast

class UserController:
    
    def __init__(self):        
        self.__session = Session()    
        self.__id_user = cast(int,self.__session.get_user_id if self.__session.get_user_id is not None else -1)
        self.__data = {}
        self.__db_manager = DatabaseManager()
        self.__dao = UserDAO(self.__db_manager)
        self.__data = {obj.id: obj for obj in self.__dao.find_all_ordered()}
        self.__audit_controller = AuditController()
        self.__user = None

        # CREATE
    def create(self, new_obj)->bool:
        self.__audit_controller.register_creation(new_obj, id_user= self.__id_user )  # Simulamos un ID de usuario        
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
        self.__audit_controller.register_update(update_obj, id_user= self.__id_user)  # Simulamos un ID de usuario 
        result =self.__dao.update(update_obj.id, update_obj)
        if result == True:
            self.__load_dict()
        print(f"Registro Actualizado")
        return result

    # DELETE (Borrado Lógico)
    def is_deleted(self, id:int)->bool:
        obj = self.__data.get(id)
        self.__audit_controller.mark_as_deleted(obj, id_user= self.__id_user)  # type: ignore # Simulamos un ID de usuario
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


    def authenticate(self, username, password) ->bool:        
        for user in self.__data.values():
            if user.user_name == username and user.password == password:
                print(f"Autenticación exitosa para el usuario '{username}'.")
                self.__user = user
                return True
            else:
                print(f"Error: Credenciales inválidas. '{user.user_name}' '{user.password}' ")
                self.__user = None
        return False
    
    def user_authenticate(self) -> Optional[User]:
        return self.__user


    def change_password(self, id_user, new_password)->bool:
        if id_user in self.__data:
            user = self.__data[id_user]
            user.password = new_password
            self.update(user)
            print(f"Contraseña del usuario {id_user} actualizada.")
            return True
        else:
            print("Error: ID inexistente.")
            return False

    
    def assign_role(self, id_user, new_role)->bool:
        if id_user in self.__data:
            user = self.__data[id_user]
            user.role = new_role
            self.update(user)
            print(f"Rol del usuario {id_user} actualizado a '{new_role}'.")
            return True
        else:
            print("Error: ID inexistente.")
            return False
    
    