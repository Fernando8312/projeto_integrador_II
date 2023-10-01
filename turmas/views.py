from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Turmas
import re
from django.core import serializers
import json
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@login_required
def turmas(request):
    if request.method == "GET":
        lista_turmas = {
                'lista_turmas':Turmas.objects.all()
            }
        print(lista_turmas)
        return render(request,'turmas.html', lista_turmas)
    elif request.method == "POST":
        turma = request.POST.get('Turma')
        professor = request.POST.get('Professor')
        dias = request.POST.get('Dias')
        obs = request.POST.get('Obs')

        turma = Turmas(
            nome = turma,
            professor = professor,
            dias_aulas = dias,
            obs = obs

        )
        turma.save()
        lista_turmas = {
            'lista_turmas':Turmas.objects.all()
            }
        return render(request,'turmas.html', lista_turmas)
    


@login_required    
def apagar_turmas(request, id):
    try:
        turma = Turmas.objects.get(id=id)
        print(turma)
        turma.delete()
        return redirect(reverse('turmas'))
    except:
        return redirect(reverse('turmas'))
