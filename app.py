from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return "Rota index."

@app.route('/hello', methods=['GET'])
#def hello_world():
#    return "<p>Hello, World!</p>"
def hello():
    name = request.args.get("name", "Flask")
    return f"Hello, {escape(name)}!"    

@app.route("/about")
def about():
    return "Sobre a aplicação."

@app.route("/teste", methods=["GET", "POST"])
def teste():
    if request.method == "POST":
        return "Você enviou um POST! (Dados processados)"
    return "Você enviou um GET! (Página visualizada)"

@app.route("/usuarios/<nome_usuario>")
def perfil(nome_usuario): 
    return f"Olá, {nome_usuario}! Este é o seu perfil." 

@app.route("/soma/<int:n1>/<int:n2>")
def somar(n1, n2):
    resultado = n1 + n2
    return f"A soma de {n1} + {n2} é igual a: {resultado}"

@app.route("/pagamento/<any(cartao, boleto, pix):metodo>")
def processar_pagamento(metodo):
    return f"Processando pagamento via {metodo}"

@app.route('/user/<username>')
def profile(username):
    return f"Perfil de {username}"

@app.route('/user/admin')
def admin():
    return "Área do Administrador"

@app.route("/rastrear")
def rastrear():
    info = {
        "ip_do_usuario": request.remote_addr,
        "metodo": request.method,
        "caminho": request.path,
        "navegador": request.user_agent.string
    }
    return info

@app.route("/livros")
def livros():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return "sobre"

@app.route("/livros/<int:id_livro>")
def id_livro(id_livro):
    return f"o id do livro é {id_livro}"

@app.route("/generos/<any(romance,comedia,terror):genero>")
def genero_livro(genero):
    return f"o genero do livro é {genero.capitalize()}" #capitalize upper 1 letra

@app.route("/string")
def query_string():
    termo = request.args.get('teste', default ="Nada")  
    return f"Você buscou por: {termo}" 


if __name__ == '__main__':
    print("Servidor Flask rodando em http://localhost:5000")
    app.run(debug=True, port=5000)
