"""
VERIFIQUE SE UMA PALAVRA É PALINDROME (EX. ARARA)
"""

palavra = input ("Palavra: ")
if palavra == palavra[::-1]:
    print("%s é palindrome" %palavra)
else:
    print("%s não é palindrome" %palavra)