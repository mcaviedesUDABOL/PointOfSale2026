from typing import Optional

from data.seeds.base_seed import BaseSeed


class CategorySeed(BaseSeed):
    """Seed para la tabla de categorías"""
    
    def up(self):
        """Crea la tabla de categorías"""
        sql = """
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                activate BOOLEAN DEFAULT 0,
                description TEXT,
                created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                id_user_create INTEGER,
                updated_date TIMESTAMP,
                id_user_update INTEGER,
                is_deleted BOOLEAN DEFAULT 0,
                deleted_date TIMESTAMP,
                id_user_delete INTEGER                
            )
        """   

        self.execute_sql(sql)
      
        # Crear índices
        index_sql = "CREATE INDEX IF NOT EXISTS idx_categories_name ON categories(name)"
        self.execute_sql(index_sql)
    
    def down(self):
        """Elimina la tabla de categorías"""
        sql = "DROP TABLE IF EXISTS categories"
        self.execute_sql(sql)
    
    def seed(self):
        """Puebla la tabla con datos iniciales"""
        categories = [
            ("Electronics", True, "Electronic products, gadgets, and accessories",'2025-10-25 14:30:00',1),
            ("Clothing", True, "Clothing, shoes, and fashion accessories",'2025-10-25 14:31:00',1),
            ("Home & Garden", True, "Home decor, furniture, and garden supplies",'2025-10-25 14:32:00',1),
            ("Sports", True, "Sports equipment and outdoor gear",'2025-10-25 14:33:00',1),
            ("Books", True, "Books, magazines, and educational materials",'2025-10-25 14:34:00',1),
            ("Toys", True, "Toys, games, and hobbies",'2025-10-25 14:35:00',1),
            ("Health & Beauty", True, "Health products, cosmetics, and personal care",'2023-10-25 14:36:00',1),
            ("Automotive", True, "Car parts, accessories, and tools",'2023-10-25 14:37:00',1),
            ("Pet Supplies", True, "Food, toys, and accessories for pets",'2023-10-25 14:38:00',1),
            ("Office Supplies", True, "Office equipment, stationery, and furniture",'2023-10-25 14:39:00',1)
        ]
        
        for name, activate, description, created_date, id_user_create in categories:
            try:
                sql = "INSERT INTO categories (name, activate, description, created_date, id_user_create) VALUES (?, ?, ?, ?, ?)"
                self.execute_sql(sql, (name, activate, description, created_date, id_user_create))
                print(f"  ✓ Added category: {name}")
            except Exception as e:
                print(f"  ✗ Error adding category {name}: {e}")
        
        # Verificar que se insertaron datos
        count_sql = "SELECT COUNT(*) as count FROM categories"
        result = self.execute_query(count_sql)
        count = result[0]['count'] if result else 0
        print(f"\n✓ Total categories in database: {count}")
