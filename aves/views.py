from django.shortcuts import render, redirect, get_object_or_404
from .models import Ave, Investidor, Cliente
from .forms import AveForm, InvestidorForm, ClienteForm
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

# Edição de investidores
def editar_investidor(request, id):
    investidor = get_object_or_404(Investidor, id=id)
    if request.method == 'POST':
        form = InvestidorForm(request.POST, instance=investidor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Investidor atualizado com sucesso!')
            return redirect('listar_investidores')
        else:
            messages.error(request, 'Erro ao atualizar investidor. Verifique os dados e tente novamente.')
    else:
        form = InvestidorForm(instance=investidor)
    return render(request, 'aves/cadastrar_investidor.html', {'form': form})

# Deleção de investidores
def deletar_investidor(request, id):
    investidor = get_object_or_404(Investidor, id=id)
    if request.method == 'POST':
        investidor.delete()
        messages.success(request, 'Investidor deletado com sucesso!')
        return redirect('listar_investidores')
    return render(request, 'aves/deletar_investidor.html', {'investidor': investidor})

# Lista de clientes
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'aves/listar_clientes.html', {'clientes': clientes})

# Cadastro de clientes
def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('listar_clientes')
        else:
            messages.error(request, 'Erro ao cadastrar cliente. Verifique os dados e tente novamente.')
    else:
        form = ClienteForm()
    return render(request, 'aves/cadastrar_cliente.html', {'form': form})

# Edição de clientes
def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente atualizado com sucesso!')
            return redirect('listar_clientes')
        else:
            messages.error(request, 'Erro ao atualizar cliente. Verifique os dados e tente novamente.')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'aves/cadastrar_cliente.html', {'form': form})

# Deleção de clientes
def deletar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente deletado com sucesso!')
        return redirect('listar_clientes')
    return render(request, 'aves/deletar_cliente.html', {'cliente': cliente})
