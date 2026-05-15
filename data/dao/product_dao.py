from typing import List, Optional
from data.connection.database_manager import DatabaseManager
from data.dao.base_dao import BaseDAO
from models.abstract_product_model import AbstractProduct
from models.non_perishable_product_model import NonPerishableProduct
from models.perishable_product_model import PerishableProduct

class ProductDAO(BaseDAO[AbstractProduct]):
    
    def __init__(self, db_manager: DatabaseManager):
        super().__init__(db_manager)

