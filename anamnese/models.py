from django.db import models

# Cadastro de Usuários
class Cadastro(models.Model):
    nome_usuario = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    senha = models.CharField(max_length=100, blank=True)
    cpf = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return self.nome_usuario

# Dados Pessoais de cada Ficha
class DadoPessoal(models.Model):
    nome = models.CharField(max_length=100, blank=True)
    endereco = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    data_nascimento = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True)
    profissao = models.CharField(max_length=100, blank=True)
    estado_civil = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nome

# Exame Hemograma (Detalhes de Exames)
class ExameHemograma(models.Model):
    nivel_glicemia = models.FloatField(blank=True, null=True)
    nivel_colesterol = models.FloatField(blank=True, null=True)
    nivel_plasmaticos_colesterol = models.FloatField(blank=True, null=True)
    nivel_triglicerideos = models.FloatField(blank=True, null=True)
    nivel_lipoproteinas_plasmaticos = models.FloatField(blank=True, null=True)
    nivel_pressao_arterial = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'Hemograma - Glicemia: {self.nivel_glicemia}'

# Informações Gerais de Exames
class Exame(models.Model):
    doencas_familiares = models.TextField(blank=True)
    doencas_pessoais = models.TextField(blank=True)
    doencas_atual = models.TextField(blank=True)
    remedios = models.TextField(blank=True)
    fuma = models.BooleanField(blank=True)
    consumo_alcool = models.BooleanField(blank=True)
    tempo_medio_sono = models.IntegerField(blank=True, null=True)
    exame_sangue = models.OneToOneField(ExameHemograma, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Exame - Doenças Atuais: {self.doencas_atual}'

# Questionário de Saúde
class Questionario(models.Model):
    pergunta_1 = models.BooleanField(blank=True)
    pergunta_2 = models.BooleanField(blank=True)
    pergunta_3 = models.BooleanField(blank=True)
    pergunta_4 = models.BooleanField(blank=True)
    pergunta_5 = models.BooleanField(blank=True)
    pergunta_6 = models.BooleanField(blank=True)
    pergunta_7 = models.BooleanField(blank=True)

    def __str__(self):
        return 'Questionário de Saúde'

# Fichas de Exames (associadas ao Cadastro/Usuário)
class Ficha(models.Model):
    usuario = models.ForeignKey(Cadastro, on_delete=models.CASCADE)  # Relaciona a Ficha com o Usuário
    dados_pessoais = models.OneToOneField(DadoPessoal, on_delete=models.CASCADE, null=True)
    exames = models.ForeignKey(Exame, on_delete=models.CASCADE, null=True)  # Permite múltiplos exames
    questionario = models.OneToOneField(Questionario, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Ficha de {self.usuario}'

