'''
Título: Calcula média
Autor: Letícia Nascimento
Data: 19/09/2024
Descrição: Desenvolver um algoritmo que calcula a média de 4 notas e apresenta para o usuário a média entre elas
'''
# cometário seleciono o texto e ctrl+;

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
nota4 = float(input("Informe a quarta nota: "))

soma = nota1 + nota2 + nota3 + nota4    
media = soma/4


print(f"A média das notas é: {media}")