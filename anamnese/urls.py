from django.urls import path
from . import views

app_name = 'anamnese'

urlpatterns = [
    path('', views.index_usuario, name='index_usuario'),
    path('ficha/', views.fficha, name="ficha"),
    path('dados/', views.dadospessoais, name="dadospessoais"),
    path('doenças/', views.historicodoenças, name="historicodoenças"),
    path('familiar/', views.historicofamiliar, name="historicofamiliar"),
    path('sintomas/', views.sintomas, name="sintomas"),
    
    path('excluir/', views.excluir_cadastro, name="excluir_cadastro"),
    path('atualizar/', views.atualizar_cadastro, name='atualizar_cadastro'),


    path('atualizar_triglierideos/', views.atualizar_triglicerideos, name='atualizar_triglicerideos'),
]