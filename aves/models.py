from django.db import models

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

    def __str__(self):
        return f"{self.nome} ({self.id_chip})"

class Investidor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    aves = models.ManyToManyField(Ave, related_name='investidores')
    custo_mensal = models.DecimalField(max_digits=10, decimal_places=2)
    desconto_percentual = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome