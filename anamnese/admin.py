from django.contrib import admin
from .models import *

@admin.register(Cadastro)
class CadastroAdmin (admin.ModelAdmin):
     list_display=('nome_usuario','email','CPF',)

@admin.register(Ficha)
class FichaAdmin (admin.ModelAdmin):
     list_display=('nome',)



