"""
DEFINA UMA FUNCAO "EMBARALHA" QUE RETORNE AS LETRAS DE UMA STRING MISTURADAS.
DICA: UTILIZE LIST() PARA CONVERTER SUAS STRING EM LISTA
"""
def embaralha (s):
    import random
    lista = list(s)
    random.shuffle(lista)
    return "".join(lista)