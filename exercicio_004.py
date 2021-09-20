#Exercício: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e as informações possíveis sobre ela

x = input("Digite algo: ")

print("É um número?", x.isnumeric())
print("Está escrito em letras maiúsculas?",x.isupper())
print("Está escrito em letras minúsculas?",x.islower())
print("É capitalizada?",x.istitle())
