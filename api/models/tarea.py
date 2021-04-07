from django.db import models
from .asignacion import Asignacion


class Tarea(models.Model):
    asignacion = models.ForeignKey(Asignacion, on_delete=models.CASCADE, related_name="tarea_asignacion")
    tarea = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    archivo = models.FileField(upload_to='Documento',null=True, blank=True)#duda    
    fechaEntrega = models.DateField()
    horaEntrega = models.TimeField()
    nota = models.FloatField(max_length=5)
    
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    

    def __unicode__(self):
        return self.tarea

    def delete(self, *args):
        self.active = False
        self.save()
        return True