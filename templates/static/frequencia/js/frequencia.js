function exibe_data(){
    data = document.getElementById('data_aula')
    today = new Date
    data.value = today
    console.log(today)

}

function exibe_turma(){


    turma = document.getElementById('comboTurma')
    data = document.getElementById('data_aula')
    dados =  document.getElementById('exibe_pesquisa')

    dados.style.display = "block"

   
    

}