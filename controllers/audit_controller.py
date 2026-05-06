from datetime import date, datetime
from interfaces.auditable import Auditable
from zoneinfo import ZoneInfo
from constants.timezone_enum import Timezone


class AuditController:

    @staticmethod
    def register_creation(entity: Auditable, id_user: int):
        entity.create_date = datetime.now(ZoneInfo(Timezone.AMERICA_LA_PAZ.value))
        entity.id_user_create = id_user
        #.register_creation(id_user)
        
    @staticmethod
    def register_update(entity: Auditable, id_user: int):
        #entity.register_update(id_user)
        entity.update_date = datetime.now(ZoneInfo(Timezone.AMERICA_LA_PAZ.value))
        entity.id_user_update = id_user
        #print(f"Registro auditado: Actualización registrada el {entity.update_date} por usuario {id_user}")

    @staticmethod
    def mark_as_deleted(entity: Auditable, id_user: int):
        #entity.mark_as_deleted(id_user)
        entity.delete_date = datetime.now(ZoneInfo(Timezone.AMERICA_LA_PAZ.value))
        entity.id_user_delete = id_user
        entity.is_deleted = True
            