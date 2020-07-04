from rest_framework import viewsets, filters
from .serializers import MarcaSerializer, ModeloSerializer, TipoCarroSerializer, CarroSerializer
from .models import Marca, Modelo, TipoCarro, Carro

# Create your views here.
class MarcaView(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class TipoCarroView(viewsets.ModelViewSet):
    queryset = TipoCarro.objects.all()
    serializer_class = TipoCarroSerializer

class ModeloView(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer

class CarroView(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    filter_backends = (filters.SearchFilter, 
                        filters.OrderingFilter)
    search_fields = ('precio')
    ordering_fields = ('precio',)
