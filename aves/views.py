from django.shortcuts import render, redirect
from .models import Ave

# Página inicial
def index(request):
    return render(request, 'aves/index.html')

# Lista de aves
def listar_aves(request):
    aves = Ave.objects.all() # Busca todas as aves no banco de dados
    return render(request, 'aves/listar_aves.html', {'aves': aves}) # Renderiza o template

# Cadastro de aves
def cadastrar_ave(request):
    if request.method == 'POST':
        # Captura os dados do formulário e salva no banco
        Ave.objects.create(
            id_chip=request.POST['id_chip'],
            nome=request.POST['nome'],
            especie=request.POST['especie'],
            mutacao_genetica=request.POST['mutacao_genetica'],
            data_nascimento=request.POST['data_nascimento'],
            data_entrada=request.POST['data_entrada'],
            origem=request.POST['origem'],
            parceiro_atual=request.POST['parceiro_atual'],
            id_chip_parceiro=request.POST['id_chip_parceiro'],
            gaiola=request.POST['gaiola'],
            sexo=request.POST['sexo'],
            mutacao=request.POST['mutacao'],
            filhotes=request.POST['filhotes'],
            investidores=request.POST['investidores'],
        )
        # Redireciona para a listagem após salvar
        return redirect('listar_aves') # Redireciona para a lista de aves
    # Renderiza o formulário se for um GET
    return render(request, 'aves/cadastrar_ave.html')

# Create your views here.
