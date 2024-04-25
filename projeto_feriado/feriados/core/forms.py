from django import forms
from django.core.exceptions import ValidationError


class FeriadoForm(forms.Form):
    nome = forms.CharField(max_length=50)
    dia = forms.IntegerField()
    mes = forms.IntegerField()
    
    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return nome.upper()

    def clean_dia(self):
        dia = self.cleaned_data['dia']
        if dia <=0 or dia>31:
            raise ValidationError('Dia Inválido')
        return dia

    def clean_mes(self):
        mes = self.cleaned_data['mes']
        if mes <=0 or mes>12:
            raise ValidationError('Mês Inválido')
        return mes