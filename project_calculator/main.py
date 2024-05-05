from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calcular_idade', methods=['POST'])
def calcular_idade():
    data_nascimento_string = request.form['data_nascimento']
    data_nascimento = datetime.strptime(data_nascimento_string, "%Y-%m-%d").date()
    data_atual = datetime.now().date()
    diferenca = data_atual - data_nascimento
    idade_anos = diferenca.days // 365
    dias_restantes = diferenca.days % 365
    idade_meses = dias_restantes // 30
    idade_dias = dias_restantes % 30
    return render_template('resultado.html', idade_anos=idade_anos, idade_meses=idade_meses, idade_dias=idade_dias)

if __name__ == '__main__':
    app.run(debug=True)
