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
    
    class Metatest: 
        model = Ficha
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            
        }


