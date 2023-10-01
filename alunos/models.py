from django.db import models

class Alunos(models.Model):
    nome = models.CharField(max_length=255)
    responsavel = models.CharField(max_length=255)
    genero = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=9)
    situacao = models.CharField(max_length=7)
    turma = models.IntegerField()
    endereco = models.CharField(max_length=255)
    numero = models.CharField(max_length=20)
    bairro = models.CharField(max_length=255)
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=255)
    uf = models.CharField(max_length=2)
    email = models.CharField(max_length=255)
    telefone = models.CharField(max_length=10)
    obs = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.nome