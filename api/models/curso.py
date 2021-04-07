from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=255)
    
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    

    def __unicode__(self):
        return self.nombre

    def delete(self, *args):
        self.active = False
        self.save()
        return True