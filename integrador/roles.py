from rolepermissions.roles import AbstractUserRole

# comando python manage.py sync_roles


class Administrador(AbstractUserRole):
    available_permission = {}


class Usuario_comum(AbstractUserRole):
    available_permissions = {}
