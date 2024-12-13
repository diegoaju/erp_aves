from django.shortcuts import render, redirect, get_object_or_404
from .models import Ave, Investidor, Cliente, Perfil
from .forms import AveForm, InvestidorForm, ClienteForm, UserForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Página inicial
@login_required
def index(request):
    return render(request, 'aves/index.html')

# Lista de aves
@login_required
def listar_aves(request):
    aves = Ave.objects.all()
    return render(request, 'aves/listar_aves.html', {'aves': aves})

# Cadastro de aves
@login_required
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
@login_required
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
@login_required
def deletar_ave(request, id):
    ave = get_object_or_404(Ave, id=id)
    if request.method == 'POST':
        ave.delete()
        messages.success(request, 'Ave deletada com sucesso!')
        return redirect('listar_aves')
    return render(request, 'aves/deletar_ave.html', {'ave': ave})

# Página em construção
@login_required
def em_construcao(request):
    return render(request, 'aves/em_construcao.html')

# Lista de investidores
@login_required
def listar_investidores(request):
    investidores = Investidor.objects.all()
    return render(request, 'aves/listar_investidores.html', {'investidores': investidores})

# Cadastro de investidores
@login_required
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
@login_required
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
@login_required
def deletar_investidor(request, id):
    investidor = get_object_or_404(Investidor, id=id)
    if request.method == 'POST':
        investidor.delete()
        messages.success(request, 'Investidor deletado com sucesso!')
        return redirect('listar_investidores')
    return render(request, 'aves/deletar_investidor.html', {'investidor': investidor})

# Lista de clientes
@login_required
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'aves/listar_clientes.html', {'clientes': clientes})

# Cadastro de clientes
@login_required
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
@login_required
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
@login_required
def deletar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente deletado com sucesso!')
        return redirect('listar_clientes')
    return render(request, 'aves/deletar_cliente.html', {'cliente': cliente})

# View de registro
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada para {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Lista de usuários (apenas para administradores)
@login_required
def listar_usuarios(request):
    if not request.user.is_superuser:
        return redirect('index')
    
    usuarios = User.objects.all()
    return render(request, 'registration/listar_usuarios.html', {'usuarios': usuarios})

# Cadastro de novos usuários (apenas para administradores)
@login_required
def cadastrar_usuario(request):
    if not request.user.is_superuser:
        return redirect('index')
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            perfil = Perfil(user=user, perfil=form.cleaned_data['perfil'])
            perfil.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('listar_usuarios')
        else:
            messages.error(request, 'Erro ao cadastrar usuário. Verifique os dados e tente novamente.')
    else:
        form = UserForm()
    return render(request, 'registration/cadastrar_usuario.html', {'form': form})

# Edição de usuários (apenas para administradores)
@login_required
def editar_usuario(request, id):
    if not request.user.is_superuser:
        return redirect('index')
    
    usuario = get_object_or_404(User, id=id)
    perfil = get_object_or_404(Perfil, user=usuario)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=usuario)
        if form.is_valid():
            user = form.save(commit=False)
            if 'password' in form.cleaned_data:
                user.set_password(form.cleaned_data['password'])
            user.save()
            perfil.perfil = form.cleaned_data['perfil']
            perfil.save()
            messages.success(request, 'Usuário atualizado com sucesso!')
            return redirect('listar_usuarios')
        else:
            messages.error(request, 'Erro ao atualizar usuário. Verifique os dados e tente novamente.')
    else:
        form = UserForm(instance=usuario, initial={'perfil': perfil.perfil})
    return render(request, 'registration/editar_usuario.html', {'form': form})

# Deleção de usuários (apenas para administradores)
@login_required
def deletar_usuario(request, id):
    if not request.user.is_superuser:
        return redirect('index')
    
    usuario = get_object_or_404(User, id=id)
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuário deletado com sucesso!')
        return redirect('listar_usuarios')
    return render(request, 'registration/deletar_usuario.html', {'usuario': usuario})
