"""
Determine se um ano é bissexto. Verifique no Google como fazer isso...

DEFINICAO ANO BISSEXTO
- DIVISIVEL 4 (% 4 == 0)
- NAO PODE SER DIVISIVEL POR 100 (% 100 != 0)
- NAO PODE SER DIVISIVEL POR 400 (% 400 == 0)

"""
ano = int(input("Informe o ano (ex. 1999): "))
if ano % 4 == 0 and (ano % 400 == 0 or ano % 100 != 0):
    print("Ano Bissexto")
else:
    print("Ano não é Bissexto")
    