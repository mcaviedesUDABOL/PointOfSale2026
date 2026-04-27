import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QMdiArea, 
                             QMdiSubWindow, QTableWidget, QTableWidgetItem, 
                             QVBoxLayout, QWidget, QPushButton, QHBoxLayout,
                             QMessageBox, QDialog, QLabel, QLineEdit, QFormLayout)
from PySide6.QtCore import Qt

# --- Ventana de Formulario (Usada para Nuevo y Editar) ---
class DialogoProducto(QDialog):
    def __init__(self, titulo, datos_producto=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle(titulo)
        self.setMinimumWidth(300)
        
        layout_principal = QVBoxLayout(self)
        formulario = QFormLayout()
        
        # Si datos_producto es None, es un producto nuevo
        self.input_id = QLineEdit(datos_producto['id'] if datos_producto else "")
        self.input_nombre = QLineEdit(datos_producto['nombre'] if datos_producto else "")
        self.input_precio = QLineEdit(datos_producto['precio'] if datos_producto else "")
        
        if datos_producto:
            self.input_id.setReadOnly(True) # No editar ID en edición
        
        formulario.addRow("ID:", self.input_id)
        formulario.addRow("Nombre:", self.input_nombre)
        formulario.addRow("Precio:", self.input_precio)
        
        layout_botones = QHBoxLayout()
        self.btn_guardar = QPushButton("Guardar")
        self.btn_cancelar = QPushButton("Cancelar")
        
        self.btn_guardar.clicked.connect(self.accept)
        self.btn_cancelar.clicked.connect(self.reject)
        
        layout_botones.addWidget(self.btn_guardar)
        layout_botones.addWidget(self.btn_cancelar)
        
        layout_principal.addLayout(formulario)
        layout_principal.addLayout(layout_botones)

    def obtener_datos(self):
        return {
            "id": self.input_id.text(),
            "nombre": self.input_nombre.text(),
            "precio": self.input_precio.text()
        }

# --- Ventana MDI de Lista de Productos ---
class VentanaProductos(QMdiSubWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Productos")
        self.resize(700, 500)
        
        container = QWidget()
        self.setWidget(container)
        layout_principal = QVBoxLayout(container)
        
        # --- Cabecera: Botón Nuevo y Buscador ---
        layout_cabecera = QHBoxLayout()
        
        self.btn_nuevo = QPushButton("Nuevo Producto")
        self.btn_nuevo.setStyleSheet("background-color: #2ecc71; color: white; font-weight: bold;")
        self.btn_nuevo.clicked.connect(self.accion_nuevo)
        
        self.buscador = QLineEdit()
        self.buscador.setPlaceholderText("🔍 Buscar producto por nombre...")
        self.buscador.textChanged.connect(self.filtrar_productos) # Evento al escribir
        
        layout_cabecera.addWidget(self.btn_nuevo)
        layout_cabecera.addSpacing(20) # Espacio entre botón y buscador
        layout_cabecera.addWidget(QLabel("Buscar:"))
        layout_cabecera.addWidget(self.buscador)
        
        layout_principal.addLayout(layout_cabecera)
        
        # --- Datos de ejemplo iniciales ---
        self.productos = [
            {"id": "1", "nombre": "Laptop Gamer", "precio": "1500"},
            {"id": "2", "nombre": "Teclado Mecánico", "precio": "80"},
            {"id": "3", "nombre": "Monitor 4K", "precio": "400"}
        ]
        
        # --- Tabla ---
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(4)
        self.tabla.setHorizontalHeaderLabels(["ID", "Nombre", "Precio", "Acciones"])
        self.tabla.setColumnWidth(3, 220)
        
        layout_principal.addWidget(self.tabla)
        self.cargar_datos()

    def cargar_datos(self):
        self.tabla.setRowCount(len(self.productos))
        for i, prod in enumerate(self.productos):
            self.tabla.setItem(i, 0, QTableWidgetItem(prod["id"]))
            self.tabla.setItem(i, 1, QTableWidgetItem(prod["nombre"]))
            self.tabla.setItem(i, 2, QTableWidgetItem(prod["precio"]))
            
            botones_widget = QWidget()
            botones_layout = QHBoxLayout(botones_widget)
            botones_layout.setContentsMargins(5, 2, 5, 2)
            
            btn_actualizar = QPushButton("Actualizar")
            btn_eliminar = QPushButton("Eliminar")
            
            btn_actualizar.clicked.connect(lambda ch, r=i: self.accion_actualizar(r))
            btn_eliminar.clicked.connect(lambda ch, r=i: self.accion_eliminar(r))
            
            botones_layout.addWidget(btn_actualizar)
            botones_layout.addWidget(btn_eliminar)
            self.tabla.setCellWidget(i, 3, botones_widget)

    def filtrar_productos(self):
        texto = self.buscador.text().lower()
        for i in range(self.tabla.rowCount()):
            item_nombre = self.tabla.item(i, 1)
            if item_nombre:
                # Si el nombre contiene el texto del buscador, mostrar fila, si no, ocultar
                ocultar = texto not in item_nombre.text().lower()
                self.tabla.setRowHidden(i, ocultar)

    def accion_nuevo(self):
        dialogo = DialogoProducto("Registrar Nuevo Producto", parent=self)
        if dialogo.exec():
            nuevo_prod = dialogo.obtener_datos()
            self.productos.append(nuevo_prod)
            self.cargar_datos()
            self.status_message("Producto guardado con éxito")

    def accion_actualizar(self, fila):
        datos_actuales = {
            "id": self.tabla.item(fila, 0).text(),
            "nombre": self.tabla.item(fila, 1).text(),
            "precio": self.tabla.item(fila, 2).text()
        }
        
        dialogo = DialogoProducto("Editar Producto", datos_actuales, self)
        if dialogo.exec():
            nuevos_datos = dialogo.obtener_datos()
            # Actualizar en la lista interna
            self.productos[fila] = nuevos_datos
            self.cargar_datos()
            self.status_message("Producto actualizado")

    def accion_eliminar(self, fila):
        nombre = self.tabla.item(fila, 1).text()
        respuesta = QMessageBox.question(
            self, "Confirmar", f"¿Eliminar {nombre}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if respuesta == QMessageBox.StandardButton.Yes:
            self.productos.pop(fila)
            self.cargar_datos()

    def status_message(self, msj):
        # Si la ventana principal tiene status bar, podríamos enviar mensajes ahí
        print(msj)

# --- Ejecución ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = QMainWindow()
    mdi = QMdiArea()
    main_win.setCentralWidget(mdi)
    
    ventana_prod = VentanaProductos()
    mdi.addSubWindow(ventana_prod)
    ventana_prod.show()
    
    main_win.show()
    sys.exit(app.exec())