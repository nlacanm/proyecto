from django.db import models
from .cicloEscolar import CicloEscolar

class Evento(models.Model):
    cicloEscolar = models.ForeignKey(CicloEscolar, on_delete=models.CASCADE, related_name="evento_cicloEscolar")
    titulo = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=255)
    fecha = models.DateField()
    hora = models.TimeField()
    
    activo = models.BooleanField(default=True)    
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    

    def __unicode__(self):
        return self.titulo

    def delete(self, *args):
        self.active = False
        self.save()
        return True