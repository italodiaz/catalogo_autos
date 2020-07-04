from django.contrib import admin
from .models import Marca, TipoCarro, Modelo, Carro

# Register your models here.
admin.site.register(Marca)
admin.site.register(TipoCarro)
admin.site.register(Modelo)
admin.site.register(Carro)
