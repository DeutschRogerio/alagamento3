#from flask import Flask, render_template,flash
from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3

app = Flask(__name__, template_folder='static')

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/teste1")
def index():
  return render_template('Cadastro_incidente.html')

@app.route("/teste2")
def cadastro_incidentes():
  return render_template('Cadastro_pessoa.html')


@app.route('/teste4')
def testeinsert():
    conn = get_db_connection()
    pessoas = conn.execute('SELECT * FROM TB_PESSOAS').fetchall()
    conn.close()
    return render_template('33.html', pessoas=pessoas)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        nome_pessoa = request.form['nome_pessoa']
        tel_pessoa = request.form['tel_pessoa']

        if not nome_pessoa:
            flash('Title is required!')
        elif not tel_pessoa:
            flash('Content is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (nome_pessoa, tel_pessoa)')
            conn.commit()
            conn.close()
            return redirect(url_for('testeinsert'))

    return render_template('Cadastro_pessoa.html')



if __name__ == "__main__":
 app.run()
