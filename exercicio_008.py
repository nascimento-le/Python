#Exercício: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metro = int(input("Digite o valor do metro: "))

cm = metro * 100
mm = metro * 1000

print("O valor do metro é igual a {} centímetros e {} milímetros.".format(cm,mm))

