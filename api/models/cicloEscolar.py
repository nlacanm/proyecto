from django.db import models

class CicloEscolar(models.Model):
    anio = models.PositiveIntegerField()

    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    

    def __unicode__(self):
        return self.anio

    def delete(self, *args):
        self.active = False
        self.save()
        return True