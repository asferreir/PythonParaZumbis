"""
FAÇA UM PROGRAMA QUE LEIA UM VETOR DE 10 NUMEROS REAIS E MOSTRE-OS NA ORDEM INVERSA DIGITADA
"""

vetor = []
cont = 1
while cont <= 10:
    n = float (input("Digite um numero: "))
    vetor.append(n)
    cont += 1
cont = 9
while cont >= 0:
    print (vetor[cont])
    cont -= 1