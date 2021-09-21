#Exercício: Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

Celsius = float(input("Digite a temperatura em ºC: "))
Fahrenheit = 9 * Celsius / 5 + 32

print("{}ºC equivale a {}ºF.".format(Celsius,Fahrenheit))