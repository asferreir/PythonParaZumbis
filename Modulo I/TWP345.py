"""
FAÇA UM PROGRAMA QUE LEIA O TEXTO ALICE.TXT E CONTE O NUMERO DE OCORRENCIAS DE CADA PALAVRA NO TEXTO.
OBS.: PARA SABER OS CARACTERES ESPECIAIS USE import string e utilize string.punctuation
"""

arq = open("alice.txt", encoding="utf-8")
texto = arq.read()
texto = texto.lower()
import string
for c in string.punctuation:
    texto = texto.replace(c, " ")
texto = texto.split()

dic = {}
for p in texto:
    if p not in dic:
        dic[p] = 1
    else:
        dic[p] += 1

print ("Alice aparece %s vezes" %dic["alice"])
arq.close()