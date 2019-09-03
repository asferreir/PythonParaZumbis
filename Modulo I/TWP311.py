
"""
MODO 1
"""
arquivo = open("numeros.txt", "r")
for linha in arquivo.readlines():
    #print(linha)
    print (linha.rstrip())
arquivo.close()



"""
MODO 2
"""
with open("numeros.txt") as f:
    print (f.read())