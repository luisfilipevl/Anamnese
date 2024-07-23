from django.urls import path
from .import views

urlpatterns = [
    path('',views.index),
    path('dados',views.dadospessoais),
    path('doenças',views.historicodoenças),
    path('familiar',views.historicofamiliar),
    path('sintomas',views.sintomas),
    path('ficha',views.fficha),
    path('exames',views.examess),
    path('cadastro',views.cadastross),


    path('inserir_cadastro',views.in_cadastro,name='inserir_cadastro'),
    
]
