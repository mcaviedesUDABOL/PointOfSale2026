from dataclasses import dataclass, field
from typing import ClassVar, Dict,List, Any, Optional

from models.category_model import Category

@dataclass
class Product:
    """Modelo de datos para Categoría"""
    __id: Optional[int] = field(default=None)
    __name: str = field(default="")
    __price: float = field(default=0.0)
    __bar_code: int = field(default=0)
    __category: Optional[Category] = None  # Referencia inversa opcional
    __activate: bool = field(default=True)
    __description: str = field(default="")

    def __init__(self,id: int=-1, name: str="", price: float=0.0, bar_code: int=0, activate: bool=True, description: str="" ) -> None:
        self.__id=id
        self.__name=name
        self.__price = price
        #self.__category = category
        self.__bar_code = bar_code       
        self.__activate=activate
        self.__description=description

    

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
    def price(self):        
        return self.__price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("price must be a number")
        self.__price = value

    
    @property
    def bar_code(self):
        return self.__bar_code
    
    @bar_code.setter
    def bar_code(self, value):
        self.__bar_code = value

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        self.__category = value

    @property
    def is_perishable(self):
        return self.__is_perishable

    @is_perishable.setter
    def is_perishable(self, value):
        if not isinstance(value, bool):
            raise ValueError("is_perishable must be a boolean")
        self._is_perishable = value
#identificacion

#Clasificación y Tipo

#sobre escritua de los metodos base de la clase Object

    def __str__(self):        
        return f"Product(id={self.id}, name='{self.name}', price={self.price})"
    
    def __repr__(self): 
        return self.__str__()
    
    def __eq__(self, other):
        if isinstance(other, Product):
            return self.id == other.__id
        return False
    def __hash__(self):  
        return hash(self.id)
