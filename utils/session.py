
class Session:
    def __init__(self):
        self.user_id = -1
        self.user_name = str = "empty"
        self.role_id = -1 
        self.token: str = "empty"


    def set_user(self, user_id: int, name_user: str, role_id: int):
        self.user_id = user_id
        self.user_name = name_user
        self.role_id = role_id
        self.token = f"token_{user_id}_{name_user}_{role_id}"


    def is_logged_in(self) -> bool:
        return self.user_id != -1
    
    
    def get_user_info(self) -> dict:
        if self.is_logged_in():
            return {
                "user_id": self.user_id,
                "user_name": self.user_name,
                "role_id": self.role_id               
            }
        else:
            return {}
    

    def logout(self) -> None:
        self.__init__()  # Reiniciar la sesión a su estado inicial
    

    def __str__(self):
        return f"Session(user_id={self.user_id}, user_name='{self.user_name}', role_id={self.role_id}, token='{self.token}')"
    

    

   