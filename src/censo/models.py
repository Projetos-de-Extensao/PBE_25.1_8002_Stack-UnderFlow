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


    def __str__(self):
        return f"{self.nome} {self.sobrenome}: {self.cpf}"

class Indicadores(models.Model):
    pergunta = models.CharField(max_length=100)
    resposta = models.TextField()
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.pergunta


class Domicilio(models.Model):

    Especie_CHOICES =[
        ('Domicilio particular permanentemente', 'DOMICÍLIO PARTICULAR PERMANENTE OCUPADO'),
        ('Domicilio particular improvisado ocupado', 'DOMICÍLIO PARTICULAR IMPROVISADO OCUPADO'),
        ('Domicilio coletivo com morador', 'DOMICÍLIO COLETIVO COM MORADOR'),
    ]

    Tipo_CHOICES= [
        ('Casa', 'Casa'),
        ('Casa de vila ou em condomínio', 'Casa de vila ou em condomínio'),
        ('Apartamento', 'Apartamento'),
        ('Habitação em casa de cômodos ou cortiço', 'Habitação em casa de cômodos ou cortiço'),
        ('Habitação indígena sem paredes ou maloca', 'Habitação indígena sem paredes ou maloca'),
        ('Estrutura residencial permanente degradada ou inacabada', 'Estrutura residencial permanente degradada ou inacabada'),
        ('Tenda ou barraca de lona, plástico ou tecido', 'Tenda ou barraca de lona, plástico ou tecido'),
        ('Dentro do estabelecimento em funcionamento', 'Dentro do estabelecimento em funcionamento'),
        ('Outros (abrigos naturais e outras estruturas improvisadas)', 'Outros (abrigos naturais e outras estruturas improvisadas)'),
        ('Estrutura improvisada em logradouro público, exceto tenda ou barraca', 'Estrutura improvisada em logradouro público, exceto tenda ou barraca'),
        ('Estrutura não residencial permanente degradada ou inacabada', 'Estrutura não residencial permanente degradada ou inacabada'),
        ('Veículos (carros, caminhões, trailers, barcos etc.)', 'Veículos (carros, caminhões, trailers, barcos etc.)'),
        ('Asilo ou outra instituição de longa permanência para idosos', 'Asilo ou outra instituição de longa permanência para idosos'),
        ('Hotel ou pensão', 'Hotel ou pensão'),
        ('Alojamento', 'Alojamento'),
        ('Penitenciária, centro de detenção e similar', 'Penitenciária, centro de detenção e similar'),
        ('Outro', 'Outro'),
        ('Abrigo, albergue ou casa de passagem para população em situação de rua', 'Abrigo, albergue ou casa de passagem para população em situação de rua'),
        ('Abrigo, casas de passagem ou república assistencial para outros grupos vulneráveis', 'Abrigo, casas de passagem ou república assistencial para outros grupos vulneráveis'),
        ('Clínica psiquiátrica, comunidade terapêutica e similar', 'Clínica psiquiátrica, comunidade terapêutica e similar'),
        ('Orfanato e similar', 'Orfanato e similar'),
        ('Unidade de internação de menores', 'Unidade de internação de menores'),
        ('Quartel ou outra organização militar', 'Quartel ou outra organização militar'),

    ]

    ABASTECIMENTO_CHOICES = [
        ('Rede geral de distribuição', 'Rede geral de distribuição'),
        ('Poço artesiano', 'Poço artesiano'),
        ('Cacimba', 'Cacimba'),
        ('Rio, lago, córregos ou represas', 'Rio, lago, córregos ou represas'),
        ('fonte, nascente ou mina', 'fonte, nascente ou mina'),
        ('carro-pipa', 'carro-pipa'),
        ('água de chuva', 'água de chuva'),
        ('Outro', 'Outro'),
        ]

    ESGOTO_CHOICES = [
        ('Rede geral de esgoto', 'Rede geral de esgoto'),
        ('Fossa séptica', 'Fossa séptica'),
        ('Fossa rudimentar', 'Fossa rudimentar'),
        ('Rio, lago, córregos ou represas', 'Rio, lago, córregos ou represas'),
        ('Vala', 'Vala'),
        ('Outro', 'Outro'),
        ]

    DISTRIBUICAO_AGUA_CHOICES = [
        ('Encanada até dentro da moradia', 'Encanada até dentro da moradia'),
        ('Encanada, mas apenas terreno ou quintal', 'Encanada, mas apenas terreno ou quintal'),
        ('Não encanada', 'Não encanada'),
        ]

    LIXO_CHOICES = [
        ('Coletado pela prefeitura', 'Coletado pela prefeitura'),
        ('Coletado por empresa particular', 'Coletado por empresa particular'),
        ('Queimado', 'Queimado'),
        ('Enterrado', 'Enterrado'),
        ('Jogado em terreno baldio', 'Jogado em terreno baldio'),
        ('Jogado em rio, lago, córrego ou represa', 'Jogado em rio, lago, córrego ou represa'),
        ('Outro', 'Outro'),
        ]

    proprietario = models.ForeignKey(Morador, related_name='domicilios', on_delete=models.CASCADE, null=True, blank=True)
    uf = models.CharField (max_length=2)
    municipio = models.TextField()
    distrito = models.TextField()
    subdistrito = models.TextField()
    setor = models.TextField()
    numero = models.IntegerField()
    especie = models.TextField(choices=Especie_CHOICES, null=True, blank=True)
    tipo = models.TextField(choices=Tipo_CHOICES)
    quantidade_comodos = models.IntegerField()
    acesso_internet = models.BooleanField(default=False)
    abastecimento_agua = models.TextField(choices=ABASTECIMENTO_CHOICES)
    coleta_esgoto = models.TextField(choices=ESGOTO_CHOICES)
    distribuicao_agua = models.TextField(choices=DISTRIBUICAO_AGUA_CHOICES)
    lixo_destino = models.TextField (choices=LIXO_CHOICES)
    energia_eletrica = models.BooleanField(default=False)

    def __str__(self):
        return str(self.proprietario)