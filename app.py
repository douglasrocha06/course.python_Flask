from flask import Flask, jsonify, request
import json

app = Flask(__name__)

#Criando um biblioteca de desenvolvedores e suas habilidades
desenvolvedores = [
    {
        'id': 0,
        'nome':'Douglas',
        'habilidades':['Python', 'Flask']
    },

    {
        'id':1,
        'nome':'Jose',
        'habilidade':['Python','Django']
    }
]
#RETORNA um desenvolvedor pelo ID, e também ALTERA e DELETA um desenvolvedor
@app.route('/dev/<int:id>', methods=['GET','PUT','DELETE']) 
def desenvolvedor(id):
    if request.method == 'GET':
        try: 
            response = desenvolvedores[id]
        except IndexError: 
            mensagem = 'Desenvolvedor de ID {} não existe.'.format(id)
            response = {'status':'404', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API' 
            response = {'status':'404', 'mensagem':mensagem}
        return jsonify(response) 

    elif request.method == 'PUT': 
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        print(dados)
        return jsonify("Alteração realizada com sucesso",dados)
          
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'200', 'Mensagem':'Registro excluído com sucesso.'})

#Lista TODOS os desenvolvedores e permite CRIAR um novo desenvolvedor 
@app.route('/dev/', methods=['POST','GET'])
def lista_desenvolvedores():

    if request.method == 'POST':
        dados = json.loads(request.data) 
        posicao = len(desenvolvedores) 
        dados['id'] = posicao 
        desenvolvedores.append(dados) 
        return jsonify(desenvolvedores[posicao])

    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__== '__main__':
    app.run(debug=True)