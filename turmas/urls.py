from django.urls import path 
from . import views

urlpatterns = [
    path('', views.turmas, name="turmas"),
    path('apagar_turmas/<int:id>', views.apagar_turmas, name = "apagar_turmas"),
    
]