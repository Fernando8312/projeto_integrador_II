from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Alunos
from turmas.models import Turmas
import re
from django.core import serializers
import json
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def alunos(request):
    if request.method == "GET":
        lista_turmas = Turmas.objects.all()
        print(lista_turmas)
        
        #parametros para o paginador    
        parametro_page = request.GET.get('page','1')
        parametro_limit = request.GET.get('limit','10')

        if not(parametro_limit.isdigit() and int(parametro_limit) > 0):
            parametro_limit = '10'

                
        #campo de pesquisa
        txt_pesquisa = request.GET.get('Pesquisa_Nome')
        if txt_pesquisa:
            print(txt_pesquisa)

            alunos_paginador = Paginator(Alunos.objects.filter(nome__icontains=txt_pesquisa), parametro_limit)

            try:
                page = alunos_paginador.page(parametro_page)
            except (EmptyPage, PageNotAnInteger):
                page = alunos_paginador.page(1)

            lista_alunos = {
                'lista_alunos':page,
                'lista_turmas':lista_turmas, 
            }
            print(lista_alunos)
            return render(request,'alunos.html', lista_alunos)
        else:
            print("nao tem dados")

            alunos_paginador = Paginator(Alunos.objects.all(), parametro_limit)

            try:
                page = alunos_paginador.page(parametro_page)
            except (EmptyPage, PageNotAnInteger):
                page = alunos_paginador.page(1)    
            lista_alunos = {
                'lista_alunos':page,
                'lista_turmas':lista_turmas,                
            }
            print(lista_alunos)
            return render(request,'alunos.html', lista_alunos)
        

    elif request.method == "POST":
        nome = request.POST.get('Nome')
        responsavel = request.POST.get('Responsavel')
        genero = request.POST.get('genero')
        cpf = request.POST.get('cpf')
        rg = request.POST.get('rg')
        situacao = request.POST.get('situacao')
        turma = request.POST.get('turma')
        endereco = request.POST.get('endereco')
        numero = request.POST.get('numero')
        bairro = request.POST.get('bairro')
        cep = request.POST.get('cep')
        cidade = request.POST.get('cidade')
        uf = request.POST.get('UF')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        obs = request.POST.get('observacoes')
        
        aluno_cpf = Alunos.objects.filter(cpf = cpf)
        if aluno_cpf.exists():
            print(nome,responsavel,genero, cpf, rg, situacao, turma, endereco, numero, bairro, cep, cidade, uf, email, telefone, obs)
            return render(request, 'alunos.html', {'Nome': nome, 'Responsavel': responsavel, 'genero' : genero,'cpf': cpf,'rg':rg, 'situacao':situacao, 'turma':turma, 'endereco':endereco, 'numero': numero, 'bairro':bairro, 'cep':cep, 'cidade':cidade, 'UF':uf, 'email':email, 'telefone':telefone, 'observacoes':obs})
    
        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            return render(request, 'alunos.html', {'Nome': nome, 'Responsavel': responsavel, 'genero' : genero,'cpf': cpf,'rg':rg, 'situacao':situacao, 'turma':turma, 'endereco':endereco, 'numero': numero,'bairro':bairro, 'cep':cep, 'cidade':cidade, 'UF':uf, 'email':email, 'telefone':telefone, 'observacoes':obs})

        aluno = Alunos(
            nome = nome,
            responsavel = responsavel,
            genero = genero,
            cpf = cpf,
            rg = rg,
            situacao = situacao,
            turma = turma,
            endereco = endereco,
            numero = numero,
            bairro = bairro,
            cep = cep,
            cidade = cidade,
            uf = uf,
            email = email,
            telefone = telefone,
            obs = obs

        
        )
    
        aluno.save()

        #paginador
        #parametros para o paginador    
        parametro_page = request.GET.get('page','1')
        parametro_limit = request.GET.get('limit','10')

        if not(parametro_limit.isdigit() and int(parametro_limit) > 0):
            parametro_limit = '10'

        alunos_paginador = Paginator(Alunos.objects.all(), parametro_limit)

        try:
            page = alunos_paginador.page(parametro_page)
        except (EmptyPage, PageNotAnInteger):
            page = alunos_paginador.page(1)     

        lista_alunos = {
            'lista_alunos':page,
            'lista_turmas':Turmas.objects.all(), 
            }
        return render(request,'alunos.html', lista_alunos)

@login_required   
def att_aluno(request):
    id_aluno = request.POST.get('id_aluno')
    aluno = Alunos.objects.filter(id=id_aluno)
    aluno_json = json.loads(serializers.serialize('json', aluno))[0]['fields']
    aluno_id = json.loads(serializers.serialize('json',aluno))[0]['pk']
    dados={'aluno_id': aluno_id, 'aluno': aluno_json}
    print(dados)
    return JsonResponse(dados)

@login_required
def update_aluno(request, id):
    body = json.loads(request.body)

    nome = body['nome']
    responsavel= body['responsavel']
    genero= body['genero']
    cpf = body['cpf']
    rg = body['rg']
    situacao = body['situacao']
    turma = body['turma']
    endereco = body['endereco'] 
    numero = body['numero']
    bairro = body['bairro']
    cep = body['cep']
    cidade= body['cidade']
    uf = body['uf']
    email = body['email']
    telefone = body['telefone']
    obs = body['obs']

    aluno = get_object_or_404(Alunos, id=id)
    try:
        aluno.nome = nome
        aluno.responsavel = responsavel
        aluno.genero= genero
        aluno.cpf = cpf
        aluno.rg = rg
        aluno.situacao = situacao
        aluno.turma = turma
        aluno.endereco = endereco
        aluno.numero = numero
        aluno.bairro = bairro
        aluno.cep = cep
        aluno.cidade= cidade
        aluno.uf = uf
        aluno.email = email
        aluno.telefone = telefone
        aluno.obs = obs

        aluno.save()
        

        return JsonResponse({'status': '200', 'nome': nome, 'responsavel': responsavel, 'genero': genero, 'cpf': cpf, 'rg' : rg, 'situacao' : situacao, 'turma' : turma, 'endereco' : endereco,'numero': numero, 'bairro': bairro, 'cep' :cep, 'cidade': cidade, 'uf' : uf, 'email' : email, 'telefone' : telefone, 'obs' : obs})
        
    
    except:
        return JsonResponse({'status': '500'})

@login_required    
def apagar_aluno(request, id):
    try:
        aluno = Alunos.objects.get(id=id)
        print(aluno)
        aluno.delete()
        return redirect(reverse('alunos'))
    except:
        return redirect(reverse('alunos'))


