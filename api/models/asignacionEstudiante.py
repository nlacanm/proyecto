from django.db import models
from .asignacion import Asignacion
from .estudiante import Estudiante

class AsignacionEstudiante(models.Model):
    asignacion = models.ForeignKey(Asignacion, on_delete=models.CASCADE, related_name="asignacionEstudiante_asignacion")
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name="asignacionEstudiante_estudiante")

    def __unicode__(self):
        return self.asignacion.cicloEscolar.anio
    
    
    