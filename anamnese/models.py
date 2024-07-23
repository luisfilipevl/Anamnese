from django.db import models

class Dado_pessoal(models.Model):
    nome = models.CharField(max_length=100, blank=True)
    endereço = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    data_nascimento = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True)
    profissão = models.CharField(max_length=100, blank=True)
    estado_civil = models.CharField(max_length=100, blank=True)

class Exame_hemograma(models.Model):
    nivel_glicemia = models.FloatField(blank=True, null=True)
    nivel_colesterol = models.FloatField(blank=True, null=True)
    nivel_plasmaticos_colesterol = models.FloatField(blank=True, null=True)
    nivel_triglicerideos = models.FloatField(blank=True, null=True)
    nivel_lipoproteinas_plasmaticos = models.FloatField(blank=True, null=True)
    nivel_pressão_arterial = models.FloatField(blank=True, null=True)

class Exame(models.Model):
    doenças_familiares = models.TextField(blank=True)
    doenças_pessoas = models.TextField(blank=True)
    doenças_atual = models.TextField(blank=True)
    remedios = models.TextField(blank=True)
    fuma = models.BooleanField(blank=True)
    consumo_alcool = models.BooleanField(blank=True)
    tempo_medio_sono = models.IntegerField(blank=True, null=True)
    exame_sangue = models.OneToOneField(Exame_hemograma, on_delete=models.CASCADE, null=True)

class Questionario(models.Model):
    pergunta_1 = models.BooleanField(blank=True)
    pergunta_2 = models.BooleanField(blank=True)
    pergunta_3 = models.BooleanField(blank=True)
    pergunta_4 = models.BooleanField(blank=True)
    pergunta_5 = models.BooleanField(blank=True)
    pergunta_6 = models.BooleanField(blank=True)
    pergunta_7 = models.BooleanField(blank=True)

class Ficha(models.Model):
    dados_pessoais = models.OneToOneField(Dado_pessoal, on_delete=models.CASCADE, null=True)
    exames = models.OneToOneField(Exame, on_delete=models.CASCADE, null=True)
    questionario = models.OneToOneField(Questionario, on_delete=models.CASCADE, null=True)

class Cadastro(models.Model):
    nome_usuario = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    senha = models.TextField(blank=True)
    CPF = models.CharField(max_length=25, blank=True)
    ficha = models.OneToOneField(Ficha, on_delete=models.CASCADE, null=True)

class medico (models.Model):
    nome_medico = models.TextField()
    email = models.EmailField()
    senha = models.TextField()
    CPF = models.CharField(max_length=25)
    CRM = models.CharField(max_length=100)
    ficha = models.ManyToManyField(Ficha)
    