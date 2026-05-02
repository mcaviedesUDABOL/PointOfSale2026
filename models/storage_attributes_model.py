from dataclasses import dataclass, field
from typing import Optional


@dataclass
class StorageAttributes():
    """Modelo de datos para Categoría"""
    __id: Optional[int] = field(default=None)
    __optimal_temperature: float = field(default=0.0)
    __maximum_humidity: float = field(default=0.0)
    __storage_instructions: str = field(default="")
    __perishable_product_id: Optional[int] = field(default=None)

    def __init__(self, id: int=-1, optimal_temperature: float=0.0, 
                 maximum_humidity: float=0.0, storage_instructions: str="", 
                 perishable_product_id: Optional[int] = None) -> None:
        self.__id = id
        self.__optimal_temperature = optimal_temperature
        self.__maximum_humidity = maximum_humidity
        self.__storage_instructions = storage_instructions
        self.__perishable_product_id = perishable_product_id


    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError("id must be an integer")
        self.__id = value
    
    
    @property
    def optimal_temperature(self):
        return self.__optimal_temperature
    @optimal_temperature.setter
    def optimal_temperature(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("optimal_temperature must be a number")
        self.__optimal_temperature = value
    
    
    @property
    def maximum_humidity(self):
        return self.__maximum_humidity
    @maximum_humidity.setter
    def maximum_humidity(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("maximum_humidity must be a number")
        self.__maximum_humidity = value
    
    
    @property
    def storage_instructions(self):
        return self.__storage_instructions
    @storage_instructions.setter
    def storage_instructions(self, value):
        if not isinstance(value, str):
            raise ValueError("storage_instructions must be a string")
        self.__storage_instructions = value

    
    @property
    def perishable_product_id(self):
        return self.__perishable_product_id
    @perishable_product_id.setter
    def perishable_product_id(self, value):
        if not isinstance(value, int) and value is not None:
            raise ValueError("perishable_product_id must be an integer or None")
        self.__perishable_product_id = value


    def __str__(self):
        return f"StorageAttributes(id={self.id}, optimal_temperature={self.optimal_temperature}, maximum_humidity={self.maximum_humidity})"
    
    
    def __repr__(self):
        return self.__str__()
    
    
    def __eq__(self, other):
        if not isinstance(other, StorageAttributes):
            return NotImplemented
        return self.id == other.id
    

    def __hash__(self): 
        return hash(self.id)

    
    