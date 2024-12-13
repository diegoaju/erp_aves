# forms.py
from django import forms
from .models import Ave, Investidor, Cliente

class DateInput(forms.DateInput):
    input_type = 'date'

class AveForm(forms.ModelForm):
    class Meta:
        model = Ave
        fields = [
            'id_chip', 'nome', 'especie', 'mutacao_genetica', 'data_nascimento',
            'data_entrada', 'origem', 'parceiro_atual', 'id_chip_parceiro',
            'gaiola', 'sexo', 'mutacao', 'filhotes', 'investidor', 'preco_compra',
            'status', 'preco_venda', 'data_morte', 'motivo_morte'
        ]
        widgets = {
            'data_nascimento': DateInput(),
            'data_entrada': DateInput(),
            'data_morte': DateInput(),
        }

class InvestidorForm(forms.ModelForm):
    class Meta:
        model = Investidor
        fields = [
            'cpf', 'nome_completo', 'email', 'telefone', 'data_inicio_investimento',
            'filhotes', 'valor_investimento', 'aves', 'comissao', 'custo_condominio', 'notas_adicionais'
        ]
        widgets = {
            'data_inicio_investimento': DateInput(),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'cpf', 'nome_completo', 'email', 'telefone', 'aves_compradas', 'data_compra',
            'motivo_compra', 'preco_compra', 'notas_adicionais'
        ]
        widgets = {
            'data_compra': DateInput(),
        }