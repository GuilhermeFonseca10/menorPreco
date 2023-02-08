from rolepermissions.roles import AbstractUserRole


class Admin(AbstractUserRole):
    available_permissions = {"ver_dashboard": True}


class user_normal(AbstractUserRole):
    available_permissions = {"ver_home": True, "ver_supermercado": True}


# https://www.youtube.com/watch?v=XVYyPHoH64s
