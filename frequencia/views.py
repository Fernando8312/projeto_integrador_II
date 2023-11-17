from django.shortcuts import render
from .models import Frequencia
from turmas.models import Turmas
from alunos.models import Alunos
from frequencia.models import Frequencia, Dia_aula
from django.core import serializers
import json
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def frequencia(request):
    if request.method == "GET":

        #parametros para o paginador    
        parametro_page = request.GET.get('page','1')
        parametro_limit = request.GET.get('limit','10')

        if not(parametro_limit.isdigit() and int(parametro_limit) > 0):
            parametro_limit = '10'

        freq_paginator = Paginator(Dia_aula.objects.all(), parametro_limit)

        try:
            page = freq_paginator.page(parametro_page)
        except (EmptyPage, PageNotAnInteger):
            page = freq_paginator.page(1)


        lista_frequencia = {
                'lista_turmas':Turmas.objects.all(),
                'lista_aulas': page,
                
            }
        return render(request,'frequencia.html', lista_frequencia)
    elif request.method == "POST":
        turma_id = request.POST.get('turma')
        data_lancamento = request.POST.get('data_aula')

        #verificacao se a data esta em branco
        if data_lancamento == "":
        
            #parametros para o paginador    
            parametro_page = request.GET.get('page','1')
            parametro_limit = request.GET.get('limit','10')

            if not(parametro_limit.isdigit() and int(parametro_limit) > 0):
                parametro_limit = '10'

            freq_paginator = Paginator(Dia_aula.objects.all(), parametro_limit)

            try:
                page = freq_paginator.page(parametro_page)
            except (EmptyPage, PageNotAnInteger):
                page = freq_paginator.page(1) 
            
            lista_frequencia = {
                'lista_turmas':Turmas.objects.all(),
                'lista_aulas': page,
                
            }
            return render(request,'frequencia.html', lista_frequencia)

        #verificar se ja existe dia e turma no banco de dados
        busca = Q(
             Q(data__exact=data_lancamento) & Q(id_turma__exact = turma_id)
        )
        turma_data_dia = Dia_aula.objects.filter(busca)
        if turma_data_dia.exists():
            print("ja existe esse dia e turma no banco de dados")
            print(turma_data_dia)
            print("id do registro")
            id_registro = {
                'Id':json.loads(serializers.serialize('json',turma_data_dia))[0]['pk'],
            }
            print(id_registro['Id'])
            #chamar pagina att_frequencia para alterar dados dessa turma nesse dia
            return redirect('att_frequencia/'+str(id_registro['Id']))
        else:
            print("nao existe no banco de dados") 
            #Gravar no banco de dados
            dia_aula = Dia_aula(
                data = data_lancamento,
                id_turma = turma_id
            )
            dia_aula.save()

            #chamar a pagina att_frequencia para gravar as presenças
            busca = Q(
                Q(data__exact=data_lancamento) & Q(id_turma__exact = turma_id)
            )
            turma_data_dia = Dia_aula.objects.filter(busca)
            if turma_data_dia.exists():
                id_registro = {
                    'Id':json.loads(serializers.serialize('json',turma_data_dia))[0]['pk'],
                }
                return redirect('att_frequencia/'+str(id_registro['Id']))

@login_required    
def att_frequencia(request, id):
    if request.method =="GET":
        #verificar se a url digitada existe no banco, se não existir voltar para lancamento de frequencia
        busca = Q(id__exact = id)
        turma_data_dia = Dia_aula.objects.filter(busca)
        if turma_data_dia.exists():
            #renderizar a pagina com a lista de alunos
            #dados_controle retorna de forma serializada os dados da tabela Dia_aula
            dados_controle = {
                'dados':json.loads(serializers.serialize('json', turma_data_dia))[0]['fields'],
            }

            
            #Formata os dados para enviar para a pagina

            #consulta se ja tinha sido lancado dados no banco de dados
            print(dados_controle['dados']['controle'])
            #print("variavel presentes:")
            #print(dados_alunos['presentes'])
            controle = dados_controle['dados']['controle']
            
            if controle==False:
                print("nao foi lancado no banco de dados")
                            #retorna os dados dos alunos e turma
                dados_alunos = {
                    'presentes':[],
                    'alunos':Alunos.objects.filter(turma=dados_controle['dados']['id_turma']),
                    'turma': json.loads(serializers.serialize('json',Turmas.objects.filter(id=dados_controle['dados']['id_turma'])))[0]['fields'],
                }
                lista_frequencia={
                    'id': id, 
                    'controle': dados_controle,
                    'alunos' : dados_alunos,
                    'up_tabela':0,
                }
                return render(request, 'att_frequencia.html', lista_frequencia)    

            else:
                #atualiza dados existentes
                #busca dados na tabela frequencia
                busca = Q(
                    Q(data__exact=dados_controle['dados']['data']) & Q(id_turma__exact = dados_controle['dados']['id_turma'])
                )
                dados_alunos = {
                    'presentes':Frequencia.objects.filter(busca),
                    'alunos':Alunos.objects.filter(turma=dados_controle['dados']['id_turma']),
                    'turma': json.loads(serializers.serialize('json',Turmas.objects.filter(id=dados_controle['dados']['id_turma'])))[0]['fields'],
                }
                lista_frequencia={
                    'id': id, 
                    'controle': dados_controle,
                    'alunos' : dados_alunos,
                    'up_tabela':1,
                }
                print("ja existem dados no banco de dados")
                return render(request, 'att_frequencia.html', lista_frequencia)   




        else:

                        #parametros para o paginador    
            parametro_page = request.GET.get('page','1')
            parametro_limit = request.GET.get('limit','10')

            if not(parametro_limit.isdigit() and int(parametro_limit) > 0):
                parametro_limit = '10'

            freq_paginator = Paginator(Dia_aula.objects.all(), parametro_limit)

            try:
                page = freq_paginator.page(parametro_page)
            except (EmptyPage, PageNotAnInteger):
                page = freq_paginator.page(1) 

            lista_frequencia = {
                'lista_turmas':Turmas.objects.all(),
                'lista_aulas': page,
                
            }
            return render(request, 'frequencia.html', lista_frequencia)

    if request.method == "POST":  
       #Gravar lista de presença no banco de dados
        controle = get_object_or_404(Dia_aula, id=id)
        atualiza_s_n = request.POST.get('atualiza_s_n')
        print("novo lancamento ou atualizacao:")
        print(type(atualiza_s_n))
        print(atualiza_s_n)
        
        if atualiza_s_n == '0':
            try:
                #gravar controle na tabela Dias_aulas
                controle.controle = True
        
                controle.save()
                print("salvei a tabela controle")
                #pegar os dados do formulario
                id_aluno_formulario = request.POST.getlist('id')
                data_formulario = request.POST.getlist('data')
                turma_formulario = request.POST.getlist('turma')
                presenca_formulario = request.POST.getlist('presenca')
                id_controle_formulario = request.POST.getlist('id_controle')



                for id_dia_aula1, id_aluno1,id_turma1, data1, presenca1 in zip(id_controle_formulario, id_aluno_formulario, turma_formulario, data_formulario, presenca_formulario):
                    print(id_dia_aula1, id_aluno1, id_turma1, data1, presenca1)
                    presentes = Frequencia(
                        id_dia_aula = id_dia_aula1,
                        id_aluno = id_aluno1, 
                        id_turma = id_turma1, 
                        data = data1, 
                        presenca = presenca1,    
                    )
                    presentes.save()

                    
                print("gravei os dados na tabela frequencia")

            
                #parametros para o paginador    
                parametro_page = request.GET.get('page','1')
                parametro_limit = request.GET.get('limit','10')

                if not(parametro_limit.isdigit() and int(parametro_limit) > 0):
                    parametro_limit = '10'

                freq_paginator = Paginator(Dia_aula.objects.all(), parametro_limit)

                try:
                    page = freq_paginator.page(parametro_page)
                except (EmptyPage, PageNotAnInteger):
                    page = freq_paginator.page(1) 

                lista_frequencia = {
                    'lista_turmas':Turmas.objects.all(),
                    'lista_aulas': page,

                }
                return render(request,'frequencia.html', lista_frequencia)

            except:
                print("aconteceu um erro")
                #Voltar para tela de escolha de data e turma
                #parametros para o paginador    
                parametro_page = request.GET.get('page','1')
                parametro_limit = request.GET.get('limit','10')

                if not(parametro_limit.isdigit() and int(parametro_limit) > 0):
                    parametro_limit = '10'

                freq_paginator = Paginator(Dia_aula.objects.all(), parametro_limit)

                try:
                    page = freq_paginator.page(parametro_page)
                except (EmptyPage, PageNotAnInteger):
                    page = freq_paginator.page(1) 
                lista_frequencia = {
                'lista_turmas':Turmas.objects.all(),
                'lista_aulas': page,
                    
                }
                return render(request,'frequencia.html', lista_frequencia)

        if atualiza_s_n == '1':
            try:
                #gravar controle na tabela Dias_aulas
                controle.controle = True
        
                controle.save()
                print("salvei a tabela controle")
                #pegar os dados do formulario
                id_aluno_formulario = request.POST.getlist('id')
                data_formulario = request.POST.getlist('data')
                turma_formulario = request.POST.getlist('turma')
                presenca_formulario = request.POST.getlist('presenca')
                id_controle_formulario = request.POST.getlist('id_controle')
                id_frequencia = request.POST.getlist('id_presenca')



                for id_dia_aula1, id_aluno1,id_turma1, data1, presenca1, id_frequencia1 in zip(id_controle_formulario, id_aluno_formulario, turma_formulario, data_formulario, presenca_formulario, id_frequencia):
                    print(id_dia_aula1, id_aluno1, id_turma1, data1, presenca1, id_frequencia1)
                    presentes = get_object_or_404(Frequencia, id=id_frequencia1)
                    presentes.id_dia_aula = id_dia_aula1
                    presentes.id_aluno = id_aluno1
                    presentes.id_turma = id_turma1 
                    presentes.data = data1 
                    presentes.presenca = presenca1
                    
                    presentes.save()

                    
                print("gravei os dados na tabela frequencia")

            
                #parametros para o paginador    
                parametro_page = request.GET.get('page','1')
                parametro_limit = request.GET.get('limit','10')

                if not(parametro_limit.isdigit() and int(parametro_limit) > 0):
                    parametro_limit = '10'

                freq_paginator = Paginator(Dia_aula.objects.all(), parametro_limit)

                try:
                    page = freq_paginator.page(parametro_page)
                except (EmptyPage, PageNotAnInteger):
                    page = freq_paginator.page(1) 

                lista_frequencia = {
                    'lista_turmas':Turmas.objects.all(),
                    'lista_aulas': page,

                }
                return render(request,'frequencia.html', lista_frequencia)

            except:
                print("aconteceu um erro")
                #Voltar para tela de escolha de data e turma
                #parametros para o paginador    
                parametro_page = request.GET.get('page','1')
                parametro_limit = request.GET.get('limit','10')

                if not(parametro_limit.isdigit() and int(parametro_limit) > 0):
                    parametro_limit = '10'

                freq_paginator = Paginator(Dia_aula.objects.all(), parametro_limit)

                try:
                    page = freq_paginator.page(parametro_page)
                except (EmptyPage, PageNotAnInteger):
                    page = freq_paginator.page(1) 

                lista_frequencia = {
                'lista_turmas':Turmas.objects.all(),
                'lista_aulas': page,
                    
                }
                return render(request,'frequencia.html', lista_frequencia)
       


@login_required
def apagar_dia_aula(request, id):
        try:
            dia = Dia_aula.objects.get(id=id)
            print(dia)
            dia.delete()
            return redirect(reverse('frequencia'))
        except:
            return redirect(reverse('frequencia'))