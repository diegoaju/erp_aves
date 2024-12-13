# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listar/', views.listar_aves, name='listar_aves'),
    path('cadastrar/', views.cadastrar_ave, name='cadastrar_ave'),
    path('investidores/', views.listar_investidores, name='listar_investidores'),
    path('investidores/cadastrar/', views.cadastrar_investidor, name='cadastrar_investidor'),
    path('investidores/editar/<int:id>/', views.editar_investidor, name='editar_investidor'),
    path('investidores/deletar/<int:id>/', views.deletar_investidor, name='deletar_investidor'),
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('clientes/cadastrar/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('clientes/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/deletar/<int:id>/', views.deletar_cliente, name='deletar_cliente'),
    path('fornecedores/', views.em_construcao, name='fornecedores'),
    path('criadores/', views.em_construcao, name='criadores'),
    path('editar/<int:id>/', views.editar_ave, name='editar_ave'),
    path('deletar/<int:id>/', views.deletar_ave, name='deletar_ave'),
]

