from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ
# make_response pacote para lidar com as respostas em python
# SQLAlchemy p trabalhar com tabelas e banco de dados
# environ p trabalhar com variáveis de ambiente
# flask p criar api e aplicação web
# jsonify p trabalhar com dados em formato json
# request (SEM 'S') é para requisicões http 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL') # CONEXÃO COM O BANCO DE DADOS
db = SQLAlchemy(app) # sqlalchemy vai conseguir trabalhar com o app

# se a variável de ambiente DB_URL não estiver configurada, o app não vai funcionar
if not app.config['SQLALCHEMY_DATABASE_URI']:
    raise RuntimeError("A variável de ambiente 'DB_URL' não está configurada.")

class User(db.Model): # criando uma tabela para os usuários
    __tablename__ = 'usuarios' # nome da tabela

    id = db.Column(db.Integer, primary_key=True) # id do usuário
    usuario = db.Column(db.String(80), unique=True, nullable=False) # nome do usuário (não pode ser nulo e tem que ser único)
    email = db.Column(db.String(120), unique=True, nullable=False) # email do usuário (não pode ser nulo e tem que ser único)

    def json(self):
        return {'id': self.id, 'usuario': self.usuario, 'email': self.email} # retorna os dados do usuário em formato json

with app.app_context(): # cria um contexto para o app, para poder usar o banco de dados
    db.create_all() # inicia o database

# ROTA TESTE
@app.route('/teste', methods=['GET']) # não precisa especificar o método, mas é bom para deixar claro o que a rota faz
def teste():
    return make_response(jsonify({'mensagem': 'rota de teste'}), 200) # retorna em json com o status 200 (ok)

# CRIANDO USUÁRIO
@app.route('/create-usuarios', methods=['POST']) # rota para criar um usuário, usando o método POST
def criar_usuario():
    try:
        dados = request.get_json() # pega os dados do usuário em formato json
        # verifica se os dados estão corretos
        if not dados or 'usuario' not in dados or 'email' not in dados: 
            return make_response(jsonify({'mensagem': 'dados inválidos ou incompletos'}), 400)
        # se os dados estiverem corretos, cria o usuário
        novo_usuario = User(usuario=dados['usuario'], email=dados['email']) # cria um novo usuário em formato json com os dados: usuario e email
        db.session.add(novo_usuario) # adiciona o usuário ao banco de dados
        db.session.commit() # salva as alterações no banco de dados
        return make_response(jsonify({'mensagem': 'usuário criado com sucesso', 'user': novo_usuario.json()}), 201) # retorna em json com o status 201 (criado)
    except Exception as e: # caso de erro
        # caso não seja erro de dados inválidos, retorna erro 500
        print(e) # mostra o erro
        return make_response(jsonify({'mensagem': 'erro ao criar usuário'}), 500)

# PEGANDO TODOS OS USUÁRIOS
@app.route('/get-usuarios', methods=['GET']) # rota para pegar todos os usuários, usando o método GET
def pegar_usuarios():
    try:
        usuarios = User.query.all() # pega todos os usuários do banco de dados
        # verifica se a lista está vazia
        if not usuarios: # se não tiver nenhum usuário
            return make_response(jsonify({'mensagem': 'Nenhum usuário encontrado'}), 204)
        return make_response(jsonify({'usuarios': [usuario.json() for usuario in usuarios]}), 200) # retorna em json com o status 200 (ok)
    except Exception as e: # caso de erro
        print(e) # mostra o erro
        return make_response(jsonify({'mensagem': 'erro ao pegar usuários'}), 500)
    
# PEGANDO USUÁRIO PELO ID
@app.route('/read-usuarios/<int:id>', methods=['GET']) # rota para pegar um usuário pelo id, usando o método GET
def pegar_usuario(id):
    try:
        usuario = User.query.filter_by(id=id).first() # pega UM usuário pelo id 
        # verificando se o usuário existe antes de retornar
        if usuario:
            return make_response(jsonify({'usuario': usuario.json()}), 200) # retorna o usuário em json com o status 200 (ok)
        return make_response(jsonify({'mensagem': 'usuário não encontrado'}), 404) # se o usuário não for encontrado, retorna erro 404 (não encontrado)
    except Exception as e: # caso de erro
            print(e) # mostra o erro
            return make_response(jsonify({'mensagem': 'erro ao pegar usuário'}), 500)

# ATUALIZANDO USUÁRIO
@app.route('/update-usuarios/<int:id>', methods=['PUT']) # rota para atualizar um usuário pelo id, usando o método PUT
def atualizar_usuario(id):
    try:
        usuario = User.query.filter_by(id=id).first()
        if usuario:
            dados = request.get_json() # pega os dados do usuário em formato json
            usuario.usuario = dados['usuario'] # atualiza o nome do usuário
            usuario.email = dados['email'] # atualiza o email do usuário
            db.session.commit() # salva as alterações no banco de dados
            return make_response(jsonify({'mensagem': 'usuário atualizado com sucesso', 'user': usuario.json()}), 200) # retorna em json com o status 200 (ok)
        return make_response(jsonify({'mensagem': 'usuário não encontrado'}), 404) # se o usuário não for encontrado, retorna erro 404 (não encontrado)
    except Exception as e:
        print(e) # mostra o erro
        return make_response(jsonify({'mensagem': 'erro ao atualizar usuário'}), 500)
    
# # DELETANDO USUÁRIO
# @app.route('/delete-usuarios/<int:id>', methods=['DELETE']) # rota para deletar um usuário pelo id, usando o método DELETE
# def deletar_usuario(id):
#     try:
#         usuario = User.query.filter_by(id=id).first() # pega o usuário pelo id
#         if usuario:
#             db.session.delete(usuario) # deleta o usuário
#             db.session.commit() # salva as alterações no banco de dados
#             return make_response(jsonify({'mensagem': 'usuário deletado com sucesso'}), 200) # retorna em json com o status 200 (ok)
#         return make_response(jsonify({'mensagem': 'usuário não encontrado'}), 404) # se o usuário não for encontrado, retorna erro 404 (não encontrado)
#     except Exception as e:
#         print(e)
#         return make_response(jsonify({'mensagem': 'erro ao deletar usuário'}), 500)
    
