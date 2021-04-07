from django.db import models
from .tarea import Tarea
from .estudiante import Estudiante

class TareaEstudiante (models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name="tareaEstudiante_tarea")
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name="tareaEstudiante_estudiante")    
    fechaEntrega = models.DateField()#dudad
    archivo = models.FileField(upload_to='DocumentoT', null=True, blank=True)#duda    
    texto = models.CharField(max_length=255)
    calificacion = models.FloatField(max_length=5)#duda    
    
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    

    def __unicode__(self):
        return self.tarea.tarea

    def delete(self, *args):
        self.active = False
        self.save()
        return True