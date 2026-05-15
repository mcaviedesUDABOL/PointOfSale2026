from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Any, List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from models.rol_model import Rol


@dataclass
class User:
    __id: Optional[int] = field(default=None)
    __name: str = field(default="")
    __user_name: str = field(default="")
    __password: str = field(default="")
    __activate: bool = field(default=True)
    __rol: Optional['Rol'] = field(default=None)


    #auditory
    # Atributos de auditoría
    _create_date: Optional[datetime] = field(default=None)  # Cambiado a Any para evitar problemas de importación circular
    _id_user_create: Optional[int] = field(default=None)
    _update_date: Optional[datetime] = field(default_factory=datetime.now)
    _id_user_update: Optional[int] = field(default=None)
    _is_deleted: bool = field(default=False)
    _delete_date: Optional[datetime] = field(default_factory=datetime.now)
    _id_user_delete: Optional[int] = field(default=None)


    def __init__(self, id: int=-1, name: str="", user_name: str="", password: str="", activate: bool=True, role: Optional['Rol']=None) -> None:
        self.__id = id
        self.__name = name
        self.__user_name = user_name
        self.__password = password
        self.__activate = activate
        self.__role = role
      
   
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError("id must be an integer")
        self.__id = value
   

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("name must be a string")
        self.__name = value
   
    @property
    def user_name(self):
        return self.__user_name 
    @user_name.setter
    def user_name(self, value):
        if not isinstance(value, str):
            raise ValueError("username must be a string")
        self.__user_name = value
   
   
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise ValueError("password must be a string")
        self.__password = value
   
   
    @property
    def activate(self):
        return self.__activate
    @activate.setter
    def activate(self, value):
        if not isinstance(value, bool):
            raise ValueError("activate must be a boolean")
        self.__activate = value
   
   
    @property
    def role(self):
        return self.__role
    @role.setter
    def role(self, value):
        if not isinstance(value, Rol) and value is not None:
            raise ValueError("role must be an instance of Rol or None")
        self.__role = value       

        
    def __str__(self):
        return f"User(id={self.__id}, username='{self.__username}', activate={self.__activate}, role={self.__role})"
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self.__id == other.__id and self.__user_name == other.__user_name and self.__activate == other.__activate and self.__role == other.__role
    
    def __hash__(self):
        return hash((self.__id, self.__user_name, self.__activate, self.__role))
    