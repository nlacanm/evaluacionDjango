from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from tutorial.quickstart.serializers import UserSerializer , ClienteSerializer, FacturaSerializer

""", cFacturaSerializer"""
from tutorial.quickstart.models import cliente, factura
""" GroupSerializer"""
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import models

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]   


class clienteViewSet(viewsets.ModelViewSet):
    queryset = cliente.objects.all().order_by('-nombre')
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]


class facturaViewSet(viewsets.ModelViewSet):    
    queryset = factura.objects.all()
    serializer_class = FacturaSerializer
    permission_classes = [permissions.IsAuthenticated]
   
    def create(self, request):
        data=request.data
        factura.objects.create(    
            nombreFactura = data.get('nombreFactura'),                        
            cliente = data.get('cliente'),
            precio = data.get('precio'),
            cantidad = data.get('cantidad'),            
            total = precio * cantidad                        
        )
        serializer = FacturaSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_CREATED_201)
    
    
