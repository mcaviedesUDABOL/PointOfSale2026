# models/category_model.py
from dataclasses import dataclass, field
from typing import Any, List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from models.product_model import Product


@dataclass
class Category:
    """Modelo de datos para Categoría"""
    __id: Optional[int] = field(default=None)
    __name: str = field(default="")
    __activate: bool = field(default=True)
    __description: str = field(default="")
    __products: List['Product'] = field(default_factory=list)

    def __init__(self,id: int=-1, name: str="", activate: bool=True,
                  description: str="", products: List['Product'] = None ) -> None:
        self.__id=id
        self.__name=name
        self.__activate=activate
        self.__description=description
        self.__products = products if products is not None else []

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise -1 # type: ignore
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
    def description(self):
        return self.__description
    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise ValueError("description must be a string")
        self.__description = value


    @property
    def activate(self):
        return self.__activate 
    @activate.setter
    def activate(self, value):
        if not isinstance(value, bool):
            raise ValueError("activa must be a boolean")
        self.__activate = value


    @property
    def products(self):
        return self.__products
    @products.setter
    def products(self, value):
        if not isinstance(value, list):
            raise ValueError("products must be a list")
        self.__products = value
    
    
    def __str__(self):
        return f"Category(id={self.__id}, name='{self.__name}')"
    def __repr__(self):
        return self.__str__()
    def __eq__(self, other):
        if isinstance(other, Category):
            return self.__id == other.__id and self.__name == other.__name
        return False
    def __hash__(self):        
        return hash((self.__id, self.__name))