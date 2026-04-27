import sys
from PySide6.QtWidgets import (QCheckBox, QMainWindow, QMenuBar, QMenu, QApplication, 
                               QMessageBox, QWidget, QVBoxLayout, QHBoxLayout,
                               QMdiArea, QMdiSubWindow, QPushButton, QLineEdit,
                               QLabel, QTableWidget, QTableWidgetItem, QHeaderView,
                               QFormLayout, QDialog, QGroupBox)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIcon
from models.category_model import Category


# Subwindow for creating/editing category
class CategoryFormWindow(QMdiSubWindow):
    def __init__(self, parent=None, Category=None, 
                 on_save_callback=None):
        super().__init__(parent)
        self.category = Category
        self.on_save_callback = on_save_callback
        self.setWindowTitle("New Category" if not Category else "Edit Category")
        
        central_widget = QWidget()
        self.setWidget(central_widget)
        
        layout = QVBoxLayout(central_widget)
        
        form_widget = QWidget()
        form_layout = QFormLayout(form_widget)
        
        
        self.id_input = QLineEdit()
        self.id_input.setReadOnly(True)
        self.name_input = QLineEdit()
        self.activate_input = QCheckBox()
        self.description_input = QLineEdit()
        
        if Category:
            self.id_input.setText(str(Category.id))
            self.name_input.setText(Category.name)
            self.activate_input.setChecked(Category.activate)
            self.description_input.setText(Category.description)
           
        
        form_layout.addRow("ID:", self.id_input)
        form_layout.addRow("Name:", self.name_input)
        form_layout.addRow("Activate:", self.activate_input)
        form_layout.addRow("Description:", self.description_input)
        
        layout.addWidget(form_widget)
        
        buttons_widget = QWidget()
        buttons_layout = QHBoxLayout(buttons_widget)
        buttons_layout.addStretch()
        
        self.btn_save = QPushButton("Save")
        self.btn_save.clicked.connect(self.save_category)
        self.btn_cancel = QPushButton("Cancel")
        self.btn_cancel.clicked.connect(self.close)
        
        buttons_layout.addWidget(self.btn_save)
        buttons_layout.addWidget(self.btn_cancel)
        
        layout.addWidget(buttons_widget)
        self.resize(600, 400)
    
    def save_category(self):
        name = self.name_input.text().strip()
        description = self.description_input.text().strip()
        
        if not name:
            QMessageBox.warning(self, "Warning", "Category name is required")
            return
        
        if not self.category:
            category = Category(id= 0,name=name, activate=True, description=description)
        else:
            self.category.id = int(self.id_input.text())
            self.category.name = name            
            self.category.activate = self.activate_input.isChecked()
            self.category.description = description
            category = self.category
        
        if self.on_save_callback:
            self.on_save_callback(category)
        
        self.close()
