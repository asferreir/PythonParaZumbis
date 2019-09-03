"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações.
"""
usuario = input("Informe o usuario: ")
senha = input("Informe a senha: ")
while usuario == senha:
    print("Usuario e senha devem ser diferentes!")
    usuario = input("Informe o usuario: ")
    senha = input("Informe a senha: ")