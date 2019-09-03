import sqlite3
"""
CRIANDO BANCO

import sqlite3

con = sqlite3.connect("alunos.bd")
cur = con.cursor()
cur.execute("CREATE TABLE ALUNOS(LOGIN VARCHAR(8), RA INTEGER)")
cur.close()
con.close()
"""
"""
INSERINDO INFORMAÇÃO NO BANCO
"""

con = sqlite3.connect("alunos.bd")
cur = con.cursor()
cur.execute('INSERT INTO ALUNOS VALUES ("masarori", 42)')
cur.execute('INSERT INTO ALUNOS VALUES ("emengarda", 666)')
cur.execute("SELECT * FROM ALUNOS")
for x in cur.fetchall():
    print(x)
cur.close()
con.commit()
con.close()
