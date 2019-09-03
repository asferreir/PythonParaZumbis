print ("Bem Vindo!")
chute = 0
while chute != 42:
    g = input("Chute um numero: ")
    chute = int(g)
    if chute == 42:
        print("Voce venceu!")
    else:
        if chute > 42:
            print("Alto")
        else:
            print("Baixo")
print("Fim de Jogo!")