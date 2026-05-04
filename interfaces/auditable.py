from typing import Protocol, Optional, runtime_checkable
from datetime import date, datetime

@runtime_checkable
class Auditable(Protocol):
    # Atributos requeridos
    _create_date: Optional[datetime]
    _id_user_create: Optional[int]
    _update_date: Optional[datetime]
    _id_user_update: Optional[int]
    _is_deleted: bool = False
    _delete_date: Optional[datetime]
    _id_user_delete: Optional[int]


    def register_creation(self, user_id: int) -> None:
        """Método requerido para registrar creación"""
        self._create_date = datetime.now()
        self._id_user_create = user_id
    

    def register_update(self, user_id: int) -> None:
        """Método requerido para registrar actualización"""
        self._update_date = datetime.now()
        self._id_user_update = user_id
    

    def mark_as_deleted(self, user_id: int) -> None:
        """Método requerido para borrado lógico"""
        self._is_deleted = True
        self._delete_date = datetime.now()
        self._id_user_delete = user_id 
    
    
    @property
    def create_date(self) -> Optional[datetime]:
        return self._create_date
    # @create_date.setter
    # def create_date(self, value: date):
    #     if not isinstance(value, date):
    #         raise ValueError("create_date must be a date")
    #     self._create_date = value   
    

    @property
    def id_user_create(self) -> Optional[int]:
        return self._id_user_create
    # @id_user_create.setter
    # def id_user_create(self, value: Optional[int]):
    #     if value is not None and not isinstance(value, int):
    #         raise ValueError("id_user_create must be an integer or None")
    #     self._id_user_create = value


    @property
    def update_date(self) -> Optional[datetime]:
        return self._update_date
    # @update_date.setter
    # def update_date(self, value: date):
    #     if not isinstance(value, date):
    #         raise ValueError("update_date must be a date")
    #     self._update_date = value


    @property
    def id_user_update(self) -> Optional[int]:
        return self._id_user_update
    # @id_user_update.setter
    # def id_user_update(self, value: Optional[int]):
    #     if value is not None and not isinstance(value, int):
    #         raise ValueError("id_user_update must be an integer or None")
    #     self._id_user_update = value


    @property
    def is_deleted(self) -> bool:
        return self._is_deleted
    # @is_deleted.setter
    # def is_deleted(self, value: bool):
    #     if not isinstance(value, bool):
    #         raise ValueError("is_deleted must be a boolean")
    #     self._is_deleted = value


    @property
    def delete_date(self) -> Optional[datetime]:
        return self._delete_date
    # @delete_date.setter
    # def delete_date(self, value: date):
    #     if not isinstance(value, date):
    #         raise ValueError("delete_date must be a date")
    #     self._delete_date = value
    
    
    @property
    def id_user_delete(self) -> Optional[int]:
        return self._id_user_delete
    # @id_user_delete.setter
    # def id_user_delete(self, value: Optional[int]):
    #     if value is not None and not isinstance(value, int):
    #         raise ValueError("id_user_delete must be an integer or None")
    #     self._id_user_delete = value
    