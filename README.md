para realizar o uso correto do codigo e doacesso ao bando evitando assim erros
primeira mente deveremos intalar o Python https://www.python.org/downloads/

logo em seguida o conector do MySQL
abrindo o CMD e digtando o seguinte comando:  pip install mysql-connector-python
apos isso ele ira instalar o conector do mysql evitando que o codigo apresente erros

deveremos ter instalado tambem o WAMPServer
https://wampserver.aviatechno.net/files/install/wampserver3.3.5_x64.exe
apos instalado inicie normalmente tento em mente que o icone deve estar verde na barra de tarefas,
apos isso va até seu navegador e na barra de pesquisa digite "localhost"
e em Seus Aliases, selecione o PhpMyAdmin 5.2.1, clique em banco de dados, depois na aba SQL
crie um database com nome PDV digitando o comando 'create database PDV;'
feito isso selecione o banco de dados PDV e importe mo arquivo PDV.sql  na aba import

apos intalado os dois configure da mesma forma que se encontra no banco,
tendo como nome de usuario para acesso ao banco seja "ROOT" e a senha padrao "mysql23"
feito isso so importar o banco "PDV.sql" que se encontra dentro do codigo
para fazer a importação, depois de instalado o mysql workbench, abra ele e clique na aba "server" que se encontra na barra superior do programa
clique na opçao "data import", e selecione a opçao "import from self-container file"
selecione o caminho onde  foi alocado seu codigo e selecione o arquivo "PDV.sql"
feito isso clique em "star import" e pronto.


caso o sistema não esteja conectando corretamente, deve ser instalada a dependência pip install --upgrade mysql-connector-python



