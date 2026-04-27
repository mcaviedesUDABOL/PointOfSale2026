from models.category_model import Category

class CategoryController:

    def __init__(self):
        # Diccionario para persistencia en memoria {id: objeto_categoria}
        self.__categories = {
            1: Category(1, "Bebidas", True, "Licores, refrescos, jugos"),
            2: Category(2, "Snacks", True, "Papas, galletas, chocolates"),
            3: Category(3, "Lácteos", True, "Leche, yogures, quesos"), 
        }
    
    # CREATE
    def create(self, category):
        if category.id in self.__categories:
            print(f"Error: La categoría con ID {category.id} ya existe.")
            return False
        
        #new_category = Category(id_cat, name, description)
        self.__categories[category.id] = category
        print(f"Categoría '{category.name}' creada exitosamente.")
        return True

    # READ
    def find(self, id_cat):
        return self.__categories.get(id_cat, "Categoría no encontrada.")

    def read(self, only_active=False):
        list_filter = [cat for cat in self.__categories.values() if cat.activate == True]
        return list_filter
    
    # UPDATE
    def update(self, id_cat, new_name=None, new_description=None, state=None):
        if id_cat not in self._categories:
            print("Error: Categoría no encontrada.")
            return False
        
        cat = self.__categories[id_cat]
        if new_name: cat.name = new_name
        if new_description: cat.descripcion = new_description
        if state is not None: cat.activate = state
        
        print(f"Categoría {id_cat} actualizada.")
        return True

    # DELETE (Borrado Lógico)
    # En sistemas de inventario, es mejor desactivar que borrar físicamente
    # para no romper el historial de productos.
    def delete(self, id_cat):
        if id_cat in self.__categories:
            # Opción A: Borrado físico
            # del self._categories[id_cat]            
            # Opción B: Desactivación (Recomendado)
            self.__categories[id_cat].activate = False
            print(f"Categoría {id_cat} marcada como inactiva.")
        else:
            print("Error: ID inexistente.")