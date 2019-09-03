"""
CONSUMINDO DADOS DE UM DB SQLITE3 V2
"""

import sqlite3
banco = sqlite3.connect("surfersDB.sdb")
banco.row_factory = sqlite3.Row
cursor = banco.cursor()
# cursor.execute("""SELECT name, average FROM surfers where age > 20 order by average desc""")
linhas = cursor.fetchall()
for linha in linhas:
    print("Nome     :", linha["name"])
    print("Média    :", linha["average"])
cursor.close()
