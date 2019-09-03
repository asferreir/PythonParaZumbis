"""
CONSUMINDO DADOS DO TWP353_1
"""

from TWP355_1 import Cliente
from TWP355_1 import Conta, ContaEspecial

joao = Cliente("Joao da Silva", "777-1234")
maria = Cliente("Maria da Silva", "888-1234")
print("Nome: %s. Telefone: %s." % (joao.nome, joao.telefone))
print("Nome: %s. Telefone: %s." % (maria.nome, maria.telefone))
conta01 = Conta([joao], 1, 1000)
conta02 = ContaEspecial([maria, joao], 2, 500, 1000)
conta01.saque(50)
conta02.deposito(300)
conta01.saque(190)
conta02.deposito(95.15)
conta02.saque(1500)
conta01.extrato()
conta02.extrato()
