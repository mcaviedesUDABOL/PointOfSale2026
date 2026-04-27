import sys
import logging
from PySide6.QtWidgets import (QApplication, QMainWindow, QMdiArea, 
                             QMdiSubWindow, QTableWidget, QTableWidgetItem, 
                             QVBoxLayout, QWidget, QStatusBar)
from PySide6.QtGui import QAction
from config_logger import configure_logging
from data.connection.database_manager import DatabaseManager
from settings import Settings
from views.main_view import MainWindow



class Main:
    def __init__(self):
        configure_logging(logging.DEBUG)
         # Usar logger específico del módulo
        logger = logging.getLogger(__name__)
        logger.info("Aplicación iniciada")
        settings = Settings()
        url_database = settings.db_url
        self.db_manager = DatabaseManager(url_database)        
        # El constructor puede inicializar variables si es necesario
        print("App Point of Sale begin")
        app = QApplication(sys.argv)
        ventana = MainWindow()
        ventana.show()
        sys.exit(app.exec())


# Bloque de ejecución principal
if __name__ == "__main__":
    app = Main()