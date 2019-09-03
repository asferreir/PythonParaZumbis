"""
CALCULO DA SOMA DE DEZ NUMEROS INTEIROS
"""
n =  1
soma = 0
while n <= 10:
    x = int(input("Digite o %d numero: " %n))
    soma = soma + x
    n += 1
print("Soma: %d" %soma)