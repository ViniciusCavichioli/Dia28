from django.db import models
from django.contrib.auth.models import User

class Endereco(models.Model):
    logradouro = models.CharField(max_length = 128)
    complemento = models.CharField(max_length = 256, null = True)
    uf = models.CharField(max_length = 2, null = True)
    cidade =  models.CharField(max_length = 64, null = True)
    cep = models.CharField(max_length = 10)

    def __str__(self):
        return '{},{},{}'.format(self.logradouro, self.cidade, self.uf)

class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    descricao = models.TextField()
    data_nascimento = models.DateField(blank=True, null=True)
    endereco = models.ForeignKey(Endereco, related_name = 'pessoas', null = True, blank = False)
    usuario = models.OneToOneField(User)

    def __str__(self):
        return self.nome

class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length = 12)
    mae = models.CharField(max_length = 100)
    pai = models.CharField(max_length = 100)

    def __str__(self):
        return self.cpf

class Evento(models.Model):
    nome = models.CharField(max_length = 100)
    descricao = models.TextField()
    sigla = models.CharField(max_length = 10)
    numero = models.IntegerField(max_length = 10)
    realizador = models.ForeignKey(PessoaFisica, related_name = 'PessoaFisica', null = True, blank = False)
    endereco = models.ForeignKey(Endereco, related_name = 'eventos', null = True, blank = False)
    logo = models.CharField(max_length = 10)
    data_de_inicio = models.DateField(max_length = 10)
    data_de_fim = models.DateField(max_length = 10)

    def __str__(self):
        return self.nome

class Inscricao(models.Model):
    data_Inscricao = models.DateField(max_length = 10)
    preco = models.FloatField()
    pessoa = models.ForeignKey(PessoaFisica, related_name = 'inscrição', null = True, blank = False)
    evento = models.ForeignKey(Evento, related_name = 'eventos', null = True, blank = False)
