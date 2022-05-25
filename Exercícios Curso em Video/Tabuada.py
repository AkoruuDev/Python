# ex09
# Exercício da aula de Python - Mundo um (Curso em Video)

# Faça um programa que leia um número inteiro e mostre sua tabuada

n = int(input('Digite um número para ver sua tabuada: '))
i = 1
while i < 11:
    print(f'{n} * {i} = {n*i}')
    i=i+1