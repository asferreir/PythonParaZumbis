"""
GERE UMA LISTA DE 15 INTEIROS ALEATORIOS ENTRE 10 E 100 QUE SEJAM DISTINTOS ENTRE SI
"""

import random
lista = []
while len(lista) < 15:
    x = random.randint(10, 100)
    if x not in lista:
        lista.append(x)
lista.sort()
print (lista)