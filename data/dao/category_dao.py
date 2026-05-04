# dao/category_dao.py
from typing import List, Optional
from data.connection.database_manager import DatabaseManager
from data.dao.base_dao import BaseDAO
from models.category_model import Category

class CategoryDAO(BaseDAO[Category]):
    """DAO específico para Category"""
    

    def __init__(self, db_manager: DatabaseManager):
        super().__init__(db_manager)
    

    def get_table_name(self) -> str:
        return "categories"
    

    def row_to_model(self, row: dict) -> Category:
        """Convierte una fila de la base de datos a Category"""
        return Category(
            id=int(row['id']) if 'id' in row and row['id'] is not None else -1,
            name=row['name'] if 'name' in row else "",
            activate=row['activate'] if 'activate' in row else True,
            description=row['description'] if 'description' in row else ""
        )
    

    def model_to_dict(self, model: Category) -> dict:
        """Convierte CategoryModel a diccionario"""
        data = {}
        if model.id != -1:
            data['id'] = model.id
        if model.name is not None:
            data['name'] = model.name
        if model.activate is not None:
            data['activate'] = model.activate            
        if model.description is not None:
            data['description'] = model.description  
        return data
    

    # Métodos específicos para Category
    def find_by_name(self, name: str) -> Optional[Category]:
        """Busca categoría por nombre exacto"""
        query = "SELECT * FROM categories WHERE name = ?"
        results = self.db_manager.execute_query(query, (name,))
        return self.row_to_model(results[0]) if results else None
    
    
    def search_by_name(self, search_term: str) -> List[Category]:
        """Busca categorías por nombre parcial"""
        query = "SELECT * FROM categories WHERE name LIKE ? ORDER BY name"
        results = self.db_manager.execute_query(query, (f"%{search_term}%",))
        return [self.row_to_model(row) for row in results]
    
    
    def find_all_ordered(self, order_by: str = "name", ascending: bool = True) -> List[Category]:
        """Obtiene todas las categorías ordenadas"""
        direction = "ASC" if ascending else "DESC"
        query = f"SELECT * FROM categories where activate = 1 ORDER BY {order_by} {direction}"
        results = self.db_manager.execute_query(query)
        return [self.row_to_model(row) for row in results]
    
    
    def get_statistics(self) -> dict:
        """Obtiene estadísticas de categorías"""
        query = """
            SELECT 
                COUNT(*) as total_categories,
                COUNT(DISTINCT name) as unique_names,
                MAX(created_at) as last_created
            FROM categories
        """
        results = self.db_manager.execute_query(query)
        return results[0] if results else {}
    

   

