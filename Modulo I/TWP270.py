"""
CALCULE A MEDIA DE 5 NOTAS
"""

notas = [5, 6, 7, 8, 9]
cont = 1
media = 0
while cont < 5:
    media += notas[cont]
    cont += 1
print ("Media: %5.2f" %(media/cont))