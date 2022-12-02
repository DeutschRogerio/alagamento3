#from flask import Flask, render_template,flash
from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3

app = Flask(__name__, template_folder='static')

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/reportar")
def reportar():
    print("teste")
    #conn = get_db_connection()
    #area_interesse  = conn.execute("UPDATE TB_AREAS  set STATUS_AREA ='1' WHERE NOME_AREA =?",
    #(area_interesse))
    #conn.close()
    #return render_template('incidentecomsql.html',area_interesse=area_interesse)



@app.route("/cadastro_incidente", methods=('GET', 'POST'))
def cadastro_incidente():
    conn = get_db_connection()
    area_interesse  = conn.execute('SELECT * FROM TB_AREAS').fetchall()
    conn.close()
    #reportar()
    return render_template('incidentecomsql.html',area_interesse=area_interesse)
    

    

@app.route("/teste2")
def cadastro_incidentes():
  return render_template('Cadastro_pessoa.html')


@app.route('/teste4')
def testeinsert():
    conn = get_db_connection()
    nome_pessoa = conn.execute('SELECT * FROM TB_PESSOAS').fetchall()
    area_interesse  = conn.execute('SELECT * FROM TB_AREAS').fetchall()
    conn.close()
    return render_template('33.html', nome_pessoa=nome_pessoa,area_interesse=area_interesse) 

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        Riquelme = request.form['Riquelme']
        tel_pessoa = request.form['tel_pessoa' ]

        if not Riquelme:
            flash('Nome é obrigatório!')
            
        elif not tel_pessoa:
            flash('telefone é obrigatório!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO TB_PESSOAS (NOME_PESSOA, TEL_PESSOA) VALUES (?, ?)',
            (Riquelme,tel_pessoa))
            conn.commit()
            conn.close()
            return redirect(url_for('testeinsert'))

    return render_template('Cadastro_pessoa.html')



if __name__ == "__main__":
 app.run()
