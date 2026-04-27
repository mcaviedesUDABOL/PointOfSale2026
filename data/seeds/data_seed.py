import sqlite3

class SeedData:
    def __init__(self, db_name="warehouse.db"):
        self.db_name = db_name

    def create_database(self):
        """Crea la base de datos y la tabla category con las especificaciones dadas."""
        try:
            # Conexión a la base de datos (se crea el archivo si no existe)
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Creación de la tabla Category
            # Nota: SQLite no limita estrictamente el tamaño de VARCHAR como otros motores,
            # pero se define por estándar y documentación.
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS category (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL CHECK(length(name) <= 50),
                    activate BOOLEAN DEFAULT 0,
                    description TEXT CHECK(length(description) <= 200)
                )
            """)

            conn.commit()
            print(f"Base de datos '{self.db_name}' y tabla 'category' creadas con éxito.")
            
        except sqlite3.Error as e:
            print(f"Error al crear la base de datos: {e}")
        finally:
            if conn:
                conn.close()

    def seed_categories(self):
        """Inserta datos iniciales de prueba."""
        categories = [
            ('Lácteos', 1, 'Productos derivados de la leche y quesos'),
            ('Limpieza', 0, 'Artículos para el aseo del hogar'),
            ('Electrónica', 1, 'Componentes y dispositivos electrónicos')
        ]

        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            cursor.executemany("""
                INSERT INTO category (name, activate, description) 
                VALUES (?, ?, ?)
            """, categories)
            
            conn.commit()
            print("Datos iniciales insertados correctamente.")
            
        except sqlite3.Error as e:
            print(f"Error al insertar semillas: {e}")
        finally:
            if conn:
                conn.close()

# --- Ejecución del Script ---
if __name__ == "__main__":
    seeder = SeedData()
    seeder.create_database()
    seeder.seed_categories()