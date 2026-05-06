from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Any,  List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from models.rol_model import Rol

@dataclass
class Permission:

    __id: Optional[int] = field(default=None)
    __permission_name: str = field(default="")
    __rol: Optional[Rol] = None  # Referencia a Rol, puede ser None si no se asigna un rol específico
    __activate: bool = field(default=True)
    
    
    #auditory
    # Atributos de auditoría
    _create_date: Optional[datetime] = field(default=None)  # Cambiado a Any para evitar problemas de importación circular
    _id_user_create: Optional[int] = field(default=None)
    _update_date: Optional[datetime] = field(default_factory=datetime.now)
    _id_user_update: Optional[int] = field(default=None)
    _is_deleted: bool = field(default=False)
    _delete_date: Optional[datetime] = field(default_factory=datetime.now)
    _id_user_delete: Optional[int] = field(default=None)


    def __init__(self, id: int=-1, permission_name: str="", rol: Optional[Rol] = None, activate: bool=True) -> None:
        self.__id = id
        self.__permission_name = permission_name
        self.__rol = rol
        self.__activate = activate

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError("id must be an integer")
        self.__id = value


    @property
    def permission_name(self):
        return self.__permission_name   
    @permission_name.setter
    def permission_name(self, value):
        if not isinstance(value, str):
            raise ValueError("permission_name must be a string")
        self.__permission_name = value


    @property
    def rol(self):
        return self.__rol
    @rol.setter
    def rol(self, value):
        if value is not None and not isinstance(value, Rol):
            raise ValueError("rol must be an instance of Rol or None")
        self.__rol = value
    

    @property
    def activate(self):
        return self.__activate
    @activate.setter
    def activate(self, value):
        if not isinstance(value, bool):
            raise ValueError("activate must be a boolean")
        self.__activate = value


    def __str__(self):
        return f"Permission(id={self.__id}, permission_name='{self.__permission_name}', rol={self.__rol}, activate={self.__activate})"
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        if not isinstance(other, Permission):
            return NotImplemented
        return self.__id == other.__id and self.__permission_name == other.__permission_name and self.__rol == other.__rol and self.__activate == other.__activate
    
    def __hash__(self):
        return hash((self.__id, self.__permission_name, self.__rol, self.__activate))
    
    