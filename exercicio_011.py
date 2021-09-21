#Exercício: Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta
#necessária para pintá-la. Sabendo que cada litro de tinta pinta uma área de 2m².

largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))

area = largura * altura
tinta = area / 2

print("Para pintar essa parede você precisará de {}l de tinta, pois a área a ser pintada é de {}m².".format(tinta,area))
