import sys
from PySide6.QtWidgets import (QApplication, QDialog, QVBoxLayout, QFormLayout, 
                             QLineEdit, QPushButton, QHBoxLayout, QMessageBox)
from PySide6.QtCore import Qt
from utils.session import Session
from controllers.user_controller import UserController
from controllers.rol_controller import RolController


class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        #sesion
        session1 = Session()

        self.setWindowTitle(self.tr("Inicio de Sesión"))
        self.setFixedSize(300, 150) # Tamaño fijo para que se vea como un diálogo real
        
        # Layout principal
        layout = QVBoxLayout(self)
        
        # --- Formulario ---
        form_layout = QFormLayout()
        
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Nombre de usuario")
        
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Contraseña")
        # Configurar para que no se vea la contraseña
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        
        form_layout.addRow(self.tr("Usuario:"), self.username_input)
        form_layout.addRow(self.tr("Password:"), self.password_input)
        
        layout.addLayout(form_layout)
        
        # --- Botones ---
        buttons_layout = QHBoxLayout()
        
        self.btn_accept = QPushButton(self.tr("Aceptar"))
        self.btn_accept.clicked.connect(self.handle_login)
        self.btn_accept.setDefault(True) # Hace que responda a la tecla 'Enter'
        
        self.btn_close = QPushButton(self.tr("Cerrar"))
        self.btn_close.clicked.connect(self.reject) # reject() cierra con código 0
        
        buttons_layout.addWidget(self.btn_accept)
        buttons_layout.addWidget(self.btn_close)
        
        layout.addLayout(buttons_layout)

    def handle_login(self):


        user = self.username_input.text().strip()
        password = self.password_input.text().strip()
        
        # Simulación de validación
        if user == "admin" and password == "1234":
            self.accept() # Cierra el diálogo devolviendo código 1 (Accepted)
        else:
            QMessageBox.critical(self, self.tr("Error"), self.tr("Usuario o contraseña incorrectos"))