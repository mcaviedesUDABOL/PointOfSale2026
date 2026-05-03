# dao/category_dao.py
from typing import List, Optional
from data.connection.database_manager import DatabaseManager
from dao.base_dao import BaseDAO
#from dto.category_dto import CategoryDTO
from models.category_model import Category

class CategoryDAO(BaseDAO[Category]):
    """DAO específico para Category"""
    
    def __init__(self, db_manager: DatabaseManager):
        super().__init__(db_manager)
    
    def get_table_name(self) -> str:
        return "categories"
    
    def row_to_dto(self, row: dict) -> Category:
        """Convierte una fila de la base de datos a Category"""
        return Category(
            id=row.get('id'),
            name=row.get('name'),
            description=row.get('description'),
            created_at=row.get('created_at'),
            updated_at=row.get('updated_at')
        )
    
    def dto_to_dict(self, dto: Category) -> dict:
        """Convierte CategoryDTO a diccionario"""
        data = {}
        if dto.name is not None:
            data['name'] = dto.name
        if dto.description is not None:
            data['description'] = dto.description
        if dto.id is not None:
            data['id'] = dto.id
        return data
    
    # Métodos específicos para Category
    def find_by_name(self, name: str) -> Optional[Category]:
        """Busca categoría por nombre exacto"""
        query = "SELECT * FROM categories WHERE name = ?"
        results = self.db_manager.execute_query(query, (name,))
        return self.row_to_dto(results[0]) if results else None
    
    def search_by_name(self, search_term: str) -> List[Category]:
        """Busca categorías por nombre parcial"""
        query = "SELECT * FROM categories WHERE name LIKE ? ORDER BY name"
        results = self.db_manager.execute_query(query, (f"%{search_term}%",))
        return [self.row_to_dto(row) for row in results]
    
    def find_all_ordered(self, order_by: str = "name", ascending: bool = True) -> List[Category]:
        """Obtiene todas las categorías ordenadas"""
        direction = "ASC" if ascending else "DESC"
        query = f"SELECT * FROM categories ORDER BY {order_by} {direction}"
        results = self.db_manager.execute_query(query)
        return [self.row_to_dto(row) for row in results]
    
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


