from data.seeds.base_seed import BaseSeed


class RolSeed(BaseSeed):
    
    def up(self):
        sql = """
            CREATE TABLE IF NOT EXISTS roles (
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
        index_sql = "CREATE INDEX IF NOT EXISTS idx_rols_name ON roles(name)"
        self.execute_sql(index_sql)

        
    def down(self):
        sql = "DROP TABLE IF EXISTS roles"
        self.execute_sql(sql)


    def seed(self):
        roles = [
            ("Admin", True, "Administrator with full permissions",'2025-10-25 14:30:00',1),
            ("Manager", True, "Manager with limited permissions",'2025-10-25 14:31:00',1),
            ("Cashier", True, "Cashier with permissions to process sales",'2025-10-25 14:32:00',1),
            ("Stock Clerk", True, "Stock clerk with permissions to manage inventory",'2025-10-25 14:33:00',1),
            ("Customer Service", True, "Customer service representative with permissions to assist customers",'2025-10-25 14:34:00',1)
        ]
        
        for name, activate, description, created_date, id_user_create in roles:
            try:
                sql = "INSERT INTO roles (name, activate, description, created_date, id_user_create) VALUES (?, ?, ?, ?, ?)"
                self.execute_sql(sql, (name, activate, description, created_date, id_user_create))
                print(f"  ✓ Added rol: {name}")
            except Exception as e:
                print(f"  ✗ Error adding rol {name}: {e}")

