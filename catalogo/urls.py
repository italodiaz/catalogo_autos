from django.urls import path, include
from rest_framework import routers
from .views import MarcaView, ModeloView, TipoCarroView, CarroView

router = routers.DefaultRouter()
router.register('marca', MarcaView)
router.register('modelo', ModeloView, basename='modelo')
router.register('carro', CarroView, basename='carro')
router.register('tipo_carro', TipoCarroView)

urlpatterns = [
    path('', include(router.urls))
]