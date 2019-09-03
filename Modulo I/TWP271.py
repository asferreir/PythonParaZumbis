"""
FAÇA UM PROGRAMA QUE LEIA UM VETOR DE 5 NUMEROS INTEIROS E MOSTRE O VETOR
"""

vetor = []
cont = 1
while cont <= 5:
    n = int (input("Digite um numero: "))
    vetor.append(n)
    cont += 1
print("Vetor lido:", vetor )