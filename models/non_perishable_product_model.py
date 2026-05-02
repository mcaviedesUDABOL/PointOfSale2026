from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Optional, List, TYPE_CHECKING

from models.abstract_product_model import AbstracProduct
from models.category_model import Category

@dataclass
class NonPerishableProduct(AbstracProduct):

    __material: str = field(default="")
    __warranty_months: int = field(default=0)
    __is_fragile: bool = field(default=False)
    __cleaning_instructions: str = field(default="")

    def __init__(self, id: int=-1, name: str="", base_selling_price: float=0.0, bar_code: int=0, 
                 activate: bool=True, description: str="", category: Optional[Category] = None, material: str="", warranty_months: int=0, 
                 is_fragile: bool=False, cleaning_instructions: str="") -> None:
        super().__init__(id, name, base_selling_price, bar_code, activate, description, category)
        self.__material = material
        self.__warranty_months = warranty_months
        self.__is_fragile = is_fragile
        self.__cleaning_instructions = cleaning_instructions


    @property
    def material(self):
        return self.__material
    @material.setter
    def material(self, value):
        self.__material = value


    @property
    def warranty_months(self):
        return self.__warranty_months
    @warranty_months.setter
    def warranty_months(self, value):
        self.__warranty_months = value


    @property
    def is_fragile(self):
        return self.__is_fragile
    @is_fragile.setter
    def is_fragile(self, value):
        self.__is_fragile = value


    @property
    def cleaning_instructions(self):
        return self.__cleaning_instructions
    @cleaning_instructions.setter
    def cleaning_instructions(self, value):
        self.__cleaning_instructions = value


     #metodos sobreescritos
    def __str__(self):        
        return f"Product(id={self.id}, name='{self.name}', price={self.price})"


    def __repr__(self): 
        return self.__str__()


    def __eq__(self, other):
        if isinstance(other, NonPerishableProduct):
            return self.id == other.__id
        return False


    def __hash__(self):  
        return hash(self.id)

    
    #implementar metodos especificos para productos no perecibles
    def calculate_sale_price(self) -> float:
        # Para productos no perecibles, el precio de venta es simplemente el precio base
        return self.sale_price
    