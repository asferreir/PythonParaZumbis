# REVISAO
"""
V1
f = open("surf.txt")
for linha in f:
    print(linha.strip())
f.close()
"""

"""
V2

f = open("surf.txt")
maior = 0
for linha in f:
    nome, pontos = linha.split()
    if float(pontos) > maior:
        maior = float(pontos)
f.close()
print(maior)
"""

"""
V3

f = open("surf.txt")
primeiro = 0
segundo = 0
terceiro = 0
maior = 0
for linha in f:
    nome, pontos = linha.split()
    if float(pontos) > primeiro:
        terceiro = segundo
        segundo = primeiro
        primeiro = float(pontos)
    elif float(pontos) > segundo:
        terceiro = segundo
        segundo = float(pontos)
    elif float(pontos) > terceiro:
        terceiro = float(pontos)
f.close()
print(primeiro)
print(segundo)
print(terceiro)
"""

"""
V4
"""
f = open("surf.txt")
notas = []
for linha in f:
    nome, pontos = linha.split()
    notas.append(float(pontos))
f.close()
print(notas[0])
print(notas[1])
print(notas[2])
