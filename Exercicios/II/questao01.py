"""
Faça um Programa que peça os três lados de um triângulo. 
O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

CONDICAO DE EXISTENCIA DE UM TRIANGULO
A < B + C
B < A + C
C < A + B
"""

a = int(input("Informe o valor do Lado A: "))
b = int(input("Informe o valor do Lado B: "))
c = int(input("Informe o valor do Lado C: "))
if a > b + c or b > a + c or c > a + b:
    print ("Os lados informados não correspondem a um Triângulo")
elif a == b == c:
    print ("Os lados informados correspondem a um Triângulo Equilátero")
elif a == b or b == c or a == c:
    print ("Os lados informados correspondem a um Triângulo Isósceles")
else:
    print ("Os lados informados correspondem a um Triângulo Escaleno")        