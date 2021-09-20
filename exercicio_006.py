#Exercício: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input("Digite um número: "))

dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)

print("Você digitou o número {}.\n" 
      "O Dobro desse número é {}.\n"
      "O Triplo desse número é {}.\n" 
      "E a Raiz quadrada desse número é {:.2f}".format(num,dobro,triplo,raiz))

