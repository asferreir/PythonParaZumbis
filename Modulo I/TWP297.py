"""
GERE UMA LISTA DE 15 INTEIROS ALEATORIOS ENTRE 10 E 100
"""

import random
lista = []
for k in range(15):
    lista.append(random.randint(10, 100))
print(lista)


