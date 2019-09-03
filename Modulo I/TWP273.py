"""
FAÇA UM PROGRAMA QUE LEIA 4 NOTAS, MOSTRE AS NOTAS E A MEDIA NA TELA
"""

notas = []
cont = 1
while cont <= 4:
    n = float (input("Digite uma Nota: "))
    notas.append(n)
    cont += 1
media = 0
cont = 0
while cont <= 3:
    media += notas[cont]
    cont += 1
print("Notas: ", notas)
print("Media: %4.2f" %(media/4))


"""
OUTRA FORMA DE FAZER O MESMO PROGRAMA
"""
notas = []
media = 0
cont = 1
while cont <= 4:
    n = float (input("Digite uma Nota: "))
    notas.append(n)
    media += n
    cont += 1
print("Notas: ", notas)
print("Media: %4.2f" %(media/4))