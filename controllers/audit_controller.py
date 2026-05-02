from datetime import date
from interfaces.auditable import Auditable


class AuditController:
    
    @staticmethod
    def eliminar_con_registro(entity: Auditable):
        """
        No importa si es un Producto o un Cliente, 
        si cumple el protocolo, se puede auditar.
        """
        if not entity.is_deleted:
            entity.mark_as_deleted()            
            print(f"Registro auditado: Borrado lógico aplicado el {entity.delete_date}")
        else:
            print("El registro ya estaba marcado como eliminado.")

    @staticmethod
    def registrar_cambio(entity: Auditable, id_editor: int):
        entity.id_user_update  = id_editor
        entity.update_date = date.today()
        print(f"Cambio registrado por usuario {id_editor}")