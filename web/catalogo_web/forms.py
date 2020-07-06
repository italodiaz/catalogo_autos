from django.forms import ModelForm, TextInput, Textarea, FileInput
from catalogo.models import Modelo, Marca, TipoCarro


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
