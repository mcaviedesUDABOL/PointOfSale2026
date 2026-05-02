from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Optional, List, TYPE_CHECKING
from datetime import date, datetime
from models.abstract_product_model import AbstracProduct
from models.storage_attributes_model import StorageAttributes

if TYPE_CHECKING:
    from models.category_model import Category

@dataclass
class PerishableProduct(AbstracProduct):

    __expiration_date: date = field(default_factory=date.today) 
    __manufacturing_date:  date = field(default=date(1900, 1, 1)) 
    __days_before_expiration: int = field(default=0)
    __storage_attributes: Optional['StorageAttributes'] = field(default=None)


    def __init__(self, id: int=-1, name: str="", base_selling_price: float=0.0, bar_code: int=0, 
                 activate: bool=True, description: str="",
                   category: Optional[Category] = None,
                   expiration_date: date = date.today(), manufacturing_date: date = date(1900, 1, 1), 
                   days_before_expiration: int = 0, 
                   storage_attributes: Optional['StorageAttributes'] = None) -> None:
        super().__init__(id, name, base_selling_price, bar_code, activate, description, category)
        self.__expiration_date = expiration_date
        self.__manufacturing_date = manufacturing_date
        self.__days_before_expiration = days_before_expiration
        self.__storage_attributes = storage_attributes


    @property
    def expiration_date(self):
        return self.__expiration_date 
    @expiration_date.setter
    def expiration_date(self, value):
        self.__expiration_date = value


    @property
    def manufacturing_date(self):
        return self.__manufacturing_date
    @manufacturing_date.setter
    def manufacturing_date(self, value):
        self.__manufacturing_date = value


    @property
    def days_before_expiration(self):
        return self.__days_before_expiration
    @days_before_expiration.setter
    def days_before_expiration(self, value):
        self.__days_before_expiration = value


    @property
    def storage_attributes(self):
        return self.__storage_attributes
    @storage_attributes.setter
    def storage_attributes(self, value):
        self.__storage_attributes = value


     #metodos sobreescritos
    def __str__(self):        
        return f"Product(id={self.id}, name='{self.name}', price={self.price})"
    

    def __repr__(self): 
        return self.__str__()
    

    def __eq__(self, other):
        if isinstance(other, PerishableProduct):
            return self.id == other.__id
        return False
    

    def __hash__(self):  
        return hash(self.id)
    
    #implementacion metodos abstractos
    def calculate_sale_price(self) -> float:
        today = date.today()
        if self.expiration_date < today:
            return 0.0
        elif self.expiration_date == today:
            return self.sale_price * 0.5
        elif (self.expiration_date - today).days <= self.days_before_expiration:
            return self.sale_price * 0.8
        else:
            return self.sale_price


