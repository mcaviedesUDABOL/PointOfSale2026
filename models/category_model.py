from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Category:
    """Modelo de datos para Categoría"""
    id: Optional[int] = field(default=None)
    name: str = field(default="")
    activate: bool = field(default=False)
    description: str = field(default="")

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise 0
        self._id = value


    @property
    def name(self):
        return self._name  
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("name must be a string")
        self._name = value
    
    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise ValueError("description must be a string")
        self._description = value

    @property
    def activate(self):
        return self._activate 
    @activate.setter
    def activate(self, value):
        if not isinstance(value, bool):
            raise ValueError("activa must be a boolean")
        self._activate = value

    
    def __str__(self):
        return f"Category(id={self._id}, name='{self._name}')"
    def __repr__(self):
        return self.__str__()
    def __eq__(self, other):
        if isinstance(other, Category):
            return self._id == other._id and self._name == other._name
        return False
    def __hash__(self):        
        return hash((self._id, self._name))