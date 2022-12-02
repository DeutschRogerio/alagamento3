import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

#cur.execute("INSERT INTO TB_PESSOAS  (NOME_PESSOA, TEL_PESSOA) VALUES  ('Rogerio', '11977056659')")

cur.execute("INSERT INTO TB_PESSOAS  (NOME_PESSOA, TEL_PESSOA) VALUES  ('Rogerio', '11977056659')",)
cur.execute("INSERT INTO TB_AREAS  (NOME_AREA, STATUS_AREA) VALUES  ('Lapa', '0')",)
cur.execute("INSERT INTO TB_AREAS  (NOME_AREA, STATUS_AREA) VALUES  ('RLG dias', '0')",)
cur.execute("INSERT INTO TB_AREAS  (NOME_AREA, STATUS_AREA) VALUES  ('SALVE', '0')",)

#cur.execute("UPDATE TB_AREAS  set STATUS_AREA ='1' WHERE NOME_AREA ='Lapa'",)
#cur.execute("SELECT * FROM TB_AREAS WHERE STATUS_AREA ='1'")

connection.commit()
connection.close()