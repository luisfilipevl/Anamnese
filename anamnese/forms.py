from django import forms 
from .models import *

class CadastroForm (forms.ModelForm):
    class Meta: 
        model = Cadastro
        fields = '__all__'

        widgets = {
            'nome_usuario': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'senha': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
    

class FichaForm(forms.ModelForm):
    class Meta:
        model = Ficha
        fields = '__all__'
        
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'sexo': forms.TextInput(attrs={'class': 'form-control'}),
            'profissao': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_civil': forms.TextInput(attrs={'class': 'form-control'}),
            'doencas_familiares': forms.Textarea(attrs={'class': 'form-control'}),
            'doencas_pessoais': forms.Textarea(attrs={'class': 'form-control'}),
            'doencas_atual': forms.Textarea(attrs={'class': 'form-control'}),
            'remedios': forms.Textarea(attrs={'class': 'form-control'}),
            'fuma': forms.TextInput(attrs={'class': 'form-check-input'}),
            'consumo_alcool': forms.TextInput(attrs={'class': 'form-check-input'}),
            'tempo_medio_sono': forms.NumberInput(attrs={'class': 'form-control'}),

            'nivel_glicemia': forms.NumberInput(attrs={'class': 'form-control'}),
            'nivel_colesterol': forms.NumberInput(attrs={'class': 'form-control'}),
            'nivel_plasmaticos_colesterol': forms.NumberInput(attrs={'class': 'form-control'}),
            'nivel_triglicerideos': forms.NumberInput(attrs={'class': 'form-control'}),
            'nivel_lipoproteinas_plasmaticos': forms.NumberInput(attrs={'class': 'form-control'}),
            'nivel_pressao_arterial': forms.NumberInput(attrs={'class': 'form-control'}),
        }