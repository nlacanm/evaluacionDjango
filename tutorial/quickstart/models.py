from django.db import models

# Create your models here.

class cliente(models.Model):
    nombre = models.CharField(max_length=40, blank=True)  
    apellido = models.CharField(max_length=40, blank=True) 
    nit = models.CharField(max_length=10, blank=True)
    
    def  __str__(self):
        return self.nombre

class factura(models.Model):
    nombreFactura  = models.CharField(max_length=60, blank=True)
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)            
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    total = models.IntegerField(null=True, blank=True)
    def  __str__(self):
        return self.total

