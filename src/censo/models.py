from django.db import models

class Morador(models.Model):

    SEXO_CHOICES = [
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
    ]

    RENDA_CHOICES = [
        ('Menos de 1 salário mínimo', 'Menos de 1 salário mínimo'),
        ('De 1 a 2 salários mínimos', 'De 1 a 2 salários mínimos'),
        ('De 2 a 3 salários mínimos', 'De 2 a 3 salários mínimos'),
        ('De 3 a 4 salários mínimos', 'De 3 a 4 salários mínimos'),
        ('De 4 a 5 salários mínimos', 'De 4 a 5 salários mínimos'),
        ('Mais de 5 salários mínimos', 'Mais de 5 salários mínimos'),
    ]

    ESTADO_CIVIL_CHOICES = [
        ('Solteiro', 'Solteiro'),
        ('Casado', 'Casado'),
        ('Divorciado', 'Divorciado'),
        ('Viúvo', 'Viúvo'),
    ]

    ETNIA_CHOICES = [
        ('Branca', 'Branca'),
        ('Pardo', 'Pardo'),
        ('Preta', 'Preta'),
        ('Amarela', 'Amarela'),
        ('Indígena', 'Indígena'),
    ]

    ESCOLARIDADE_CHOICES = [
        ('Analfabeto', 'Analfabeto'),
        ('Fundamental incompleto', 'Fundamental incompleto'),
        ('Fundamental completo', 'Fundamental completo'),
        ('Médio incompleto', 'Médio incompleto'),
        ('Médio completo', 'Médio completo'),
        ('Superior incompleto', 'Superior incompleto'),
        ('Superior completo', 'Superior completo'),
    ]

    RELIGIAO_CHOICES = [
        ('Católica', 'Católica'),
        ('Evangélica', 'Evangélica'),
        ('Espírita', 'Espírita'),
        ('Umbanda', 'Umbanda'),
        ('Candomblé', 'Candomblé'),
        ('Sem religião', 'Sem religião'),
    ]

    cpf = models.CharField(max_length=11, unique=True, primary_key=True)
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
    num_casa = models.IntegerField()
    sexo = models.TextField(choices=SEXO_CHOICES)
    renda = models.TextField(choices=RENDA_CHOICES, null=True, blank=True)
    data_nascimento = models.DateField()
    estado_civil = models.TextField(choices=ESTADO_CIVIL_CHOICES, null=True, blank=True)
    etnia = models.TextField(choices=ETNIA_CHOICES, null=True, blank=True)
    escolaridade = models.TextField(choices=ESCOLARIDADE_CHOICES, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    nacionalidade = models.CharField(max_length=30)
    deficiencia = models.BooleanField(default=False)
    num_dependentes = models.IntegerField(default=0, null=True, blank=True)
    religiao = models.CharField(max_length=50, choices=RELIGIAO_CHOICES, null=True, blank=True)

    
    def str(self):
        return self.cpf
    
class Indicadores(models.Model):
    pergunta = models.CharField(max_length=100)
    resposta = models.TextField()
    descricao = models.TextField(blank=True, null=True)
  
    def __str__(self):
        return self.pergunta
    
