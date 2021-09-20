#Exercício: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#cotação do dólar. 19/09/2021 - R$5,29

valor_carteira = float(input("Digite quantos reais tem na sua carteira: R$"))
dolar = valor_carteira / 5.29

print("Com R${:.2f} você poderá comprar US${:.2f}".format(valor_carteira,dolar))

