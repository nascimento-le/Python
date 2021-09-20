#Exercício: Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor.

num = int(input("Digite um número: "))

antes = num - 1
depois = num + 1

print("Você digitou o número {}, sendo seu antecessor {} e o seu sucessor {}.".format(num,antes,depois))