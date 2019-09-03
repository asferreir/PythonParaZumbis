"""
CONSUMINDO DADOS DO TWP352
"""

from TWP352 import Cliente
from TWP352 import Conta

joao = Cliente("Joao da Silva", "777-1234")
maria = Cliente("Maria da Silva", "888-1234")
print("Nome: %s. Telefone: %s." % (joao.nome, joao.telefone))
print("Nome: %s. Telefone: %s." % (maria.nome, maria.telefone))
conta01 = Conta([joao], 1, 1000)
conta02 = Conta([maria], 2, 1500)
conta01.resumo()
conta02.resumo()
