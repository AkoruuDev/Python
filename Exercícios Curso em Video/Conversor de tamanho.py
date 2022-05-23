# ex08
# Exercício da aula de Python - Mundo um (Curso em Video)

# Excreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros

distancia = float(input('Digite uma distancia em métros: '))
centimetros = distancia * 1000
milimetros = centimetros * 1000
print(f'A distancia que você digitou é de {distancia} metros.\nIsso dá {centimetros} centímetros e {milimetros} milímetros')