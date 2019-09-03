"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""
a = int (input("Informe um numero A: "))
b = int (input("Informe um numero B: "))
c = int (input("Informe um numero C: "))

if a >= b and a >= c:
    print("O numero %d é o maior" %a)
elif b >= c:
    print("O numero %d é o maior" %b)
else:
    print("O numero %d é o maior" %c)

if a <= b and a <= c:
    print("O numero %d é o maior" %a)
elif b <= c:
    print("O numero %d é o maior" %b)
else:
    print("O numero %d é o maior" %c)