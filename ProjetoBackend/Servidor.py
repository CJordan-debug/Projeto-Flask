from flask import Flask, request, jsonify
from Persistencia.JogadorBD import JogadorBD
from Modelo.Jogador import Jogador
from flask_basicauth import BasicAuth 

app = Flask(__name__)

app.secret_key = 'A0B1C2D34E4F5G6H7I8J9'
app.config['BASIC_AUTH_USERNAME'] = 'Carlos'
app.config['BASIC_AUTH_PASSWORD'] = '123456'

basic_auth = BasicAuth(app)

#parâmetro id é do tipo inteiro
#exemplo: http://endereçoServidor/jogador/10

@app.route("/jogadores", methods=["GET","POST","PUT","DELETE"])
@app.route("/jogadores/<int:id>", methods=["GET","POST","PUT","DELETE"])
@basic_auth.required
def jogador(id=None):
    if request.method == "GET":
        jogadorBD = JogadorBD()
        jogadores = []
        if id: # recebemos um id?
            jogador = jogadorBD.consultar(id)
            if jogador: 
                jogadores.append(jogador)
        else:
            jogadores = jogadorBD.consultar("")
        return jsonify([jogador.toJson() for jogador in jogadores])
        

    elif request.method == "POST":
        if id:
            return {"status" : "Método POST não permitido para /" + str(id)}
        else:
            if request.is_json:
                dados = request.get_json()
                pNome     = dados.get("nome")
                pDataNasc = dados.get("dataNasc")
                pApelido  = dados.get("apelido")
                jogador = Jogador(id=0,nome=pNome,dataNasc=pDataNasc,apelido=pApelido,bibliotecaJogos=[])
                jogadorBD = JogadorBD()
                jogadorBD.incluir(jogador)
                return {"id": jogador.id}
            else:
                return {"status":"O servidor aceita apenas dados no formato JSON."}

    elif request.method == "PUT":
        if id:
           if request.is_json:
               #transformação de JSON para dicionário Python via get_json()
               dados = request.get_json()
               nome     = dados.get("nome")
               dataNasc = dados.get("dataNasc")
               apelido  = dados.get("apelido")
               if (nome and dataNasc and apelido):
                   jogador = Jogador(id=id, nome=nome, dataNasc=dataNasc, apelido=apelido)
                   jogadorBD = JogadorBD()
                   jogadorBD.atualizar(jogador)
                   return {"status":True}
               else:
                   return {"status":"Especifique o nome, a dataNasc e o apelido!"}
           else:
               return {"status":"Somente o formato JSON é aceito pelo servidor!"} 
        else:
            return {"status":"Especifique o id do recurso que deseja atualizar!"}
    elif request.method == "DELETE":
        if id:
            jogadorBD = JogadorBD()
            jogador = jogadorBD.consultar(id)
            if jogador:
                jogadorBD.apagar(jogador)
                return {"status":True}
            else:
                return {"status":"Jogador não encontrado no servidor!"}
        else:
            return {"status":"Especifique o id na url!"}
    else:
        pass


app.run('0.0.0.0', port=5000)