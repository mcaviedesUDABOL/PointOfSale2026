from models.category_model import Category
from data.dao.base_dao import BaseDAO
from data.dao.category_dao import CategoryDAO
from data.connection.database_manager import DatabaseManager
from interfaces.auditable import Auditable
from controllers.audit_controller import AuditController


class CategoryController:
    

    def __init__(self):        
        self.__categories = {}
        self.__db_manager = DatabaseManager()
        self.__category_dao = CategoryDAO(self.__db_manager)
        self.__categories = {cat.id: cat for cat in self.__category_dao.find_all_ordered()}
        self.__audit_controller = AuditController()

    # CREATE
    def create(self, category):
        self.__audit_controller.register_creation(category, id_user=1)  # Simulamos un ID de usuario        
        self.__category_dao.insert(category)
        self.__categories = {cat.id: cat for cat in self.__category_dao.find_all_ordered()}
        print(f"Categoría '{category.name}' creada exitosamente.")
        return True

    # READ
    def find(self, id_cat):
        return self.__categories.get(id_cat, "Categoría no encontrada.")

    def read(self, only_active=False):
        #list_filter = [cat for cat in self.__categories.values() if cat.activate == True]
        return self.__categories.values()
    
    # UPDATE
    def update(self, category):
        self.__audit_controller.register_update(category, id_user=1)  # Simulamos un ID de usuario 
        self.__category_dao.update(category.id, category)
        self.__categories = {cat.id: cat for cat in self.__category_dao.find_all_ordered()}
        print(f"Categoría {category.id} actualizada.")
        return True

    # DELETE (Borrado Lógico)
    def is_deleted(self, id_cat):
        category = self.__categories.get(id_cat)
        self.__audit_controller.mark_as_deleted(category, id_user=1)  # type: ignore # Simulamos un ID de usuario
        self.__category_dao.update(category.id, category) # type: ignore
        self.__categories = {cat.id: cat for cat in self.__category_dao.find_all_ordered()}
        print(f"Categoría {id_cat} marcada como eliminada.")

    # DELETE (Borrado Lógico)
    def delete(self, id_cat):
        if id_cat in self.__categories:
            self.__categories[id_cat].activate = False
            print(f"Categoría {id_cat} marcada como inactiva.")
        else:
            print("Error: ID inexistente.")