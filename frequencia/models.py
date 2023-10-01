from django.db import models

class Frequencia(models.Model):
    id_dia_aula = models.IntegerField(null=True, blank=True)
    id_aluno = models.IntegerField(null=True, blank=True)
    id_turma = models.IntegerField(null=True, blank=True)
    data = models.DateField(null=True, blank=True)
    presenca = models.BooleanField(null=True, blank=True, default=False)
    

    def __str__(self) -> str:
        return self.id_aluno
    
class Dia_aula(models.Model):
    data = models.DateField(null=True, blank=True)
    id_turma = models.IntegerField(null=True, blank=True)
    controle = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self) -> str:
        return str(self.data)