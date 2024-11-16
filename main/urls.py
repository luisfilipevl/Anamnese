"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from anamnese import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('<int:cadastro_id>/', views.index_usuario, name='index_usuario'),
    
    path('cadastro', views.cadastross, name='cadastross'),
    path('login2',views.login2, name='login2'),
    path("logout/", views.logout_, name="logout"),

    
    path('<int:cadastro_id>/ficha/', views.fficha, name="ficha"),
    path('<int:cadastro_id>/dados/', views.dadospessoais, name="dadospessoais"),
    path('<int:cadastro_id>/doenças/', views.historicodoenças, name="historicodoenças"),
    path('<int:cadastro_id>/familiar/', views.historicofamiliar, name="historicofamiliar"),
    path('<int:cadastro_id>/sintomas/', views.sintomas, name="sintomas"),
    
    path('<int:cadastro_id>/excluir/', views.excluir_cadastro, name="excluir_cadastro"),
    path('<int:cadastro_id>/atualizar/', views.atualizar_cadastro, name='atualizar_cadastro'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)