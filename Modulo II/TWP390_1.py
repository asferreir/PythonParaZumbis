import urllib.request
import time
opcao = input("Deseja comprar ja? (S/N)")
if opcao == "S":
        pagina = urllib.request.urlopen(
            "http://beans.itcarlow.ie/prices-loyalty.html")
        texto = pagina.read().decode("utf8")
        onde = texto.find(">$")
        inicio = onde + 2
        fim = inicio + 4
        preco = float(texto[inicio:fim])
        print("Comprar! Preço: %5.2f" % preco)
else:
    preco = 99.99
    while preco >= 4.74:
        pagina = urllib.request.urlopen(
            "http://beans.itcarlow.ie/prices-loyalty.html")
        texto = pagina.read().decode("utf8")
        onde = texto.find(">$")
        inicio = onde + 2
        fim = inicio + 4
        preco = float(texto[inicio:fim])
        if preco >= 4.74:
            time.sleep(600)
    print("Comprar! Preço: %5.2f" % preco)
