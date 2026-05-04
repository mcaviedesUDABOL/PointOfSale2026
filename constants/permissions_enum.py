from enum import Enum, auto

class PermissionsEnum(Enum):
    READ = auto()
    WRITE = auto()
    DELETE = auto()
    UPDATE = auto()
    CREATE = auto()

    # Modulos Principales
    MODULO_VENTAS = "ventas.ver"
    MODULO_INVENTARIO = "inventario.ver"
    MODULO_REPORTES = "reportes.ver"
    MODULO_USUARIOS = "usuarios.ver"
    
    # Acciones Específicas
    PRODUCTO_CREAR = "producto.crear"
    PRODUCTO_ELIMINAR = "producto.eliminar"
    VENTA_CANCELAR = "venta.cancelar"