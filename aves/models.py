from django.db import models
from django.contrib.auth.models import User

class Ave(models.Model):
    id_chip = models.CharField(max_length=100, unique=True)  # ID da Ave (Chip)
    nome = models.CharField(max_length=100, blank=True, null=True)  # Nome/Código da Ave
    especie = models.CharField(max_length=100)  # Espécie
    mutacao_genetica = models.CharField(max_length=100, blank=True, null=True)  # Mutação Genética
    data_nascimento = models.DateField(blank=True, null=True)  # Data de nascimento
    data_entrada = models.DateField(blank=True, null=True)  # Data de entrada no plantel
    origem = models.CharField(max_length=100, blank=True, null=True)  # Origem
    parceiro_atual = models.CharField(max_length=100, blank=True, null=True)  # Parceiro Atual
    id_chip_parceiro = models.CharField(max_length=100, blank=True, null=True)  # ID da Ave do Parceiro Atual
    gaiola = models.CharField(max_length=100, blank=True, null=True)  # Gaiola
    sexo = models.CharField(max_length=10, choices=[('Macho', 'Macho'), ('Fêmea', 'Fêmea')])  # Sexo
    mutacao = models.CharField(max_length=100, blank=True, null=True)  # Mutação
    filhotes = models.IntegerField(default=0)  # Filhotes
    investidor = models.CharField(max_length=255, blank=True, null=True)  # Investidores
    preco_compra = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Preço de Compra
    status = models.CharField(max_length=10, choices=[('Disponível', 'Disponível'), ('Vendida', 'Vendida'), ('Morte', 'Morte')], default='Disponível')  # Status
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Preço de Venda
    data_morte = models.DateField(blank=True, null=True)  # Data da Morte
    motivo_morte = models.TextField(blank=True, null=True)  # Motivo da Morte

    def __str__(self):
        return f"{self.nome} ({self.id_chip})"

class Investidor(models.Model):
    cpf = models.CharField(max_length=11, unique=True)  # CPF
    nome_completo = models.CharField(max_length=100)  # Nome Completo
    email = models.EmailField()  # E-mail
    telefone = models.CharField(max_length=15)  # Telefone
    data_inicio_investimento = models.DateField(blank=True, null=True)  # Data de Início do Investimento
    filhotes = models.IntegerField(default=0)  # Filhotes
    valor_investimento = models.DecimalField(max_digits=10, decimal_places=2)  # Valor do Investimento
    aves = models.ManyToManyField('Ave', related_name='investidores_set')  # Aves (Propriedade)
    comissao = models.DecimalField(max_digits=5, decimal_places=2)  # Comissão (%)
    custo_condominio = models.DecimalField(max_digits=10, decimal_places=2)  # Custo de Condomínio
    notas_adicionais = models.TextField(blank=True, null=True)  # Notas Adicionais

    def __str__(self):
        return self.nome_completo

class Cliente(models.Model):
    cpf = models.CharField(max_length=11, unique=True)  # CPF
    nome_completo = models.CharField(max_length=100)  # Nome Completo
    email = models.EmailField()  # E-mail
    telefone = models.CharField(max_length=15)  # Telefone
    aves_compradas = models.ManyToManyField('Ave', related_name='clientes_set')  # Aves Compradas
    data_compra = models.DateField(blank=True, null=True)  # Data da Compra
    motivo_compra = models.CharField(max_length=50, choices=[('Criador', 'Criador'), ('Coleção', 'Coleção'), ('Pet', 'Pet')])  # Motivo da Compra
    preco_compra = models.DecimalField(max_digits=10, decimal_places=2)  # Preço de Compra
    notas_adicionais = models.TextField(blank=True, null=True)  # Notas Adicionais

    def __str__(self):
        return self.nome_completo

class Perfil(models.Model):
    PERFIL_CHOICES = [
        ('consulta', 'Consulta'),
        ('cadastro_edicao', 'Cadastro e Edição'),
        ('admin', 'Admin'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    perfil = models.CharField(max_length=20, choices=PERFIL_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.get_perfil_display()}"
