from django.urls import path 
from . import views

urlpatterns = [
    path('', views.alunos, name="alunos"),
    path('atualiza_aluno/', views.att_aluno, name='atualiza_aluno'),
    path('update_aluno/<int:id>', views.update_aluno, name = "update_aluno"),
    path('apagar_aluno/<int:id>', views.apagar_aluno, name = "apagar_aluno"),

]