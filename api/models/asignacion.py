from django.db import models

from .cicloEscolar import CicloEscolar
from .grado import Grado
from .seccion import Seccion
from .curso import Curso
from .profesor import Profesor


class Asignacion(models.Model):
    cicloEscolar = models.ForeignKey(CicloEscolar, on_delete=models.CASCADE,related_name="asignacion_cicloEscolar")    
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE, related_name="asignacion_grado")
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, related_name="asignacion_seccion")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="asignacion_curso")
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name="asignacion_profesor")
    imagen = models.ImageField(upload_to='ImgAsignacion', null=True, blank=True)#duda en frontend media_devel
    descripcion = models.CharField(max_length=255)

    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    

    def __unicode__(self):
        return self.cicloEscolar.anio

    def delete(self, *args):
        self.active = False
        self.save()
        return True