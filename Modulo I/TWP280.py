"""
FATIAMENTO

FATIA DO PRIMEIRO INDICE ATE O ANTERIOR DO SEGUNDO
"""

x = "0123456789"
print(x[0:2])
print(x[1:2])
print(x[2:4])
print(x[0:5])
print(x[1:8])
"""
PODEMOS OMITIR INDICES, SUBSTITUINDO PELO EXTREMO CORRESPONDENTE E TBM PODEMOS 
TER INDICES NEGATIVOS: -1 (ULTIMO), -2 (PENULTIMO) 
"""

print(x[:2])
print(x[4:])
print(x[4:-1])
print(x[-4: -1])
print(x[:])

"""
INCREMENTO NO FATIAMENTO
POSSO USAR UM INCREMENTO AO FATIR A STRING
"""
texto = "batatinha quando nasce"
print (texto [::2])
print (texto[::-1])