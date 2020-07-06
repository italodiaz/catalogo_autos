from django.contrib import admin
from catalogo.models import Marca, TipoCarro, Modelo, Carro

# Register your models here.

class TipoCarroAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']

class MarcaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']

class ModeloAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']

class CarroAdmin(admin.ModelAdmin):
    pass


admin.site.register(TipoCarro, TipoCarroAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Modelo, ModeloAdmin)
admin.site.register(Carro, CarroAdmin)
