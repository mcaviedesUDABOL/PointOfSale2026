
class Session:


    def __init__(self):
        self.__user_id = -1
        self.__user_name : str = "empty"
        self.__role_id = -1 
        self.__token: str = "empty"


    def set_user(self, user_id: int, name_user: str, role_id: int):
        self.__user_id = user_id
        self.__user_name = name_user
        self.__role_id = role_id
        self.__token = f"token_{user_id}_{name_user}_{role_id}"


    def is_logged_in(self) -> bool:
        return self.__user_id != -1
    
    
    def get_user_info(self) -> dict:
        if self.is_logged_in():
            return {
                "user_id": self.__user_id,
                "user_name": self.__user_name,
                "role_id": self.__role_id               
            }
        else:
            return {}

    def get_user_id(self) ->int:
        return  self.__user_id
    
    def get_user_name(self) ->str:
        return  self.__user_name

    def get_rol_id(self) -> int:
        return self.__role_id
    

    def logout(self) -> None:
        self.__init__()  # Reiniciar la sesión a su estado inicial
    

    def __str__(self):
        return f"Session(user_id={self.__user_id}, user_name='{self.__user_name}', role_id={self.__role_id}, token='{self.__token}')"
    

    

   