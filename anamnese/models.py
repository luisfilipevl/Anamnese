from django.db import models

# Cadastro de Usuários
class Cadastro(models.Model):
    nome_usuario = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    senha = models.CharField(max_length=100, blank=True)
    cpf = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return self.nome_usuario


# Fichas de Exames (associadas ao Cadastro/Usuário)
class Ficha(models.Model):
    usuario = models.ForeignKey(Cadastro, on_delete=models.CASCADE)  # Relaciona a Ficha com o Usuário
    nome = models.CharField(max_length=100, blank=True)
    endereco = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    data_nascimento = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True)
    profissao = models.CharField(max_length=100, blank=True)
    estado_civil = models.CharField(max_length=100, blank=True)
    doencas_familiares = models.TextField(blank=True)
    doencas_pessoais = models.TextField(blank=True)
    doencas_atual = models.TextField(blank=True)
    remedios = models.TextField(blank=True)
    fuma = models.BooleanField(blank=True)
    consumo_alcool = models.BooleanField(blank=True)
    tempo_medio_sono = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return f'Ficha de {self.nome}'

