# main_window.py
import sys
from PySide6.QtWidgets import (QCheckBox, QMainWindow, QMenuBar, QMenu, QApplication, 
                               QMessageBox, QWidget, QVBoxLayout, QHBoxLayout,
                               QMdiArea, QMdiSubWindow, QPushButton, QLineEdit,
                               QLabel, QTableWidget, QTableWidgetItem, QHeaderView,
                               QFormLayout, QDialog, QGroupBox)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIcon
from models.category_model import Category
#from views.category_views.category_for_window import CategoryFormWindow
from views.category_views.category_for_window_dialog import CategoryFormWindow
from controllers.category_controller import CategoryController
import qtawesome as qta

class CategoriesWindow(QMdiSubWindow):  # ← Guardar referencia

    def __init__(self, mdi_area, parent=None):
        super().__init__(parent)
        self.__controller = CategoryController()
        self.__categories = []        
        self.mdi_area = mdi_area
        
        self.load_sample_data()
        self.setWindowTitle(self.tr("Administrador de Categorías"))
        
        central_widget = QWidget()
        self.setWidget(central_widget)
        
        main_layout = QVBoxLayout(central_widget)
        
        # Top panel
        top_panel = QWidget()
        top_layout = QHBoxLayout(top_panel)
                
        lbl_search = QLabel(self.tr("Categorías"))
        lbl_search.setProperty("class", "lbl-primary")  
        lbl_search.setText(self.tr("Buscar:"))
        top_layout.addWidget(lbl_search)
        top_layout.addSpacing(10) 
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText(self.tr("Buscar categoria por el nombre..."))
        self.search_input.textChanged.connect(self.search_categories)       
        top_layout.addWidget(self.search_input)
        # Establecer altura fija
        self.search_input.setFixedHeight(40)
        #ancho fijo para evitar que se expanda demasiado
        with_maximo = self.mdi_area.viewport().width()
        self.search_input.setFixedWidth(with_maximo-290)
        # Agregar espacio entre el campo de búsqueda y el botón
        top_layout.addSpacing(10)        
        #icono
        icon_add = qta.icon('ei.address-book-alt', color='white')
        #carga
        self.btn_new = QPushButton(self.tr("Nueva categoria"))
        self.btn_new.setIcon(icon_add)
        self.btn_new.setProperty("class", "btn-primary")
        self.btn_new.clicked.connect(self.open_new_category_form)
        top_layout.addWidget(self.btn_new)
        
        top_layout.addStretch()
        main_layout.addWidget(top_panel)
        
        # Table
        self.table = QTableWidget()
        self.table.verticalHeader().setVisible(False)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Nombre", "Activo", "Descripción", "Acciones"])
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents) # type: ignore
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)# type: ignore
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)# type: ignore
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)# type: ignore
        self.table.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)# type: ignore
        
        main_layout.addWidget(self.table)
        
        self.load_table_data()
        self.resize(800, 500)
    
    def load_sample_data(self):        
        self.__categories =  self.__controller.read()      

    def load_table_data(self, search_text=""):
        filtered_categories = self.__categories
        if search_text:
            filtered_categories = [c for c in self.__categories 
                                  if search_text.lower() in c.name.lower()]
        
        self.table.setRowCount(len(filtered_categories))
        
        for row, category in enumerate(filtered_categories):
            self.table.setItem(row, 0, QTableWidgetItem(str(category.id)))
            self.table.setItem(row, 1, QTableWidgetItem(category.name))
            self.table.setItem(row, 2, QTableWidgetItem("Yes" if category.activate else "No"))
            self.table.setItem(row, 3, QTableWidgetItem(category.description))
            
            actions_widget = QWidget()
            actions_layout = QHBoxLayout(actions_widget)
            actions_layout.setContentsMargins(5, 2, 5, 2)
            
            btn_update = QPushButton(self.tr("✏️ Actualizar"))
            btn_update.setProperty("class", "btn-update")
            btn_update.clicked.connect(lambda checked, c=category: self.open_edit_category_form(c))
            
            btn_delete = QPushButton(self.tr("🗑️ Eliminar"))    
            btn_delete.setProperty("class", "btn-delete")
            btn_delete.clicked.connect(lambda checked, c=category: self.delete_category(c))
            
            actions_layout.addWidget(btn_update)
            actions_layout.addWidget(btn_delete)
            actions_layout.addStretch()
            
            self.table.setCellWidget(row, 4, actions_widget)

    def load_table_and_data(self):
        self.load_sample_data()  # Recargar categorías desde el controlador para obtener el ID asignado
        self.load_table_data()
    

    def search_categories(self, text):
        self.load_table_data(text)
    
    def open_new_category_form(self):
        form_window = CategoryFormWindow(parent=self, on_save_callback=self.add_category)
        if form_window.exec():
            print(self.tr("La categoría se guardó correctamente."))           
        else:           
            print(self.tr("El usuario canceló la operación."))
            
    
    def open_edit_category_form(self, category):
        # mdi_area = self.parent()
        # if self.mdi_area:
        #     form_window = CategoryFormWindow(mdi_area, 
        #                                      category, 
        #                                      on_save_callback=self.update_category)
        #     self.mdi_area.addSubWindow(form_window)
        #     form_window.show()
        form_window = CategoryFormWindow(
            parent=self, 
            Category_obj=category,  # Pasamos el objeto a editar
            on_save_callback=self.update_category
        )
        if form_window.exec():
            print(self.tr("Categoría actualizada correctamente en la base de datos."))            
        else:
            print(self.tr("Edición cancelada."))

    
    def add_category(self, category):        
        self.__controller.create(category)  # Llamar al controlador para manejar la lógica de adición            
        self.load_table_and_data()
        QMessageBox.information(self, self.tr("Success"), self.tr(f"Category '{category.name}' added successfully"))
   
    def update_category(self, updated_category):
        self.__controller.update(updated_category)  # Llamar al controlador para manejar la lógica de actualización
        self.load_table_and_data()
        QMessageBox.information(self, self.tr("Success"), self.tr(f"Category '{updated_category.name}' updated successfully"))
    
    def delete_category(self, category):
        reply = QMessageBox.question(self, self.tr("Confirmar Borrado"),
                                     self.tr(f"Esta seguro que desea borrar la categoria '{category.name}'?"),
                                     QMessageBox.Yes | QMessageBox.No) # type: ignore
        if reply == QMessageBox.Yes: # type: ignore
            self.__controller.delete(category.id)  # Llamar al controlador para manejar la lógica de borrado  
            self.__categories = self.__controller.read()  # Actualizar la lista de categorías desde el controlador
            #self.__categories = [c for c in self.__categories if c.id != category.id]
            self.load_table_data(self.search_input.text())
            QMessageBox.information(self, self.tr("Success"), self.tr(f"Category '{category.name}' deleted successfully"))

    def closeEvent(self, event):
        """Handle close event to properly clean up"""
        # Optional: Save data before closing
        reply = QMessageBox.question(self, self.tr("Close Window"),
                                     self.tr("Do you want to close this window?"),
                                     QMessageBox.Yes | QMessageBox.No,# type: ignore
                                     QMessageBox.No)# type: ignore
        if reply == QMessageBox.Yes:# type: ignore
            event.accept()
        else:
            event.ignore()