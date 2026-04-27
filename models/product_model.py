class Product:
    def __init__(self, id=0, name="", price=0.0, new_category=None):
        self._id = id
        self._name = name
        self._price = price
        self._bar_code = None
        self._category = new_category
        self._is_perishable = False

#La isinstance()función comprueba si un objeto pertenece a una clase específica o a una tupla de clases.
# Devuelve verdadero Truesi el objeto es una instancia de la clase (o de cualquier clase de la tupla); 
# de lo contrario, devuelve falso False.

    @property
    def id(self):
        return self._id 
    
    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError("id must be an integer")
        self._id = value
    
    @property
    def name(self):
        return self._name
    
    @name.setter   
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("name must be a string")
    
    @property
    def price(self):        
        return self._price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("price must be a number")
        self._price = value

    
    @property
    def bar_code(self):
        return self._bar_code
    
    @bar_code.setter
    def bar_code(self, value):
        self._bar_code = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value

    @property
    def is_perishable(self):
        return self._is_perishable

    @is_perishable.setter
    def is_perishable(self, value):
        if not isinstance(value, bool):
            raise ValueError("is_perishable must be a boolean")
        self._is_perishable = value
#identificacion

#Clasificación y Tipo

#sobre escritua de los metodos base de la clase Object

    def __str__(self):        return f"Product(id={self.id}, name='{self.name}', price={self.price})"
    
    def __repr__(self):        return self.__str__()
    
    def __eq__(self, other):
        if isinstance(other, Product):
            return self.id == other.id
        return False
    def __hash__(self):  
        return hash(self.id)
