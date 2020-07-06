from rest_framework import serializers
from .models import Marca, Modelo, TipoCarro, Carro

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class TipoCarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCarro
        fields = '__all__'

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = '__all__'

class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Carro

class CatalogoSerializer(serializers.ModelSerializer):
    marca = MarcaSerializer(many=False)
    tipo_carro = TipoCarroSerializer(many=False)
    modelo = ModeloSerializer(many=False)
    class Meta:
        fields = '__all__'
        model = Carro
