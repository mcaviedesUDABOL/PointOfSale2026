from typing import Protocol, Optional, runtime_checkable
from datetime import date

@runtime_checkable
class Auditable(Protocol):
    # Atributos requeridos
    __create_date: date
    __id_user_create: Optional[int]
    __update_date: date
    __id_user_update: Optional[int]
    __is_deleted: bool
    __delete_date: date
    __id_user_delete: Optional[int]

    def mark_as_deleted(self) -> None:
        """Método requerido para borrado lógico"""
        self.__is_deleted = True
        self.__delete_date = date.today()
    
    
    @property
    def create_date(self) -> date:
        return self.__create_date
    @create_date.setter
    def create_date(self, value: date):
        if not isinstance(value, date):
            raise ValueError("create_date must be a date")
        self.__create_date = value   
    

    @property
    def id_user_create(self) -> Optional[int]:
        return self.__id_user_create
    @id_user_create.setter
    def id_user_create(self, value: Optional[int]):
        if value is not None and not isinstance(value, int):
            raise ValueError("id_user_create must be an integer or None")
        self.__id_user_create = value


    @property
    def update_date(self) -> date:
        return self.__update_date
    @update_date.setter
    def update_date(self, value: date):
        if not isinstance(value, date):
            raise ValueError("update_date must be a date")
        self.__update_date = value


    @property
    def id_user_update(self) -> Optional[int]:
        return self.__id_user_update
    @id_user_update.setter
    def id_user_update(self, value: Optional[int]):
        if value is not None and not isinstance(value, int):
            raise ValueError("id_user_update must be an integer or None")
        self.__id_user_update = value


    @property
    def is_deleted(self) -> bool:
        return self.__is_deleted
    @is_deleted.setter
    def is_deleted(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("is_deleted must be a boolean")
        self.__is_deleted = value


    @property
    def delete_date(self) -> date:
        return self.__delete_date
    @delete_date.setter
    def delete_date(self, value: date):
        if not isinstance(value, date):
            raise ValueError("delete_date must be a date")
        self.__delete_date = value
    
    
    @property
    def id_user_delete(self) -> Optional[int]:
        return self.__id_user_delete
    @id_user_delete.setter
    def id_user_delete(self, value: Optional[int]):
        if value is not None and not isinstance(value, int):
            raise ValueError("id_user_delete must be an integer or None")
        self.__id_user_delete = value
    