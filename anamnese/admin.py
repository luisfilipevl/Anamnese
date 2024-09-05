from django.contrib import admin
from .models import *

@admin.register(Cadastro)
class EuAdmin (admin.ModelAdmin):
     list_display=('nome_usuario','email','cpf',)


admin.site.register(DadoPessoal)
admin.site.register(ExameHemograma)
admin.site.register(Exame)
admin.site.register(Questionario)
admin.site.register(Ficha)
admin.site.register(Cadastro)
