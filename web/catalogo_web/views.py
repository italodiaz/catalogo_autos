from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from catalogo.models import Modelo, Marca, TipoCarro
from .forms import ModeloForm, MarcaForm, TipoCarroForm
from django.urls import reverse_lazy

# Create your views here.
class Home(TemplateView):
    template_name = 'catalogo_web/index.html'

class ListModelo(ListView):
    model = Modelo
    template_name = 'catalogo_web/modelo/list_modelo.html'
    queryset = Modelo.objects.all()
    context_object_name = 'modelos'

class CreateModelo(CreateView):
    model = Modelo
    form_class = ModeloForm
    template_name = 'catalogo_web/modelo/create_modelo.html'
    success_url = reverse_lazy('catalogo_web:list.modelo')

class UpdateModelo(UpdateView):
    model = Modelo
    form_class = ModeloForm
    template_name = 'catalogo_web/modelo/update_modelo.html'
    success_url = reverse_lazy('catalogo_web:list.modelo')

class DeleteModelo(DeleteView):
    model = Modelo
    form_class = ModeloForm
    template_name = 'catalogo_web/modelo/delete_modelo.html'
    success_url = reverse_lazy('catalogo_web:list.modelo')
    
    def get_context_data(self, **kwargs):
        modelo = Modelo.objects.get(id=self.kwargs.get('pk'))
        context = super(DeleteModelo, self).get_context_data(**kwargs)
        context['modelo'] = modelo
        return context


class ListMarca(ListView):
    model = Marca
    template_name = 'catalogo_web/marca/list_marca.html'
    queryset = Marca.objects.all()
    context_object_name = 'marcas'

class CreateMarca(CreateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'catalogo_web/marca/create_marca.html'
    success_url = reverse_lazy('catalogo_web:list.marca')

class UpdateMarca(UpdateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'catalogo_web/marca/update_marca.html'
    success_url = reverse_lazy('catalogo_web:list.marca')

class DeleteMarca(DeleteView):
    model = Marca
    form_class = MarcaForm
    template_name = 'catalogo_web/marca/delete_marca.html'
    success_url = reverse_lazy('catalogo_web:list.marca')
    
    def get_context_data(self, **kwargs):
        marca = Marca.objects.get(id=self.kwargs.get('pk'))
        context = super(DeleteMarca, self).get_context_data(**kwargs)
        context['marca'] = marca
        return context

class ListTipoCarro(ListView):
    model = TipoCarro
    template_name = 'catalogo_web/tipo_carro/list_tipo_carro.html'
    queryset = TipoCarro.objects.all()
    context_object_name = 'tipo_carros'

class CreateTipoCarro(CreateView):
    model = TipoCarro
    form_class = TipoCarroForm
    template_name = 'catalogo_web/tipo_carro/create_tipo_carro.html'
    success_url = reverse_lazy('catalogo_web:list.tipo_carro')

class UpdateTipoCarro(UpdateView):
    model = TipoCarro
    form_class = TipoCarroForm
    template_name = 'catalogo_web/tipo_carro/update_tipo_carro.html'
    success_url = reverse_lazy('catalogo_web:list.tipo_carro')

class DeleteTipoCarro(DeleteView):
    model = TipoCarro
    form_class = TipoCarroForm
    template_name = 'catalogo_web/tipo_carro/delete_tipo_carro.html'
    success_url = reverse_lazy('catalogo_web:list.tipo_carro')
    
    def get_context_data(self, **kwargs):
        tipo_carro = TipoCarro.objects.get(id=self.kwargs.get('pk'))
        context = super(DeleteTipoCarro, self).get_context_data(**kwargs)
        context['tipo_carro'] = tipo_carro
        return context
