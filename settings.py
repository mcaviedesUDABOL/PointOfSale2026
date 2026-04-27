from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Punto de Venta"
    debug: bool = False
    db_url: str  ="data/database/point_of_sale_database.db"# Esta es obligatoria y debe venir de una variable de entorno

    class Config:
        env_file = ".env"  # Archivo desde el que cargar las variables
