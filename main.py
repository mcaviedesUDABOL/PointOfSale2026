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
from utils.utilities import load_style
from PySide6.QtCore import QTranslator, QLibraryInfo, QLocale
from PySide6.QtCore import QLibraryInfo, QFileInfo
from utils.session import Session

class Main:

    def __init__(self): 
        #inicio de Session      
        current_session = Session() 
        #inicio de logs
        self.__load_logs()        
        url_database = self.__load_database_url()
        self.db_manager = DatabaseManager(url_database)                        
        # El constructor puede inicializar variables si es necesario
        print("App Point of Sale begin")
        app = QApplication(sys.argv)
        #hoja de estilos
        load_style(app, "views/styles/style.qss")
        #internacionalización
        # Aquí podrías cargar archivos de traducción si los tienes, por ejemplo:
        translator = QTranslator()
        if translator.load("es_BO", "locales"):
            app.installTranslator(translator)
        qt_translator = QTranslator()
        if qt_translator.load(QLocale.system(), "qtbase", "_", 
                            QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath)):
            app.installTranslator(qt_translator)
        ventana = MainWindow()
        ventana.show()
        sys.exit(app.exec())
    
    def __load_logs(self):
    # Método para cargar los logs, si es necesario
        configure_logging(logging.DEBUG)
         # Usar logger específico del módulo
        logger = logging.getLogger(__name__)
        logger.info("Aplicación iniciada")

    def __load_database_url(self):
        settings = Settings()
        return settings.db_url

    

# Bloque de ejecución principal
if __name__ == "__main__":
    app = Main()