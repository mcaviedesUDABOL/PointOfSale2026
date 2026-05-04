from dataclasses import dataclass, field
from datetime import date
from typing import Any, List, Optional, TYPE_CHECKING


@dataclass
class Rol:
    __id: Optional[int] = field(default=None)
    __name: str = field(default="")
    __activate: bool = field(default=True)    
    __description: str = field(default="")
    __permissions: List[str] = field(default_factory=list)


    def __init__(self, id: int=-1, name: str="", activate: bool=True, description: str="", permissions: List[str]=None) -> None:
        self.__id = id
        self.__name = name
        self.__activate = activate   
        self.__description = description    
        self.__permissions = permissions if permissions is not None else []
    
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
    def activate(self):
        return self.__activate
    @activate.setter
    def activate(self, value):
        if not isinstance(value, bool):
            raise ValueError("activate must be a boolean")
        self.__activate = value
   

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise ValueError("description must be a string")
        self.__description = value

    @property
    def permissions(self):
        return self.__permissions
    @permissions.setter
    def permissions(self, value):
        if not isinstance(value, list):
            raise ValueError("permissions must be a list")
        self.__permissions = value


    def __str__(self):
        return f"Rol(id={self.__id}, name='{self.__name}', activate={self.__activate}, description='{self.__description}')"


    def __repr__(self):
        return self.__str__()


    def __eq__(self, other):
        if not isinstance(other, Rol):
            return NotImplemented
        return self.__id == other.__id and self.__name == other.__name and self.__activate == other.__activate and self.__description == other.__description


    def __hash__(self):
        return hash((self.__id, self.__name, self.__description))