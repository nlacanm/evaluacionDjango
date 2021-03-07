from django.urls import include, path
from rest_framework import routers
from tutorial.quickstart import views

"""Creando intancia de router"""
router = routers.DefaultRouter()

"""Creando rutas"""
router.register(r'api/users', views.UserViewSet)
router.register(r'api/cliente', views.clienteViewSet)
router.register(r'api/factura', views.facturaViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
