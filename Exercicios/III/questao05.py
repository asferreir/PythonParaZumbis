"""
Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o algoritmo de Euclides.
Ex:. mdc (21, 15) = 3
"""
a = int(input ("Informe o valor de A: "))
b = int(input ("Informe o valor de B: "))

while a % b != 0:
    a, b = b, a % b
print ("O MDC é = %d" %b)