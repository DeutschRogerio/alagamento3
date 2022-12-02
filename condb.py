import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO TB_PESSOAS  (NOME_PESSOA, TEL_PESSOA) VALUES  ('Rogerio', '11977056659')",  
           
            )

cur.execute("INSERT INTO TB_PESSOAS  (NOME_PESSOA, TEL_PESSOA) VALUES  ('Rogerio', '11977056659')",  
            )

connection.commit()
connection.close()