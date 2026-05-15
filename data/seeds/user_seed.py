from data.seeds.base_seed import BaseSeed


class UserSeed(BaseSeed):
    
    def up(self):
        sql = """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                user_name TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                activate BOOLEAN DEFAULT 0,
                rol_id INTEGER NOT NULL,
                created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                id_user_create INTEGER,
                updated_date TIMESTAMP,
                id_user_update INTEGER,
                is_deleted BOOLEAN DEFAULT 0,
                deleted_date TIMESTAMP,
                id_user_delete INTEGER,       
                FOREIGN KEY (rol_id) REFERENCES rol(id) ON DELETE RESTRICT ON UPDATE CASCADE         
            )         
        """   

        self.execute_sql(sql)

        # Crear índices
        index_sql = "CREATE INDEX IF NOT EXISTS idx_users_user_name ON users(user_name)"
        self.execute_sql(index_sql)
    def down(self):
        sql = "DROP TABLE IF EXISTS users"
        self.execute_sql(sql)

    def seed(self):    
        users = [
            ("admin", "admin", "admin123", "admin@example.com",1,1)
        ]
        for name, user_name, password, email, activate, rol_id in users:
            try:
                sql = """
                    INSERT INTO users (name, user_name, password, email, activate, rol_id) VALUES (?, ?, ?, ?, ?, ?)
                """
                self.execute_sql(sql, (name, user_name, password, email, 1, 1))
                print(f"  ✓ Added user: {user_name}")
            except Exception as e:
                print(f"  ✗ Error adding user {user_name}: {e}")
          

