from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from models.category_model import Category

@dataclass
class AbstractProduct(ABC):
    """Modelo de datos para Categoría"""
    __id: Optional[int] = field(default=None)
    __name: str = field(default="")
    __base_selling_price: float = field(default=0.0)
    __bar_code: int = field(default=0)
    __activate: bool = field(default=True)
    __description: str = field(default="")
    __category: Optional[Category] = None  # Referencia inversa opcional
    __SKU: str=field(default="") #(Stock Keeping Unit): El código alfanumérico interno para control de inventario.
    

    def __init__(self,id: int=-1, name: str="", base_selling_price: float=0.0, bar_code: int=0, 
                 activate: bool=True, description: str="",
                   category: Optional[Category] = None) -> None:
        self.__id=id
        self.__name=name
        self.__base_selling_price = base_selling_price
        self.__bar_code = bar_code       
        self.__activate=activate
        self.__description=description
        self.__category=category
        self.__SKU="0000000000"


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
    def sale_price(self):        
        return self.__base_selling_price    
    @sale_price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("price must be a number")
        self.__base_selling_price = value

    
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
    def SKU(self):
        return self.__SKU
    @SKU.setter
    def SKu(self, value):
        self.__SKU = value
        

    #metodos abstractos
    @abstractmethod
    def calculate_final_price(self):
        pass
