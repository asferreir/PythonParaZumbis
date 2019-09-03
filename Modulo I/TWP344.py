"""
FAÇA UM PROGRAMA QUE LEIA O TEXTO ALICE.TXT E CONTE O NUMERO DE OCORRENCIAS DE CADA PALAVRA NO TEXTO.
OBS.: PARA SABER OS CARACTERES ESPECIAIS USE import string e utilize string.punctuation
"""
import string

texto = "Alice foi atras do coelho, mas nao o encontrou"
texto = texto.lower()
print(texto)
#'alice foi atras do coelho, mas nao o encontrou'

texto = texto.replace("," , " " )
print(texto)
#'alice foi atras do coelho  mas nao o encontrou'

texto = texto.split()
print(texto)
#['alice', 'foi', 'atras', 'do', 'coelho', 'mas', 'nao', 'o', 'encontrou']

dic = {}
for p in texto:
    if p not in dic:
        dic[p] = 1
    else:
        dic[p] +=1
print (dic)

texto = "Alice caiu num buraco".split()

dic = {}
for p in texto:
    if p not in dic:
        dic[p] = 1
    else:
        dic[p] +=1
print (dic)