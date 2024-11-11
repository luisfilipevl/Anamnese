from django.db import models

# Cadastro de Usuários
class Cadastro(models.Model):
    nome_usuario = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    senha = models.CharField(max_length=100, blank=True)
    CPF = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return self.nome_usuario


# Fichas de Exames (associadas ao Cadastro/Usuário)
class Ficha(models.Model):
    # Torne 'usuario' temporariamente opcional
    usuario = models.ForeignKey(Cadastro, on_delete=models.CASCADE, null=True, blank=True)

    nome = models.CharField(max_length=100, blank=True)
    endereco = models.TextField(blank=True)
    data_nascimento = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True)
    profissao = models.CharField(max_length=100, blank=True)
    estado_civil = models.CharField(max_length=100, blank=True)

    doencas_familiares = models.TextField(blank=True)
    doencas_pessoais = models.TextField(blank=True)
    doencas_atual = models.TextField(blank=True)
    remedios = models.TextField(blank=True)
    tempo_medio_sono = models.IntegerField(blank=True, null=True)

    nivel_glicemia = models.FloatField(blank=True, null=True)
    nivel_colesterol = models.FloatField(blank=True, null=True)
    nivel_plasmaticos_colesterol = models.FloatField(blank=True, null=True)
    nivel_triglicerideos = models.FloatField(blank=True, null=True)
    nivel_lipoproteinas_plasmaticos = models.FloatField(blank=True, null=True)
    nivel_pressão_arterial = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'Ficha de {self.nome}'
