from flask import Flask, request
from cadastraUsuario import insertUsuario

app = Flask("Server")

@app.route("/hello", methods=["GET"])
def hello():
    return {"app": "Hello World"}

@app.route("/cadastra/usuario", methods=["POST"])
def cadastra():
    body = request.get_json()

    if("nome" not in body):
        return {"status": 400, "info": "O parâmetro nome é obrigatório"}
    
    usuario = insertUsuario(body["nome"], body["email"], body["senha"])

    return usuario

app.run()

