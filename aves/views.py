from django.shortcuts import render, redirect, get_object_or_404
from .models import Ave, Investidor
from .forms import AveForm, InvestidorForm
from django.contrib import messages

# Página inicial
def index(request):
    return render(request, 'aves/index.html')

# Lista de aves
def listar_aves(request):
    aves = Ave.objects.all()
    return render(request, 'aves/listar_aves.html', {'aves': aves})

# Cadastro de aves
def cadastrar_ave(request):
    if request.method == 'POST':
        form = AveForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ave cadastrada com sucesso!')
            return redirect('listar_aves')
        else:
            messages.error(request, 'Erro ao cadastrar ave. Verifique os dados e tente novamente.')
    else:
        form = AveForm()
    return render(request, 'aves/cadastrar_ave.html', {'form': form})

# Edição de aves
def editar_ave(request, id):
    ave = get_object_or_404(Ave, id=id)
    if request.method == 'POST':
        form = AveForm(request.POST, instance=ave)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ave atualizada com sucesso!')
            return redirect('listar_aves')
        else:
            messages.error(request, 'Erro ao atualizar ave. Verifique os dados e tente novamente.')
    else:
        form = AveForm(instance=ave)
    return render(request, 'aves/cadastrar_ave.html', {'form': form})

# Deleção de aves
def deletar_ave(request, id):
    ave = get_object_or_404(Ave, id=id)
    if request.method == 'POST':
        ave.delete()
        messages.success(request, 'Ave deletada com sucesso!')
        return redirect('listar_aves')
    return render(request, 'aves/deletar_ave.html', {'ave': ave})

# Página em construção
def em_construcao(request):
    return render(request, 'aves/em_construcao.html')

# Lista de investidores
def listar_investidores(request):
    investidores = Investidor.objects.all()
    return render(request, 'aves/listar_investidores.html', {'investidores': investidores})

# Cadastro de investidores
def cadastrar_investidor(request):
    if request.method == 'POST':
        form = InvestidorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Investidor cadastrado com sucesso!')
            return redirect('listar_investidores')
        else:
            messages.error(request, 'Erro ao cadastrar investidor. Verifique os dados e tente novamente.')
    else:
        form = InvestidorForm()
    return render(request, 'aves/cadastrar_investidor.html', {'form': form})
