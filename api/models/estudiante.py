from django.db import models
from .profile import Profile
from .grado import Grado

class Estudiante(models.Model):
    profile = models.OneToOneField(Profile,on_delete=models.CASCADE, related_name="estudiante_profile")
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE, related_name="estudiante_grado")
    carnet = models.CharField(max_length=25)
    direcion = models.CharField(max_length=25, null=True, blank=True)
    telefonoContacto = models.CharField(max_length=15, null=True, blank=True)#agregar
    direccionContacto = models.CharField(max_length=45, null=True, blank=True)

    def __unicode__(self):
        return self.profile.nombre        

    def delete(self, *args):
        self.active = False
        self.save()
        return True