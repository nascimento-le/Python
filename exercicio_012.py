#Exercício: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

preco = float(input("Digite o valor do produto: "))
desconto = preco - (preco * 0.05)

print("O valor a ser pago é R${:.2f}, já está com o desconto aplicado.".format(desconto))