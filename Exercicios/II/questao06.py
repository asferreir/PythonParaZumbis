"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 
11% para o Imposto de Renda, 
8% para o INSS e 
5% para o sindicato, 
faça um programa que nos dê o salário bruto, quanto pagou ao INSS, 
quanto pagou ao sindicato e o salário líquido. 
Observe que Salário Bruto - Descontos = Salário Líquido. 
Calcule os descontos e o salário líquido, conforme a tabela abaixo:
a. + Salário Bruto : R$
b. - IR (11%) : R$
c. - INSS (8%) : R$
d. - Sindicato ( 5%) : R$
e. = Salário Liquido : R$
"""
valor = float(input("Informe quanto voce ganha por hora: "))
horas = int (input("Informe o número de horas trabalhadas no mês: "))
bruto = valor * horas
ir = bruto * 0.11
inss = bruto * 0.08
sind = bruto * 0.05
liquido = bruto - ir - inss - sind
print ('+Salário Bruto:\t\t R$ %10.2f' %bruto)
print ('-IR:\t\t\t R$ %10.2f' %ir)
print ('-INSS:\t\t\t R$ %10.2f' %inss)
print ('-Sindicato:\t\t R$ %10.2f' %sind)
print ('=Salário Líquido:\t R$ %10.2f' %liquido)