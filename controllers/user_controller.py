from models.user_model import User
from data.dao.base_dao import BaseDAO
from data.dao.user_dao import UserDAO
from data.connection.database_manager import DatabaseManager

class UserController:
    
    def __init__(self):        
        self.__users = {}
        self.__db_manager = DatabaseManager()
        self.__user_dao = UserDAO(self.__db_manager)
        self.__users = {user.id: user for user in self.__user_dao.find_all_ordered()}


    # CREATE
    def create(self, user) ->bool:
        self.__user_dao.insert(user)
        self.__users = {user.id: user for user in self.__user_dao.find_all_ordered()}        
        return True


    # READ
    def find(self, id_user):
        return self.__users.get(id_user, False)


    def read(self, only_active=False):
        return self.__users.values()


    # UPDATE
    def update(self, user) ->bool:
        self.__user_dao.update(user.id, user)
        self.__users = {user.id: user for user in self.__user_dao.find_all_ordered()}
        print(f"Usuario {user.id} actualizado.")
        return True


    # DELETE (Borrado Lógico)
    def delete(self, id_user) ->bool:
        if id_user in self.__users:
            self.__users[id_user].activate = False
            print(f"Usuario {id_user} marcado como inactivo.")
            return True
        else:
            print("Error: ID inexistente.")
            return False
    

    def authenticate(self, username, password) ->User:
        for user in self.__users.values():
            if user.username == username and user.password == password:
                print(f"Autenticación exitosa para el usuario '{username}'.")
                return user
        print("Error: Credenciales inválidas.")
        return User()


    def change_password(self, id_user, new_password)->bool:
        if id_user in self.__users:
            user = self.__users[id_user]
            user.password = new_password
            self.update(user)
            print(f"Contraseña del usuario {id_user} actualizada.")
            return True
        else:
            print("Error: ID inexistente.")
            return False

    
    def assign_role(self, id_user, new_role)->bool:
        if id_user in self.__users:
            user = self.__users[id_user]
            user.role = new_role
            self.update(user)
            print(f"Rol del usuario {id_user} actualizado a '{new_role}'.")
            return True
        else:
            print("Error: ID inexistente.")
            return False
    
    