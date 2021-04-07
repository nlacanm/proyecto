from django.db import models
from .asignacion import Asignacion

class MaterialDeClase(models.Model):
    asignacion = models.ForeignKey(Asignacion, on_delete=models.CASCADE, related_name="materialDeClase_asignacion")
    titulo = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=255)
    archivo = models.FileField(null=True, blank=True)#duda    
    
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
         

    def __unicode__(self):
        return self.titulo

    def delete(self, *args):
        self.active = False
        self.save()
        return True
