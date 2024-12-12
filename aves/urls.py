# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listar/', views.listar_aves, name='listar_aves'),
    path('cadastrar/', views.cadastrar_ave, name='cadastrar_ave'),
    path('investidores/', views.em_construcao, name='investidores'),
    path('clientes/', views.em_construcao, name='clientes'),
    path('fornecedores/', views.em_construcao, name='fornecedores'),
    path('criadores/', views.em_construcao, name='criadores'),
    path('editar/<int:id>/', views.editar_ave, name='editar_ave'),
    path('deletar/<int:id>/', views.deletar_ave, name='deletar_ave'),
]

