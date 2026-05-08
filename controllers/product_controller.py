from dataclasses import fields
from math import prod

from models.abstract_product_model import AbstractProduct
from models.perishable_product_model import PerishableProduct
from models.non_perishable_product_model import NonPerishableProduct

from datetime import date
from typing import Optional
 
class ProductController:
    """Controlador para gestionar productos"""
    def __init__(self):
        self.products = [
            PerishableProduct(id=1, name="Leche", base_selling_price=3.5, bar_code=1234567890123, activate=True, description="Leche fresca", category=None, expiration_date=date(2024, 12, 31), manufacturing_date=date(2024, 1, 1), days_before_expiration=30, storage_attributes=None),
            NonPerishableProduct(id=2, name="Laptop", base_selling_price=1000.0, bar_code=9876543210123,
                                activate=True, description="Laptop de alta gama", category=None,
                                material="Aluminio", warranty_months=24, is_fragile=True, cleaning_instructions="Limpiar con paño seco")

        ]  
        # Lista para almacenar productos

#Reflexion: El controlador de productos es una clase que se encarga de gestionar la lógica relacionada con los productos en el sistema. En este caso, se ha implementado una lista de productos predefinidos para facilitar las pruebas y el desarrollo. La clase proporciona métodos para agregar nuevos productos, obtener un producto por su ID y listar todos los productos disponibles. Además, se incluye un método para obtener el esquema de una clase, lo que puede ser útil para entender los tipos de datos esperados al trabajar con instancias de productos.
    def add_product(self, product: AbstractProduct) -> None:

        # Creamos un producto (actúa como Auditable automáticamente)
        #prod = Producto(id=1, nombre="Laptop", precio=1000.0, id_user=10)
        # Usamos el controlador de auditoría
        #AuditoriaController.registrar_cambio(prod, id_editor=99)
        #AuditoriaController.eliminar_con_registro(prod)
        # Verificación
        #print(f"Estado final: {prod.nombre} | is_deleted: {prod.is_deleted}")

        """Agrega un nuevo producto a la lista"""
        if not isinstance(product, AbstractProduct):
            raise ValueError("El producto debe ser una instancia de AbstractProduct")
        self.products.append(product)

    def get_product_by_id(self, product_id: int) -> Optional[AbstractProduct]:
        """Obtiene un producto por su ID"""
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def list_products(self) -> list:
        """Devuelve la lista de productos"""
        return self.products

    from dataclasses import fields

    def obtener_esquema(self, clase):
        """Retorna los tipos de datos esperados de la clase Producto"""
        print(f"Esquema de {clase.__name__}:")
        for campo in fields(clase):
            print(f" -> {campo.name}: {campo.type}")
    