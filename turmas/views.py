from django.shortcuts import render
from .models import Turmas
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
def turmas(request):
    if request.method == "GET":
        #parametros para o paginador    
        parametro_page = request.GET.get('page','1')
        parametro_limit = request.GET.get('limit','10')

        if not(parametro_limit.isdigit() and int(parametro_limit) > 0):
            parametro_limit = '10'

        turma_paginator = Paginator(Turmas.objects.all(), parametro_limit)

        try:
            page = turma_paginator.page(parametro_page)
        except (EmptyPage, PageNotAnInteger):
            page = turma_paginator.page(1)

        #passar dados para a pagina
        lista_turmas = {
                'lista_turmas': page
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
        #paginador    
        parametro_page = request.GET.get('page','1')
        parametro_limit = request.GET.get('limit','10')

        if not(parametro_limit.isdigit() and int(parametro_limit) > 0):
            parametro_limit = '10'

        turma_paginator = Paginator(Turmas.objects.all(), parametro_limit)

        try:
            page = turma_paginator.page(parametro_page)
        except (EmptyPage, PageNotAnInteger):
            page = turma_paginator.page(1)

        #passar dados para a pagina
        lista_turmas = {
                'lista_turmas': page
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
