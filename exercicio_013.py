#Exercício: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salarioAntigo = float(input("Digite o salário do funcionário: "))
aumento = salarioAntigo * 0.15
salarioNovo = salarioAntigo + aumento

print("O novo salário desse funcionário é R${:.2f}, sendo R${:.2f} de aumento.".format(salarioNovo,aumento))