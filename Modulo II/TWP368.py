import random
numeroAleatorio = random.randint(1, 100)
chute = 0
while chute != numeroAleatorio:
    g = input("Chute um numero: ")
    chute = int(g)
    if chute == numeroAleatorio:
        print("Voce venceu!")
    else:
        if chute > numeroAleatorio:
            print("Alto")
        else:
            print("Baixo")
print("Fim de Jogo!")
