'''
Título: Cotação do dólar
Autor: Letícia Nascimento
Data: 19/09/2024
Descrição: Realizar um algoritmo que realize a conversão do dólar pra o real e mostre isso ao usuário
'''

real = float(input("Informe quanto gostaria de converter de R$ para $: "))
dolar = 5.00

conversao = real / dolar

print(f"Você terá ${conversao}, pois a cotação atual é de R${dolar}")