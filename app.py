from flask import Flask, render_template

app = Flask(__name__, template_folder='static')

@app.route("/teste1")
def index():
  return render_template('Cadastro_incidente.html')

@app.route("/teste2")
def cadastro_incidentes():
  return render_template('Cadastro_pessoa.html')


if __name__ == "__main__":
 app.run()

