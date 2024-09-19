from flask import Flask, render_template, request, redirect, url_for
from database import criar_tabelas, adicionar_caso, buscar_casos
from models import Caso

app = Flask(__name__)

@app.route('/')
def index():
    casos = buscar_casos()
    return render_template('index.html', casos=casos)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    numero = request.form.get('numero')
    cliente = request.form.get('cliente')
    data_abertura = request.form.get('data_abertura')
    status = request.form.get('status')
    descricao = request.form.get('descricao')
    advogado = request.form.get('advogado')
    
    if numero and cliente and data_abertura and status and advogado:
        novo_caso = Caso(numero, cliente, data_abertura, status, descricao, advogado)
        adicionar_caso(novo_caso)
    
    return redirect(url_for('index'))

@app.route('/relatorio')
def relatorio():
    casos = buscar_casos()
    return render_template('report.html', casos=casos)

if __name__ == '__main__':
    criar_tabelas()
    app.run(debug=True)
