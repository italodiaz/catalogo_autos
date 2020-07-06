from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    Home, ListModelo, CreateModelo, UpdateModelo, DeleteModelo,
    ListMarca, CreateMarca, UpdateMarca, DeleteMarca,
    ListTipoCarro, CreateTipoCarro, UpdateTipoCarro, DeleteTipoCarro
)

urlpatterns = [
    path('', login_required(Home.as_view()), name='index'),
    path('modelo/list', login_required(ListModelo.as_view()), name='list.modelo'),
    path('modelo/create', login_required(CreateModelo.as_view()), name='create.modelo'),
    path('modelo/update/<int:pk>', login_required(UpdateModelo.as_view()), name='update.modelo'),
    path('modelo/delete/<int:pk>', login_required(DeleteModelo.as_view()), name='delete.modelo'),
    path('marca/list', login_required(ListMarca.as_view()), name='list.marca'),
    path('marca/create', login_required(CreateMarca.as_view()), name='create.marca'),
    path('marca/update/<int:pk>', login_required(UpdateMarca.as_view()), name='update.marca'),
    path('marca/delete/<int:pk>', login_required(DeleteMarca.as_view()), name='delete.marca'),
    path('tipo_carro/list', login_required(ListTipoCarro.as_view()), name='list.tipo_carro'),
    path('tipo_carro/create', login_required(CreateTipoCarro.as_view()), name='create.tipo_carro'),
    path('tipo_carro/update/<int:pk>', login_required(UpdateTipoCarro.as_view()), name='update.tipo_carro'),
    path('tipo_carro/delete/<int:pk>', login_required(DeleteTipoCarro.as_view()), name='delete.tipo_carro')
]