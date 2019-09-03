from random import randint
secreta = randint(1, 100)
while True:
    chute = int(input("Chute: "))
    if chute == secreta:
        print("Parabens. voce é foda! Acerto o numero %d" %chute)
        break
    else:
        print("Alto" if chute > secreta else "Baixo")
print("Fim de Jogo!")
