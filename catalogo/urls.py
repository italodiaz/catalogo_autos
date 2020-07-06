from django.urls import path, include
from rest_framework import routers
from .views import MarcaView, ModeloView, TipoCarroView, CarroView, CatalogoView

router = routers.DefaultRouter()
router.register('marca', MarcaView, basename='marca')
router.register('modelo', ModeloView, basename='modelo')
router.register('tipo_carro', TipoCarroView, basename='tipo_carro')
router.register('carro', CarroView, basename='carro')
router.register('catalogo_carros', CatalogoView, basename='catalogo_carros')

urlpatterns = [
    path('', include(router.urls))
]