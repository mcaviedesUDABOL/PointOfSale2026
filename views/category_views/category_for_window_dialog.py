from PySide6.QtWidgets import (QDialog, QLabel, QVBoxLayout, QFormLayout, QLineEdit, 
                             QCheckBox, QPushButton, QHBoxLayout, QMessageBox, QWidget)
from models.category_model import Category

class CategoryFormWindow(QDialog): # <-- Cambiado de QMdiSubWindow a QDialog
    def __init__(self, parent=None, Category_obj=None, on_save_callback=None):
        super().__init__(parent)
        
        # Guardamos la referencia del objeto categoría (renombrado para evitar conflicto con la clase)
        self.category_data = Category_obj 
        self.on_save_callback = on_save_callback
        
        
        # Configuración de ventana modal
        self.setWindowTitle(self.tr("Nueva Categoria") if not Category_obj else self.tr("Editar Categoria"))
        self.setModal(True)
        self.resize(400, 200) # Ajustado a un tamaño más común de diálogo
        
        # Layout principal directamente al diálogo
        main_layout = QVBoxLayout(self)
        
        # --- Formulario ---
        form_layout = QFormLayout()
        
        self.id_input = QLineEdit()
        self.id_input.setReadOnly(True)
        self.id_input.setPlaceholderText("Auto-generado")
        
        self.name_input = QLineEdit()
        self.activate_input = QCheckBox(self.tr("Activa"))
        self.activate_input.setChecked(True)
        self.description_input = QLineEdit()
        
        # Cargar datos si es edición
        if Category_obj:
            self.id_input.setText(str(Category_obj.id))
            self.name_input.setText(Category_obj.name)
            self.activate_input.setChecked(Category_obj.activate)
            self.description_input.setText(Category_obj.description)
        
        lbl_id = QLabel("ID")
        lbl_id.setProperty("class", "lbl-primary")  
        lbl_id.setText(self.tr("ID:"))
        lbl_id.setFixedWidth(100)
        lbl_name = QLabel("Name")
        lbl_name.setProperty("class", "lbl-primary")  
        lbl_name.setText(self.tr("Nombre:"))
        lbl_name.setFixedWidth(100)
        lbl_activate = QLabel("State")
        lbl_activate.setProperty("class", "lbl-primary")  
        lbl_activate.setText(self.tr("Estado:"))
        lbl_activate.setFixedWidth(100)
        lbl_description = QLabel("Description")
        lbl_description.setProperty("class", "lbl-primary")  
        lbl_description.setText(self.tr("Descripción:"))
        lbl_description.setFixedWidth(100)


        form_layout.addRow(lbl_id, self.id_input)
        form_layout.addRow(lbl_name, self.name_input)
        form_layout.addRow(lbl_activate, self.activate_input)
        form_layout.addRow(lbl_description, self.description_input)
        
        main_layout.addLayout(form_layout)
        
        # --- Botones ---
        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch()
        
        self.btn_save = QPushButton(self.tr("Guardar"))
        self.btn_save.setProperty("class", "btn-secondary") # Si usas el CSS anterior
        self.btn_save.clicked.connect(self.save_category)
        
        self.btn_cancel = QPushButton(self.tr("Cancelar"))
        self.btn_cancel.setProperty("class", "btn-delete") #
        # En QDialog, reject() cierra la ventana y devuelve QDialog.Rejected
        self.btn_cancel.clicked.connect(self.reject) 
        
        buttons_layout.addWidget(self.btn_save)
        buttons_layout.addWidget(self.btn_cancel)
        
        main_layout.addLayout(buttons_layout)

    def save_category(self):
        name = self.name_input.text().strip()
        description = self.description_input.text().strip()
        
        if not name:
            QMessageBox.warning(self, self.tr("Advertencia"), self.tr("El nombre de la categoría es obligatorio"))
            return
        
        # Nota: Aquí asumo que 'Category' es tu clase de Modelo (SQLAlchemy o similar)
        # Si no la tienes importada, asegúrate de tenerla disponible
        if not self.category_data:           
            category = Category(id=-1, name=name, activate=self.activate_input.isChecked(), description=description)
        else:
            # Actualizar instancia existente
            self.category_data.name = name            
            self.category_data.activate = self.activate_input.isChecked()
            self.category_data.description = description
            category = self.category_data
        
        # Ejecutar el callback si existe
        if self.on_save_callback:
            self.on_save_callback(category)
        
        # Cerrar el diálogo devolviendo QDialog.Accepted
        self.accept()