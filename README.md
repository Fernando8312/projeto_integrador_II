# projeto_integrador_II
Projeto Integrador II da UNIVESP

O tema do seu Projeto Integrador (PI) neste semestre é: : Desenvolver um software com framework web que utilize banco de dados, inclua script web (Javascript), nuvem, uso de API, acessibilidade, controle de versão e testes. Opcionalmente, incluir análise de dados.

Nesse semestre optamos por desenvolver uma aplicação que auxilia a gestão de uma escola de HandBall. 

Para executar o projeto em sua maquina local:
1 - Tenha o Python instalado
2 - Clone esse repositório
3 - Crie um ambiente virtual - instruções
4 - Instale as dependências - requirements.txt
5 - Rode as migrações

Exemplo:
git clone https://github.com/Fernando8312/projeto_integrador_II.git
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
