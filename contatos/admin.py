from django.contrib import admin
from django.contrib.admin.helpers import checkbox
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome',
                    'telefone', 'email', 'data_da_criação', 'categoria', 'mostrar')
    list_display_links = ('id', 'nome', 'sobrenome')
    list_editable = ('telefone', 'mostrar')
    search_fields = ('nome', 'sobrenome', 'descrição', 'telefone')
    list_per_page = 10


# Register your models here.
admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
