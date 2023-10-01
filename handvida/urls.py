from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('alunos/', include('alunos.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('alunos.urls')),
    path('turmas/', include ('turmas.urls')),
    path('frequencia/', include ('frequencia.urls')),
]
