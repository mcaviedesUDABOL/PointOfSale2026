# main_window.py
import sys
from PySide6.QtWidgets import (QMainWindow, QMdiArea, QMenuBar, QMenu, QApplication, 
                               QMessageBox, QWidget, QVBoxLayout, QLabel)
from PySide6.QtCore import QTimer, Qt
from data.connection.database_manager import DatabaseManager
from views.category_views.main_category_view import CategoriesWindow
from views.login_dialog import LoginDialog
from utils.session import Session    

class MainWindow(QMainWindow):

    _menubar: QMenuBar
    _mdi_area: QMdiArea
    _file_menu: QMenu
    _sales_menu: QMenu
    _inventory_menu: QMenu
    _cash_register_item_menu: QMenu
    _customers_menu: QMenu
    _reports_menu: QMenu
    _config_menu: QMenu

    def __init__(self):
        super().__init__()
        #sesion
        self.session = Session()
        # self.setWindowTitle("Punto de venta - Sistema de Gestión Empresarial")
        self.setWindowTitle(self.tr("Punto de venta - Sistema de Gestión Empresarial"))
        self.setGeometry(100, 100, 1200, 800)
        self.showMaximized()  # Maximiza pero mantiene barra de tareas
        
        # Configurar los botones de minimizar, maximizar y cerrar (por defecto ya vienen)
        self.setWindowFlags(Qt.Window)# type: ignore
        
        # Crear widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Store reference to categories window
        self.categories_window = None
        
        # Layout para el contenido (puedes agregar más cosas después)
        layout = QVBoxLayout(central_widget)
        label = QLabel(self.tr("Bienvenido al Sistema de Gestión Empresarial"))# type: ignore 
        label.setAlignment(Qt.AlignCenter)# type: ignore
        label.setStyleSheet("font-size: 20px; font-weight: bold; margin: 50px;")
        layout.addWidget(label)
        
        # Crear la barra de menú
        self.create_menu_bar()
        self.hide_menus()

        # Widget central: MDI Area para manejar ventanas internas
        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area)

        # Lanza el método después de que el __init__ termine
        QTimer.singleShot(0, self.check_credentials)


    def check_credentials(self) -> None:
        dialogo = LoginDialog(self)
        # Oculta los menús antes de mostrar el diálogo
        if not dialogo.exec():
            self.close()   
    
    def hide_menus(self) -> None:
        self._file_menu.menuAction().setVisible(True)
        self._sales_menu.menuAction().setVisible(False)
        self._inventory_menu.menuAction().setVisible(False)
        self._cash_register_item_menu.menuAction().setVisible(False)
        self._customers_menu.menuAction().setVisible(False)
        self._reports_menu.menuAction().setVisible(False)
        self._config_menu.menuAction().setVisible(False)


    def show_menus(self) -> None:
        self._file_menu.menuAction().setVisible(True)
        self._sales_menu.menuAction().setVisible(True)
        self._inventory_menu.menuAction().setVisible(True)
        self._cash_register_item_menu.menuAction().setVisible(True)
        self._customers_menu.menuAction().setVisible(True)
        self._reports_menu.menuAction().setVisible(True)
        self._config_menu.menuAction().setVisible(True)
        

    def create_menu_bar(self) -> None:
        self._menubar = self.menuBar()
        
        # ========== MENÚ ARCHIVO ==========
        self._file_menu = self._menubar.addMenu(self.tr("Archivo"))
        
        # Item Salir
        exit_action = self._file_menu.addAction(self.tr("Salir"))
        exit_action.triggered.connect(self.close_app)
        
        # ========== MENÚ VENTAS ==========
        self._sales_menu = self._menubar.addMenu(self.tr("Ventas"))
        
        # Items del menú Ventas
        new_sale = self._sales_menu.addAction(self.tr("Nueva Venta"))
        new_sale.triggered.connect(lambda: self.show_info(self.tr("Nueva Venta")))
        
        ticket_management = self._sales_menu.addAction(self.tr("Gestión de Tickets"))
        ticket_management.triggered.connect(lambda: self.show_info(self.tr("Gestión de Tickets")))
        
        refunds = self._sales_menu.addAction(self.tr("devoluciones y Cambios"))
        refunds.triggered.connect(lambda: self.show_info(self.tr("devoluciones y Cambios")))
        
        quotes = self._sales_menu.addAction(self.tr("Cotizaciones"))
        quotes.triggered.connect(lambda: self.show_info(self.tr("Cotizaciones")))
        
        layaway_plans = self._sales_menu.addAction(self.tr("Apartados"))
        layaway_plans.triggered.connect(lambda: self.show_info(self.tr("Apartados")))
        
        # ========== MENÚ INVENTARIO ==========
        self._inventory_menu = self._menubar.addMenu(self.tr("Inventario"))
        
        category_item_menu = self._inventory_menu.addAction(self.tr("Categorías"))        
        category_item_menu.triggered.connect(self.open_categories_window)
        
        catalog_item_menu = self._inventory_menu.addAction(self.tr("Catálogo de Productos"))
        catalog_item_menu.triggered.connect(lambda: self.show_info(self.tr("Catálogo de Productos")))
        
        control_stock = self._inventory_menu.addAction(self.tr("Control de Stock"))
        control_stock.triggered.connect(lambda: self.show_info(self.tr("Control de Stock")))
        
        transfers_item_menu = self._inventory_menu.addAction(self.tr("Transferencias"))
        transfers_item_menu.triggered.connect(lambda: self.show_info(self.tr("Transferencias")))
        
        suppliers_item_menu = self._inventory_menu.addAction(self.tr("Proveedores"))
        suppliers_item_menu.triggered.connect(lambda: self.show_info(self.tr("Proveedores")))
        
        goods_receipt_item_menu = self._inventory_menu.addAction(self.tr("Entrada de Mercancía"))
        goods_receipt_item_menu.triggered.connect(lambda: self.show_info(self.tr("Entrada de Mercancía")))
        
        # ========== MENÚ CAJA Y FINANZAS ==========
        self._cash_register_item_menu = self._menubar.addMenu(self.tr("Caja y Finanzas"))
        
        opening_closing_item_menu = self._cash_register_item_menu.addAction(self.tr("Apertura y Cierre de Caja"))
        opening_closing_item_menu.triggered.connect(lambda: self.show_info(self.tr("Apertura y Cierre de Caja")))
        
        cash_item_menu = self._cash_register_item_menu.addAction(self.tr("Entradas/Salidas de Efectivo"))
        cash_item_menu.triggered.connect(lambda: self.show_info(self.tr("Entradas/Salidas de Efectivo")))
        
        accounts_receivable_item_menu = self._cash_register_item_menu.addAction(self.tr("Cuentas por Cobrar"))
        accounts_receivable_item_menu.triggered.connect(lambda: self.show_info(self.tr("Cuentas por Cobrar")))
        
        invoicing_item_menu = self._cash_register_item_menu.addAction(self.tr("Facturación Electrónica"))
        invoicing_item_menu.triggered.connect(lambda: self.show_info(self.tr("Facturación Electrónica")))
        
        # ========== MENÚ CLIENTES Y MARKETING ==========
        self._customers_menu = self._menubar.addMenu(self.tr("Clientes y Marketing"))
        
        customers_database_item_menu = self._customers_menu.addAction(self.tr("Base de Datos de Clientes"))
        customers_database_item_menu.triggered.connect(lambda: self.show_info(self.tr("Base de Datos de Clientes")))
        
        loyalty_item_menu = self._customers_menu.addAction(self.tr("Programas de Lealtad"))
        loyalty_item_menu.triggered.connect(lambda: self.show_info(self.tr("Programas de Lealtad")))
        
        promotions_item_menu = self._customers_menu.addAction(self.tr("Promociones y Descuentos"))
        promotions_item_menu.triggered.connect(lambda: self.show_info(self.tr("Promociones y Descuentos")))
        
        # ========== MENÚ REPORTES ==========
        self._reports_menu = self._menubar.addMenu(self.tr("Reportes"))
        
        sales_reports_item_menu = self._reports_menu.addAction(self.tr("Reporte de Ventas"))
        sales_reports_item_menu.triggered.connect(lambda: self.show_info(self.tr("Reporte de Ventas")))
        
        best_sellers_item_menu = self._reports_menu.addAction( self.tr("Productos Más Vendidos"))
        best_sellers_item_menu.triggered.connect(lambda: self.show_info(self.tr("Productos Más Vendidos")))
        
        cash_register_closing_item_menu = self._reports_menu.addAction(self.tr("Corte de Caja"))
        cash_register_closing_item_menu.triggered.connect(lambda: self.show_info(self.tr("Corte de Caja")))
        
        profit_item_menu = self._reports_menu.addAction(self.tr("Utilidades"))
        profit_item_menu.triggered.connect(lambda: self.show_info(self.tr("Utilidades")))
        
        # ========== MENÚ CONFIGURACIÓN ==========
        self._config_menu = self._menubar.addMenu(self.tr("Configuración"))
        
        users_item_menu = self._config_menu.addAction(self.tr("Usuarios y Permisos"))
        users_item_menu.triggered.connect(lambda: self.show_info(self.tr("Usuarios y Permisos")))
        
        devices_item_menu = self._config_menu.addAction(self.tr("Dispositivos"))
        devices_item_menu.triggered.connect(lambda: self.show_info(self.tr("Dispositivos")))
        
        companydata_item_menu = self._config_menu.addAction(self.tr("Datos de la Empresa"))
        companydata_item_menu.triggered.connect(lambda: self.show_info(self.tr("Datos de la Empresa")))
    
    def show_info(self, action_name):
        """Muestra un mensaje temporal para las acciones (demo)"""
        QMessageBox.information(self, self.tr("Información"), f"Has seleccionado: {action_name}\n\nFuncionalidad en desarrollo.")
    
    def close_app(self):
        """Cierra la aplicación"""
        reply = QMessageBox.question(self, self.tr('Confirmar Salida'), 
                                     self.tr('¿Estás seguro de que deseas salir?'),
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)# type: ignore
        if reply == QMessageBox.Yes:# type: ignore
            self.close()
    
    def closeEvent(self, event):
        """Sobrescribe el evento de cierre para confirmar"""
        reply = QMessageBox.question(self, self.tr('Confirmar Salida'), 
                                     self.tr('¿Estás seguro de que deseas salir?'),
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)# type: ignore
        if reply == QMessageBox.Yes:# type: ignore
            event.accept()
        else:
            event.ignore()
    
    def open_categories_window(self):
        """Method that opens the categories window - FIXED VERSION"""       
        if self.categories_window is not None:           
            try:
                if self.categories_window in self.mdi_area.subWindowList():                    
                    self.mdi_area.setActiveSubWindow(self.categories_window)
                    self.categories_window.showMaximized()
                    return
                else:
                    # Window was closed, set reference to None
                    self.categories_window = None
            except RuntimeError:
                # Window has been deleted
                self.categories_window = None
        
        # Create new categories window
        self.categories_window = CategoriesWindow(self.mdi_area)
        self.categories_window.setAttribute(Qt.WA_DeleteOnClose)# type: ignore
        
        # Connect the destroyed signal to clean up the reference
        self.categories_window.destroyed.connect(self.on_categories_window_destroyed)
        
        self.mdi_area.addSubWindow(self.categories_window)
        self.categories_window.showMaximized()
    
    def on_categories_window_destroyed(self):
        """Clean up reference when categories window is destroyed"""
        self.categories_window = None