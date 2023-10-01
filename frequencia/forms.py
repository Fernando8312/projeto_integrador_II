from django import forms
from .models import Frequencia

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Frequencia
        fields = ['id_aluno', 'id_turma', 'data', 'presenca']
        