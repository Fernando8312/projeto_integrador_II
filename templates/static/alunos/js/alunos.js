function exibir_form(tipo){

    add_aluno = document.getElementById('adicionar_aluno')
    pesq_aluno = document.getElementById('pesquisar_aluno')
    pesq = document.getElementById('pesquisar')
    exibe_aluno = document.getElementById('exibe_alunos')
    exibe_form_att =document.getElementById('form_att_aluno')

    if(tipo == "1"){
        pesq_aluno.style.display = "block"
        pesq.style.display="block"
        exibe_aluno.style.display="block"
        add_aluno.style.display = "none"
        exibe_form_att = document.getElementById('form_att_aluno').style.display = 'none'
        

    }else if(tipo == "2"){
        add_aluno.style.display = "block";
        pesq_aluno.style.display = "none"
    }

}

function editar_aluno(aluno){
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    dados = new FormData()
    dados.append('id_aluno', aluno)
    
    fetch("/alunos/atualiza_aluno/", {
        method:"POST",
        headers:{'X-CSRFToken':csrf_token},
        body: dados

    }).then(function(result){
        return result.json()
    }).then(function(dados){

        
        document.getElementById('form_att_aluno').style.display = 'block'
        document.getElementById('exibe_alunos').style.display = 'none'
        document.getElementById('pesquisar').style.display = 'none'
        
        console.log(dados)
        id = document.getElementById('id')
        id.value = dados['aluno_id']

        nome = document.getElementById('Edit_nome')
        nome.value = dados['aluno']['nome']
       
        responsavel = document.getElementById('Edit_responsavel')
        responsavel.value = dados['aluno']['responsavel']

        genero = document.getElementById('Edit_genero')
        genero.value = dados['aluno']['genero']

        cpf = document.getElementById('Edit_cpf')
        cpf.value = dados['aluno']['cpf']

        rg = document.getElementById('Edit_rg')
        rg.value = dados['aluno']['rg']

        situacao = document.getElementById('Edit_situacao')
        situacao.value = dados['aluno']['situacao']

        turma = document.getElementById('Edit_turma')
        turma.value = dados['aluno']['turma']

        endereco = document.getElementById('Edit_endereco')
        endereco.value = dados['aluno']['endereco']

        numero = document.getElementById('Edit_numero')
        numero.value = dados['aluno']['numero']

        bairro = document.getElementById('Edit_bairro')
        bairro.value = dados['aluno']['bairro']

        cep = document.getElementById('Edit_cep')
        cep.value = dados['aluno']['cep']

        cidade = document.getElementById('Edit_cidade')
        cidade.value = dados['aluno']['cidade']

        uf = document.getElementById('Edit_UF')
        uf.value = dados['aluno']['uf']

        email = document.getElementById('Edit_email')
        email.value = dados['aluno']['email']

        telefone = document.getElementById('Edit_telefone')
        telefone.value = dados['aluno']['telefone']

        obs = document.getElementById('Edit_observacoes')
        obs.value = dados['aluno']['obs']
        
    })

}



function update_aluno(){
    id = document.getElementById('id').value
    nome = document.getElementById('Edit_nome').value
    responsavel = document.getElementById('Edit_responsavel').value
    genero = document.getElementById('Edit_genero').value
    cpf = document.getElementById('Edit_cpf').value
    rg = document.getElementById('Edit_rg').value
    situacao = document.getElementById('Edit_situacao').value
    turma = document.getElementById('Edit_turma').value
    endereco = document.getElementById('Edit_endereco').value
    numero = document.getElementById('Edit_numero').value
    bairro = document.getElementById('Edit_bairro').value
    cep = document.getElementById('Edit_cep').value
    cidade = document.getElementById('Edit_cidade').value
    uf = document.getElementById('Edit_UF').value
    email = document.getElementById('Edit_email').value
    telefone = document.getElementById('Edit_telefone').value
    obs = document.getElementById('Edit_observacoes').value
    

    fetch('/alunos/update_aluno/' + id, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: JSON.stringify({
            nome: nome,
            responsavel: responsavel,
            genero: genero,
            cpf : cpf,
            rg : rg,
            situacao : situacao,
            turma : turma,
            endereco : endereco, 
            numero : numero,
            bairro : bairro,
            cep :cep,
            cidade: cidade,
            uf : uf,
            email : email,
            telefone : telefone,
            obs : obs,
            
        })

    }).then(function(result){
        return result.json()
    }).then(function(dados){
        if(dados['status'] == '200'){
            console.log('Dados alterado com sucesso')
            location.reload()
        }else{
            console.log('Ocorreu algum erro')
        }

    })

}

function pesquisa_cep(controle) {

    if (controle == '1'){
        var campo = document.getElementById('cep').value;
        console.log(campo);
        //Nova variável "cep" somente com dígitos.
        var cep = campo.replace(/\D/g, '');

        //Verifica se campo cep possui valor informado.
        if (cep != "") {

            //Expressão regular para validar o CEP.
            var validacep = /^[0-9]{8}$/;

            //Valida o formato do CEP.
            if(validacep.test(cep)) {

                //Preenche os campos com "..." enquanto consulta webservice.
                document.getElementById('endereco').value="...";
                document.getElementById('bairro').value="...";
                document.getElementById('cidade').value="...";
                document.getElementById('UF').value="...";
            

                //Cria um elemento javascript.
                var script = document.createElement('script');

                //Sincroniza com o callback.
                script.src = 'https://viacep.com.br/ws/'+ cep + '/json/?callback=meu_callback';

                //Insere script no documento e carrega o conteúdo.
                document.body.appendChild(script);

            } //end if.
            else {
                //cep é inválido.
                limpa_formulário_cep(1);
                alert("Formato de CEP inválido.");
            }
        } //end if.
        else {
            //cep sem valor, limpa formulário.
            limpa_formulário_cep(1);
        }
    }


    if (controle == '2'){
        var campo = document.getElementById('Edit_cep').value;
        console.log(campo);
        //Nova variável "cep" somente com dígitos.
        var cep = campo.replace(/\D/g, '');

        //Verifica se campo cep possui valor informado.
        if (cep != "") {

            //Expressão regular para validar o CEP.
            var validacep = /^[0-9]{8}$/;

            //Valida o formato do CEP.
            if(validacep.test(cep)) {

                //Preenche os campos com "..." enquanto consulta webservice.
                document.getElementById('Edit_endereco').value="...";
                document.getElementById('Edit_bairro').value="...";
                document.getElementById('Edit_cidade').value="...";
                document.getElementById('Edit_UF').value="...";
            

                //Cria um elemento javascript.
                var script = document.createElement('script');

                //Sincroniza com o callback.
                script.src = 'https://viacep.com.br/ws/'+ cep + '/json/?callback=meu_callback2';

                //Insere script no documento e carrega o conteúdo.
                document.body.appendChild(script);

            } //end if.
            else {
                //cep é inválido.
                limpa_formulário_cep(2);
                alert("Formato de CEP inválido.");
            }
        } //end if.
        else {
            //cep sem valor, limpa formulário.
            limpa_formulário_cep(2);
        }
    }
};

function limpa_formulário_cep(tipo) {
    if (tipo == '1'){
    //Limpa valores do formulário de cep.

    
        document.getElementById('endereco').value=("");
        document.getElementById('bairro').value=("");
        document.getElementById('cidade').value=("");
        document.getElementById('UF').value=("");
    }

    if (tipo == '2'){
        //Limpa valores do formulário de cep.
    
        
            document.getElementById('Edit_endereco').value=("");
            document.getElementById('Edit_bairro').value=("");
            document.getElementById('Edit_cidade').value=("");
            document.getElementById('Edit_UF').value=("");
        }
}

function meu_callback(conteudo) {

    if (!("erro" in conteudo)) {
        //Atualiza os campos com os valores.
        document.getElementById('endereco').value=(conteudo.logradouro);
        document.getElementById('bairro').value=(conteudo.bairro);
        document.getElementById('cidade').value=(conteudo.localidade);
        document.getElementById('UF').value=(conteudo.uf);
        
    } //end if.
    else {
        //CEP não Encontrado.
        limpa_formulário_cep(1);
        alert("CEP não encontrado.");
    }
}

function meu_callback2(conteudo) {

    if (!("erro" in conteudo)) {
        //Atualiza os campos com os valores.
        document.getElementById('Edit_endereco').value=(conteudo.logradouro);
        document.getElementById('Edit_bairro').value=(conteudo.bairro);
        document.getElementById('Edit_cidade').value=(conteudo.localidade);
        document.getElementById('Edit_UF').value=(conteudo.uf);
        
    } //end if.
    else {
        //CEP não Encontrado.
        limpa_formulário_cep(2);
        alert("CEP não encontrado.");
    }
}