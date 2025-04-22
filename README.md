# CP2-Flask
Segundo Check Point da disciplina Architecture Analytics And NoSQL na FIAP.

Enunciado:

1) Criar um Dockerfile para a aplicação Flask:

**Crie um arquivo chamado Dockerfile para construir a imagem Docker da aplicação Flask.
A imagem deverá ser baseada na imagem oficial do Python.
O Dockerfile deve instalar o Flask, SQLAlchemy e a biblioteca psycopg2 para conexão com o banco de dados PostgreSQL.
O Dockerfile deve definir a variável de ambiente FLASK_APP e o comando para iniciar a aplicação (flask run).
----------------------------------------------------------------------------------------------------------------**********-----------
2)Criar a aplicação Flask com SQLAlchemy:

Crie um arquivo chamado app.py que implementa uma aplicação Flask simples com SQLAlchemy.
A aplicação deve ter uma rota / que insira um novo usuário no banco de dados e outra rota /users que retorne todos os usuários armazenados.
A aplicação deve se conectar ao banco de dados PostgreSQL e armazenar os usuários com um modelo simples que contenha id, name e email.

---------------------------------------------------------------------------------------------------------------------------
3) Criar um docker-compose.yml para orquestrar os containers:

Crie um arquivo docker-compose.yml para orquestrar a aplicação e o banco de dados.
O arquivo docker-compose.yml deve definir dois serviços:
app: O serviço que rodará a aplicação Flask.
db: O serviço que rodará o banco de dados PostgreSQL.
Defina a rede entre os containers para permitir a comunicação entre o container da aplicação e o do banco de dados.
Utilize variáveis de ambiente no docker-compose.yml para configurar a conexão com o banco de dados (por exemplo, POSTGRES_USER, POSTGRES_PASSWORD e POSTGRES_DB).

----------------------------------------------------------------------------------------------------------------------------
4)Criar o banco de dados PostgreSQL: ( CRUD)

Configure o banco de dados PostgreSQL para inicializar automaticamente com uma tabela chamada users que tenha as colunas id, name e email.
Utilize um script SQL para criar essa tabela ou configure a aplicação para criá-la automaticamente ao ser iniciada.

----------------------------------------------------------------------------------------------------------------------------
5)Construir e rodar os containers:

Utilize o comando docker-compose build para construir os containers.
Após a construção, utilize docker-compose up para iniciar a aplicação e o banco de dados.
A aplicação Flask deve ser acessível na URL http://localhost:5000.

----------------------------------------------------------------------------------------------------------------------------
6) Testar a aplicação:

Abra o navegador e acesse http://localhost:5000/users. Isso deverá retornar uma lista de usuários armazenados no banco de dados.
Utilize uma ferramenta como o Postman ou cURL para enviar uma requisição POST para http://localhost:5000/ com um payload JSON que contenha o nome e o email de um novo usuário. Após a requisição, o novo usuário deve ser adicionado ao banco de dados e aparecer na lista retornada pela rota /users.
----------------------------------------------------------------------------------------------------------------------------
Dicas:
Docker e Docker Compose devem estar instalados em sua máquina.

Criar os seguintes arquivos:
Dockerfile (com a configuração da aplicação Flask).
app.py (com a aplicação Flask e a integração com o banco de dados PostgreSQL).
docker-compose.yml (para orquestrar a aplicação e o banco de dados).
Script SQL para criar a tabela ou configuração automática da tabela no banco.
