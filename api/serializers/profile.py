from rest_framework import serializers
from api.models import Profile


class ProfileReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'user',
            'rol',
            'avatar',#duda
            'nombre',
            'apellido',
            'telefono',
            'direccion'
        )
