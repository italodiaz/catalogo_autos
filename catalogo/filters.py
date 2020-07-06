import django_filters
from .models import Carro

class CarroFilter(django_filters.FilterSet):
    precio__gt = django_filters.NumberFilter(field_name='precio', lookup_expr='gte')
    precio__lt = django_filters.NumberFilter(field_name='precio', lookup_expr='lte')

    class Meta:
        model = Carro
        fields = ['marca', 'modelo', 'tipo_carro', 'año']
