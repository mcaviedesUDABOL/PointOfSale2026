from data.seeds.base_seed import BaseSeed


class CategorySeed(BaseSeed):
    """Seed para la tabla de categorías"""
    
    def up(self):
        """Crea la tabla de categorías"""
        sql = """
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """
        self.execute_sql(sql)
        
        # Crear trigger para actualizar updated_at
        trigger_sql = """
            CREATE TRIGGER IF NOT EXISTS update_categories_updated_at 
            AFTER UPDATE ON categories
            BEGIN
                UPDATE categories 
                SET updated_at = CURRENT_TIMESTAMP 
                WHERE id = NEW.id;
            END
        """
        self.execute_sql(trigger_sql)
        
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
            ("Electronics", "Electronic products, gadgets, and accessories"),
            ("Clothing", "Clothing, shoes, and fashion accessories"),
            ("Home & Garden", "Home decor, furniture, and garden supplies"),
            ("Sports", "Sports equipment and outdoor gear"),
            ("Books", "Books, magazines, and educational materials"),
            ("Toys", "Toys, games, and hobbies"),
            ("Health & Beauty", "Health products, cosmetics, and personal care"),
            ("Automotive", "Car parts, accessories, and tools"),
            ("Pet Supplies", "Food, toys, and accessories for pets"),
            ("Office Supplies", "Office equipment, stationery, and furniture")
        ]
        
        for name, description in categories:
            try:
                sql = "INSERT INTO categories (name, description) VALUES (?, ?)"
                self.execute_sql(sql, (name, description))
                print(f"  ✓ Added category: {name}")
            except Exception as e:
                print(f"  ✗ Error adding category {name}: {e}")
        
        # Verificar que se insertaron datos
        count_sql = "SELECT COUNT(*) as count FROM categories"
        result = self.execute_query(count_sql)
        count = result[0]['count'] if result else 0
        print(f"\n✓ Total categories in database: {count}")
