from dataclasses import dataclass, field
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from models.category_model import Category

@dataclass
class Product:
    """Modelo de datos para Categoría"""
    __id: Optional[int] = field(default=None)
    __name: str = field(default="")
    __price: float = field(default=0.0)
    __bar_code: int = field(default=0)
    __activate: bool = field(default=True)
    __description: str = field(default="")
    __category: Optional[Category] = None  # Referencia inversa opcional
    __is_perishable: bool = field(default=False)


    def __init__(self,id: int=-1, name: str="", price: float=0.0, bar_code: int=0, 
                 activate: bool=True, description: str="",
                   category: Optional[Category] = None, is_perishable: bool = False) -> None:
        self.__id=id
        self.__name=name
        self.__price = price
        self.__bar_code = bar_code       
        self.__activate=activate
        self.__description=description
        self.__category=category

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
        self.__is_perishable = value
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
