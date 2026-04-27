import logging
import sys

def configure_logging(level=logging.INFO):
    """Configura el sistema de logging de forma centralizada"""
    
    # Crear logger raíz
    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    
    # Formato consistente
    formatter = logging.Formatter(
        '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Handler para consola (colores opcionales)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)
    
    # Handler para archivo (con rotación)
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler(
        'app.log', maxBytes=10*1024*1024, backupCount=5
    )
    file_handler.setFormatter(formatter)
    root_logger.addHandler(file_handler)