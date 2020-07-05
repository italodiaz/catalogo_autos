from django.contrib import admin
from .models import TipoCarro, Marca, Modelo

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


admin.site.register(TipoCarro, TipoCarroAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(ModeloAdmin, ModeloAdmin)
