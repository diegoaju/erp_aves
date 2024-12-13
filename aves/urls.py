# urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('editar_usuario/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('deletar_usuario/<int:id>/', views.deletar_usuario, name='deletar_usuario'),
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),
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

