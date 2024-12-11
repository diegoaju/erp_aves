from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial do app "aves"
    path('listar/', views.listar_aves, name='listar_aves'),  # Lista de aves
    path('cadastrar/', views.cadastrar_ave, name='cadastrar_ave'), # Cadastro de aves
    ]

