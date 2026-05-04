from datetime import date
from interfaces.auditable import Auditable


class AuditController:

    @staticmethod
    def register_creation(entity: Auditable, id_user: int):
        entity.register_creation(id_user)
        print(f"Registro auditado: Creación registrada el {entity.create_date} por usuario {id_user}")
    
    @staticmethod
    def register_update(entity: Auditable, id_user: int):
        entity.register_update(id_user)
        print(f"Registro auditado: Actualización registrada el {entity.update_date} por usuario {id_user}")

    @staticmethod
    def mark_as_deleted(entity: Auditable, id_user: int):
        if not entity._is_deleted:
            entity.mark_as_deleted(id_user)
            print(f"Registro auditado: Borrado lógico aplicado el {entity.delete_date} por usuario {id_user}")
        else:
            print("El registro ya estaba marcado como eliminado.")
            