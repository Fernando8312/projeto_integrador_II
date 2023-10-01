from django.urls import path 
from . import views

urlpatterns = [
    path('', views.frequencia, name="frequencia"),
    path('att_frequencia/<int:id>', views.att_frequencia, name='att_frequencia'),
    path('apagar_dia_aula/<int:id>', views.apagar_dia_aula, name = "apagar_dia_aula"),
    
]