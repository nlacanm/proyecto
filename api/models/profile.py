from django.db import models
from django.contrib.auth.models import User
from .rol import Rol

class Profile(models.Model):
#mantener solo los campos necesarios 
   

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name="profile_rol") 
    avatar = models.ImageField(upload_to='Avatar', null=True, blank=True)    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    direccion = models.CharField(max_length=250, null=True, blank=True)
    
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.user.username

    def delete(self, *args):
        user = self.user
        user.is_active = False
        user.save()
        self.active = False
        self.save()
        return True
