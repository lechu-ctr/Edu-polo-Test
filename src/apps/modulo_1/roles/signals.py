from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver
from django.db import models

@receiver(post_migrate)
def crear_roles_y_permisos(sender, **kwargs):
    #Preparado, falta tener el resto de tablas funcionales para agregar los permisos
    roles = {
        "Administrador": [
            "add_user", "change_user", "delete_user", "view_user", "add_persona", "change_persona", "delete_persona", "view_persona",
        ],
        "Coordinador": [
            "view_user", "change_user", "view_persona"
        ],
        "MesaEntrada": [
            "add_persona", "view_persona"
        ],
        "Docente": [
            "view_estudiante", "change_estudiante"
        ],
        "Estudiante": [
            "view_curso"
        ],
        "PuntoMedio": [
            "view_user"
        ]
    }

    for nombre_rol, codename_list in roles.items():
        grupo, _ = Group.objects.get_or_create(name=nombre_rol)
        for codename in codename_list:
            try:
                permiso = Permission.objects.get(codename=codename)
                grupo.permissions.add(permiso)
            except Permission.DoesNotExist:
                print(f"No existe el permiso {codename}.")

    def save(self, *args, **kwargs):
        if not self.group:
            grupo, _ = Group.objects.get_or_create(name=self.nombre)
            self.group = grupo
        super().save(*args, **kwargs)