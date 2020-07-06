from django.forms import ModelForm, TextInput, Select, NumberInput
from catalogo.models import Modelo, Marca, TipoCarro, Carro


class ModeloForm(ModelForm):
    class Meta:
        model = Modelo
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre'
        }
        widgets = {
            'nombre': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el modelo',
                    'id': 'nombre'
                }
            )
        }

class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre'
        }
        widgets = {
            'nombre': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la marca',
                    'id': 'nombre'
                }
            )
        }

class TipoCarroForm(ModelForm):
    class Meta:
        model = TipoCarro
        fields = ['nombre']
        labels = {
            'nombre': 'Tipo'
        }
        widgets = {
            'nombre': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el tipo de carro',
                    'id': 'nombre'
                }
            )
        }

class CarroForm(ModelForm):
    class Meta:
        model = Carro
        fields = ['marca','modelo','tipo_carro','año','tipo_combustible','peso','precio']
        widgets = {
            'marca': Select(
                attrs={
                    'class': 'form-control',
                    'id': 'marca'
                }
            ),
            'modelo': Select(
                attrs={
                    'class': 'form-control',
                    'id': 'modelo'
                }
            ),
            'tipo_carro': Select(
                attrs={
                    'class': 'form-control',
                    'id': 'tipo_carro'
                }
            ),
            'año': NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'año',
                    'min':'1950',
                    'max':'2050'
                }
            ),
            'tipo_combustible': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el tipo de combustible',
                    'id': 'tipo_combustible'
                }
            ),
            'peso': NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'peso'
                }
            ),
            'precio': NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'precio'
                }
            )
        }