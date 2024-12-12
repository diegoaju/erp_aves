# forms.py
from django import forms
from .models import Ave, Investidor

class DateInput(forms.DateInput):
    input_type = 'date'

class AveForm(forms.ModelForm):
    class Meta:
        model = Ave
        fields = [
            'id_chip', 'nome', 'especie', 'mutacao_genetica', 'data_nascimento',
            'data_entrada', 'origem', 'parceiro_atual', 'id_chip_parceiro',
            'gaiola', 'sexo', 'mutacao', 'filhotes', 'investidor'
        ]
        widgets = {
            'data_nascimento': DateInput(),
            'data_entrada': DateInput(),
        }

class InvestidorForm(forms.ModelForm):
    class Meta:
        model = Investidor
        fields = ['nome', 'email', 'telefone', 'aves', 'custo_mensal', 'desconto_percentual']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }