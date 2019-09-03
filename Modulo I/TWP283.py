"""
FAÇA UM PROGRAMA QUE LEIA UMA PALAVRA E TROQUE AS VOGAIS POR '*'
"""
palavra = input ("Palavra: ") # LER A PALAVRA
p = 0 # CONTADOR
troca = "" # ACUMULADOR

while p < len(palavra): #ENQUANTO P FOR MENOR QUE TAMANHO DE PALAVRA
    if palavra[p] in "aeiou": # SE A PALAVRA DO INDICE P ESTIVER DENTRO DO CONJUNTO "aeiou"
        troca = troca + "*" 
    else:
        troca = troca + palavra[p]
    p += 1

print("Nova palavra %s" %troca)