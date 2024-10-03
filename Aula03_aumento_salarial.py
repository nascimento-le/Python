'''
Título: Aumento Salarial
Autor: Letícia Nascimento
Data 24/09/24 
Descrição: Faça um programa que receba o salário de um funcionário, calcule e mostre o novo
salário, sabendo-se que este sofreu um aumento de 25%.
'''

salario_atual = float(input("Informe o salário atual do funcionário: R$ "))

adicional = salario_atual * 0.25
novo_salario = salario_atual + adicional

print(f"O novo salário do funcionário deverá ser: R$ {novo_salario}")