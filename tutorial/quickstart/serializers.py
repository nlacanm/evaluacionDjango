from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import cliente, factura

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email','password']


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = ['url', 'nombre', 'apellido','nit']


class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = factura
        fields = ['url', 'nombreFactura', 'cliente', 'precio','cantidad', 'total']

