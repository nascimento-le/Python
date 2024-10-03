'''
Título: Conversão de Unidades
Autor: Letícia Nascimento
Data: 24/09/2024
Descrição: Faça um programa que recebe um número em Pés, faça as conversões a seguir e
mostre os resultados.   
    Sabemos que:
    1 Pé = 12 polegadas;
    1 Jarda = 3 Pés;
    1 Milha = 1.760 Jarda;
'''
num_pes = int(input("Informe um número em Pés para conversão: "))

polegadas = num_pes * 12
jardas = num_pes / 3
milha = jardas / 1760

print(f"O resultado é: \n Polegadas: {polegadas} \n Jardas: {jardas} \n Milhas: {milha}")
