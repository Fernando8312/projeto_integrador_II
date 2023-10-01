from django.db import models

class Turmas(models.Model):
    nome = models.CharField(max_length=255)
    professor = models.CharField(max_length=255)
    dias_aulas = models.CharField(max_length=255)
    obs = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nome