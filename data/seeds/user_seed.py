from data.seeds.base_seed import BaseSeed


class UserSeed(BaseSeed):
    
    def up(self):
        sql = """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
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
            );
            -- Crear índices para mejorar el rendimiento
            CREATE INDEX idx_user_rol_id ON user(rol_id);
            CREATE INDEX idx_user_email ON user(email);
            CREATE INDEX idx_user_username ON user(username);
            CREATE INDEX idx_user_activo ON user(activo);
        """   

        self.execute_sql(sql)
      
        # Crear índices
        index_sql = "CREATE INDEX IF NOT EXISTS idx_users_username ON users(username)"
        self.execute_sql(index_sql)
    def down(self):
        sql = "DROP TABLE IF EXISTS users"
        self.execute_sql(sql)

    def seed(self):
        users = [
            ("admin", "admin123", "admin@example.com")
        ]
        for username, password, email in users:
            sql = """
                INSERT OR IGNORE INTO users (username, password, email) VALUES (?, ?, ?)
            """
            self.execute_sql(sql, (username, password, email))
            print(f"  ✓ Added user: {username}")

