from enum import Enum, auto

class PermissionsEnum(Enum):
    READ = auto()
    WRITE = auto()
    DELETE = auto()
    UPDATE = auto()
    CREATE = auto()

    # Modulos Principales

    FILE_MENU = "file_menu.see"
    SALES_MENU= "sales_menu.see"
    INVENTORY_MENU= "inventory_menu.see"
    CASH_REGISTER_ITEM_MENU= "cash_register_item_menu.see"
    CUSTOMERS_MENU= "customers_menu.see"
    REPORTS_MENU= "reports_menu.see"
    CONFIG_MENU= "config_menu.see"


    
    # Acciones Específicas
    PRODUCTO_CREAR = "producto.crear"
    PRODUCTO_ELIMINAR = "producto.eliminar"
    VENTA_CANCELAR = "venta.cancelar"