# main_window.py
import sys
from PySide6.QtWidgets import (QMainWindow, QMdiArea, QMenuBar, QMenu, QApplication, 
                               QMessageBox, QWidget, QVBoxLayout, QLabel)
from PySide6.QtCore import Qt
from data.connection.database_manager import DatabaseManager
from views.category_views.main_category_view import CategoriesWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema de Gestión Empresarial")
        self.setGeometry(100, 100, 1200, 800)
        
        # Configurar los botones de minimizar, maximizar y cerrar (por defecto ya vienen)
        self.setWindowFlags(Qt.Window)
        
        # Crear widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Store reference to categories window
        self.categories_window = None
        
        # Layout para el contenido (puedes agregar más cosas después)
        layout = QVBoxLayout(central_widget)
        label = QLabel("Bienvenido al Sistema de Gestión Empresarial")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 20px; font-weight: bold; margin: 50px;")
        layout.addWidget(label)
        
        # Crear la barra de menú
        self.create_menu_bar()

        # Widget central: MDI Area para manejar ventanas internas
        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area)
    
    def create_menu_bar(self):
        menubar = self.menuBar()
        
        # ========== MENÚ ARCHIVO ==========
        file_menu = menubar.addMenu("Archivo")
        
        # Item Salir
        exit_action = file_menu.addAction("Salir")
        exit_action.triggered.connect(self.close_app)
        
        # ========== MENÚ VENTAS ==========
        sales_menu = menubar.addMenu("Ventas")
        
        # Items del menú Ventas
        new_sale = sales_menu.addAction("Nueva Venta")
        new_sale.triggered.connect(lambda: self.show_info("Nueva Venta"))
        
        ticket_management = sales_menu.addAction("Gestión de Tickets")
        ticket_management.triggered.connect(lambda: self.show_info("Gestión de Tickets"))
        
        refunds = sales_menu.addAction("devoluciones y Cambios")
        refunds.triggered.connect(lambda: self.show_info("devoluciones y Cambios"))
        
        quotes = sales_menu.addAction("Cotizaciones")
        quotes.triggered.connect(lambda: self.show_info("Cotizaciones"))
        
        layaway_plans = sales_menu.addAction("Apartados")
        layaway_plans.triggered.connect(lambda: self.show_info("Apartados"))
        
        # ========== MENÚ INVENTARIO ==========
        Inventory_menu = menubar.addMenu("Inventario")
        
        category_item_menu = Inventory_menu.addAction("Categorías")
        #category_item_menu.triggered.connect(lambda: self.show_info("Categorías"))
        category_item_menu.triggered.connect(self.open_categories_window)
        
        catalog_item_menu = Inventory_menu.addAction("Catálogo de Productos")
        catalog_item_menu.triggered.connect(lambda: self.show_info("Catálogo de Productos"))
        
        control_stock = Inventory_menu.addAction("Control de Stock")
        control_stock.triggered.connect(lambda: self.show_info("Control de Stock"))
        
        transfers_item_menu = Inventory_menu.addAction("Transferencias")
        transfers_item_menu.triggered.connect(lambda: self.show_info("Transferencias"))
        
        suppliers_item_menu = Inventory_menu.addAction("Proveedores")
        suppliers_item_menu.triggered.connect(lambda: self.show_info("Proveedores"))
        
        goods_receipt_item_menu = Inventory_menu.addAction("Entrada de Mercancía")
        goods_receipt_item_menu.triggered.connect(lambda: self.show_info("Entrada de Mercancía"))
        
        # ========== MENÚ CAJA Y FINANZAS ==========
        cash_register_item_menu = menubar.addMenu("Caja y Finanzas")
        
        opening_closing_item_menu = cash_register_item_menu.addAction("Apertura y Cierre de Caja")
        opening_closing_item_menu.triggered.connect(lambda: self.show_info("Apertura y Cierre de Caja"))
        
        cash_item_menu = cash_register_item_menu.addAction("Entradas/Salidas de Efectivo")
        cash_item_menu.triggered.connect(lambda: self.show_info("Entradas/Salidas de Efectivo"))
        
        accounts_receivable_item_menu = cash_register_item_menu.addAction("Cuentas por Cobrar")
        accounts_receivable_item_menu.triggered.connect(lambda: self.show_info("Cuentas por Cobrar"))
        
        invoicing_item_menu = cash_register_item_menu.addAction("Facturación Electrónica")
        invoicing_item_menu.triggered.connect(lambda: self.show_info("Facturación Electrónica"))
        
        # ========== MENÚ CLIENTES Y MARKETING ==========
        customers_menu = menubar.addMenu("Clientes y Marketing")
        
        customers_database_item_menu = customers_menu.addAction("Base de Datos de Clientes")
        customers_database_item_menu.triggered.connect(lambda: self.show_info("Base de Datos de Clientes"))
        
        loyalty_item_menu = customers_menu.addAction("Programas de Lealtad")
        loyalty_item_menu.triggered.connect(lambda: self.show_info("Programas de Lealtad"))
        
        promotions_item_menu = customers_menu.addAction("Promociones y Descuentos")
        promotions_item_menu.triggered.connect(lambda: self.show_info("Promociones y Descuentos"))
        
        # ========== MENÚ REPORTES ==========
        reports_menu = menubar.addMenu("Reportes")
        
        sales_reports_item_menu = reports_menu.addAction("Reporte de Ventas")
        sales_reports_item_menu.triggered.connect(lambda: self.show_info("Reporte de Ventas"))
        
        best_sellers_item_menu = reports_menu.addAction("Productos Más Vendidos")
        best_sellers_item_menu.triggered.connect(lambda: self.show_info("Productos Más Vendidos"))
        
        cash_register_closing_item_menu = reports_menu.addAction("Corte de Caja")
        cash_register_closing_item_menu.triggered.connect(lambda: self.show_info("Corte de Caja"))
        
        profit_item_menu = reports_menu.addAction("Utilidades")
        profit_item_menu.triggered.connect(lambda: self.show_info("Utilidades"))
        
        # ========== MENÚ CONFIGURACIÓN ==========
        config_menu = menubar.addMenu("Configuración")
        
        users_item_menu = config_menu.addAction("Usuarios y Permisos")
        users_item_menu.triggered.connect(lambda: self.show_info("Usuarios y Permisos"))
        
        devices_item_menu = config_menu.addAction("Dispositivos")
        devices_item_menu.triggered.connect(lambda: self.show_info("Dispositivos"))
        
        companydata_item_menu = config_menu.addAction("Datos de la Empresa")
        companydata_item_menu.triggered.connect(lambda: self.show_info("Datos de la Empresa"))
    
    def show_info(self, action_name):
        """Muestra un mensaje temporal para las acciones (demo)"""
        QMessageBox.information(self, "Información", f"Has seleccionado: {action_name}\n\nFuncionalidad en desarrollo.")
    
    def close_app(self):
        """Cierra la aplicación"""
        reply = QMessageBox.question(self, 'Confirmar Salida', 
                                     '¿Estás seguro de que deseas salir?',
                                     QMessageBox.Yes | QMessageBox.No, 
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
    
    def closeEvent(self, event):
        """Sobrescribe el evento de cierre para confirmar"""
        reply = QMessageBox.question(self, 'Confirmar Salida', 
                                     '¿Estás seguro de que deseas salir?',
                                     QMessageBox.Yes | QMessageBox.No, 
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    
    def open_categories_window(self):
        """Method that opens the categories window - FIXED VERSION"""
        # Check if categories window exists and is visible
        if self.categories_window is not None:
            # Check if window is still valid
            try:
                if self.categories_window in self.mdi_area.subWindowList():
                    # Window exists, activate it
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
        self.categories_window.setAttribute(Qt.WA_DeleteOnClose)
        
        # Connect the destroyed signal to clean up the reference
        self.categories_window.destroyed.connect(self.on_categories_window_destroyed)
        
        self.mdi_area.addSubWindow(self.categories_window)
        self.categories_window.showMaximized()
    
    def on_categories_window_destroyed(self):
        """Clean up reference when categories window is destroyed"""
        self.categories_window = None