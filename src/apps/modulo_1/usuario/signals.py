from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Usuario

@receiver(post_save, sender=Usuario)
def crear_user(sender, instance, created, **kwargs):
    if created and not instance.user:
        user = User.objects.create_user(
            username=instance.persona.dni,
            email=instance.persona.correo,
            password=instance.contraseña,
        )
        instance.user = user
        instance.save()