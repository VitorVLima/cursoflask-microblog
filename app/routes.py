from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    dados = {
        'nome': 'vitor',
        'profissao': 'estudante',
        'idade': 26

    }
    return render_template('index.html', dados = dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')