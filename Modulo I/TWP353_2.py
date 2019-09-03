"""
CONSUMINDO DADOS DO TWP353_1
"""

from TWP353_1 import Cliente
from TWP353_1 import Conta

joao = Cliente("Joao da Silva", "777-1234")
maria = Cliente("Maria da Silva", "888-1234")
print("Nome: %s. Telefone: %s." % (joao.nome, joao.telefone))
print("Nome: %s. Telefone: %s." % (maria.nome, maria.telefone))
conta01 = Conta([joao], 1, 1000)
conta02 = Conta([maria], 2, 1500)
conta01.saque(50)
conta01.saque(175)
conta02.saque(100)
conta02.saque(350)
conta02.deposito(3000)
conta01.deposito(1500)
conta01.extrato()
conta02.extrato()
