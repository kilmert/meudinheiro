from django.contrib import admin

# Register your models here.
from .models import Categoria


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'usuario']
    search_fields = ['Nome', 'usuario__username']
    list_filter = ['nome', 'usuario__username']


admin.site.register(Categoria, CategoriaAdmin)
