"""
VARIAVEIS LOCAIS E GLOBAIS

"""

#EX 01
a = 5
def muda_e_imprime():
        a = 7
        print("A dentro da função: %d" %a)
print ("A antes de mudar: %d" %a)
muda_e_imprime()
print("A depois de mudar: %d" %a)

"""
#EX 02
a = 5
def muda_e_imprime():
        global a
        print("A dentro da função: %d" %a)
print ("A antes de mudar: %d" %a)
muda_e_imprime()
print("A depois de mudar: %d" %a)
"""