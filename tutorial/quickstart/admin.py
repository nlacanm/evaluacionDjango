from django.contrib import admin

# Register your models here.
from .models import cliente, factura

admin.site.register(cliente)
admin.site.register(factura)