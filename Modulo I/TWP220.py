"""
IMPRIMIR OS NUMEROS PARES ENTRE 0 E 1 NUMERO FORNECIDO USANDO IF
"""
fim = int(input ("Digite o ultimo numero: "))
x = 1
while x <= fim:
    if x % 2 == 0:
        print(x)
    x = x + 1