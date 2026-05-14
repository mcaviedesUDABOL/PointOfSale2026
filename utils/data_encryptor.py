import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidTag

class DataEncryptor:
    """
    Clase para encriptar y desencriptar datos usando AES-256-GCM.
    GCM provee autenticación (detecta si los datos fueron modificados).
    """
    
    def __init__(self, password: str, salt: bytes = None):
        """
        Inicializa el encriptador con una contraseña.
        
        Args:
            password: Contraseña para derivar la clave
            salt: Salt opcional (se genera uno nuevo si no se provee)
        """
        self.password = password.encode('utf-8')
        self.salt = salt if salt else os.urandom(16)
        self.backend = default_backend()
        
    def _derivar_clave(self) -> bytes:
        """Deriva una clave de 32 bytes (AES-256) usando PBKDF2."""
        kdf = PBKDF2(
            algorithm=hashes.SHA256(),
            length=32,  # AES-256
            salt=self.salt,
            iterations=100000,  # Suficiente para balancear seguridad/rendimiento
            backend=self.backend
        )
        return kdf.derive(self.password)
    
    def encrypt(self, data: bytes) -> str:
        """
        Encripta datos y retorna un string en formato Base64.
        
        Args:
            data: Datos en bytes a encriptar
            
        Returns:
            String Base64 con salt + nonce + tag + ciphertext
        """
        clave = self._derivar_clave()
        nonce = os.urandom(12)  # GCM recomienda 12 bytes
        
        # Crear cipher en modo GCM
        cipher = Cipher(
            algorithms.AES(clave),
            modes.GCM(nonce),
            backend=self.backend
        )
        encryptor = cipher.encryptor()
        
        # Encriptar
        ciphertext = encryptor.update(data) + encryptor.finalize()
        
        # Obtener tag de autenticación
        tag = encryptor.tag
        
        # Empaquetar: salt (16) + nonce (12) + tag (16) + ciphertext
        empaquetado = self.salt + nonce + tag + ciphertext
        
        return base64.b64encode(empaquetado).decode('utf-8')
    
    def decrypt(self, encrypted_data: str) -> bytes:
        """
        Desencripta datos desde un string Base64.
        
        Args:
            encrypted_data: String Base64 generado por encrypt()
            
        Returns:
            Datos originales en bytes
            
        Raises:
            ValueError: Si la autenticación falla (datos corruptos o contraseña incorrecta)
        """
        # Decodificar Base64
        empaquetado = base64.b64decode(encrypted_data)
        
        # Extraer componentes: salt (16), nonce (12), tag (16), resto es ciphertext
        salt = empaquetado[:16]
        nonce = empaquetado[16:28]
        tag = empaquetado[28:44]
        ciphertext = empaquetado[44:]
        
        # Actualizar salt y derivar clave nuevamente
        self.salt = salt
        clave = self._derivar_clave()
        
        # Crear cipher para desencriptar
        cipher = Cipher(
            algorithms.AES(clave),
            modes.GCM(nonce, tag),
            backend=self.backend
        )
        decryptor = cipher.decryptor()
        
        try:
            decrypted = decryptor.update(ciphertext) + decryptor.finalize()
            return decrypted
        except InvalidTag:
            raise ValueError("Autenticación fallida: datos corruptos o contraseña incorrecta")
