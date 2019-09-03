"""
CALCULE A MEDIA DE 10 NUMEROS INTEIROS
"""
n = 1
soma = 0
while n <= 10:
    x = int(input("Digite o %d numero: " %n))
    soma = soma + x
    n = n + 1
print ("Media: %5.2f" %(soma/10)) # %5.2f (5 POSIÇÕES NO FLOAT, SENDO 2 DEPOIS DO PONTO) 