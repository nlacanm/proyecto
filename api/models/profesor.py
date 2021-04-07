from django.db import models
from .profile import Profile
from .profesion import Profesion

class Profesor (models.Model):
    profile = models.OneToOneField(Profile,on_delete=models.CASCADE, related_name="profesor_profile")
    profesion = models.ForeignKey(Profesion, on_delete=models.CASCADE, related_name="profesor_profesion") 

    def __unicode__(self):
        return self.profile.nombre