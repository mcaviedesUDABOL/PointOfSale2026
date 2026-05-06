from data.seeds.base_seed import BaseSeed


class PermissionSeed(BaseSeed):
    def up(self):
        sql = """
            CREATE TABLE IF NOT EXISTS permissions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                permission_name TEXT NOT NULL UNIQUE,
                rol_id INTEGER,
                description TEXT,               
                created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                id_user_create INTEGER,
                updated_date TIMESTAMP,
                id_user_update INTEGER,
                is_deleted BOOLEAN DEFAULT 0,
                deleted_date TIMESTAMP,
                id_user_delete INTEGER,
                FOREIGN KEY (rol_id) REFERENCES rols(id)
            );

            

        """   

        self.execute_sql(sql)
      
        # Crear índices
        index_sql = "CREATE INDEX IF NOT EXISTS idx_permissions_name ON permissions(name)"
        self.execute_sql(index_sql)

        
    def down(self):
        sql = "DROP TABLE IF EXISTS permissions"
        self.execute_sql(sql)

    def seed(self):
        permissions = [
            ("Manage Users", 1, "Permission to manage user accounts",'2025-10-25 14:30:00',1),
            ("Manage Inventory", 1, "Permission to manage inventory items",'2025-10-25 14:31:00',1),
            ("Process Sales", 1, "Permission to process sales transactions",'2025-10-25 14:32:00',1),
            ("View Reports", 1, "Permission to view sales and inventory reports",'2025-10-25 14:33:00',1),
            ("Customer Support", 1, "Permission to assist customers with inquiries and issues",'2025-10-25 14:34:00',1)
        ]
        
        for permission_name, rol_id, description, created_date, id_user_create in permissions:
            try:
                sql = "INSERT INTO permissions (permission_name, rol, description, created_date, id_user_create) VALUES (?, ?, ?, ?, ?)"
                self.execute_sql(sql, (permission_name, rol_id, description, created_date, id_user_create))
                print(f"  ✓ Added permission: {permission_name}")
            except Exception as e:
                print(f"  ✗ Error adding permission {permission_name}: {e}")
