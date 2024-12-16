from django import forms 
from .models import *
from django.contrib.auth.models import User

class CadastroForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        label="Usuário",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        required=True,
        label="E-mail",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Cadastro
        fields = ['nome_usuario', 'CPF', 'senha']  # Campos do modelo Cadastro
        widgets = {
            'nome_usuario': forms.TextInput(attrs={'class': 'form-control'}),
            'senha': forms.PasswordInput(attrs={'class': 'form-control'}),
            'CPF': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        # Recebe a instância do User (opcional)
        user_instance = kwargs.pop('user_instance', None)
        super().__init__(*args, **kwargs)
        
        # Inicializa os campos do usuário se a instância estiver disponível
        if user_instance:
            self.fields['username'].initial = user_instance.username
            self.fields['email'].initial = user_instance.email
    

class FichaForm(forms.ModelForm):
    class Meta:
        model = Ficha
        fields = '__all__'
        
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'sexo': forms.TextInput(attrs={'class': 'form-control'}),
            'profissao': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_civil': forms.TextInput(attrs={'class': 'form-control'}),
            'doencas_familiares': forms.Textarea(attrs={'class': 'form-control'}),
            'doencas_pessoais': forms.Textarea(attrs={'class': 'form-control'}),
            'doencas_atual': forms.Textarea(attrs={'class': 'form-control'}),
            'remedios': forms.Textarea(attrs={'class': 'form-control'}),
            'tempo_medio_sono': forms.NumberInput(attrs={'class': 'form-control'}),

            'nivel_glicemia': forms.NumberInput(attrs={'class': 'form-control'}),
            'nivel_colesterol': forms.NumberInput(attrs={'class': 'form-control'}),
            'nivel_plasmaticos_colesterol': forms.NumberInput(attrs={'class': 'form-control'}),
            'nivel_triglicerideos': forms.NumberInput(attrs={'class': 'form-control'}),
            'nivel_lipoproteinas_plasmaticos': forms.NumberInput(attrs={'class': 'form-control'}),
            'nivel_pressao_arterial': forms.NumberInput(attrs={'class': 'form-control'}),
        }