# ex38
# Exercício da aula de Python - Mundo um (Curso em Video)

# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela quem é o maior e o menor ou se eles são valores iguais

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
if n1 == n2:
    print('Os dois valores escolhidos são iguais')
else:
    if n1 > n2:
        maior = n1
        menor = n2
    else:
        maior = n2
        menor = n1
    print(f'Dos números que você escolheu, o numero {maior} é o maior e, consequentemente, o {menor} é o menor')