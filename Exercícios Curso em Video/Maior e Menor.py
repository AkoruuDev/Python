# ex33
# Exercício da aula de Python - Mundo um (Curso em Video)

# Faça um programa que leia três numeros e mostre na tela o maior e o menor

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
if n1 > n2:
    if n1 < n3:
        maior = n3
        menor = n2
    else:
        maior = n1
        if n2 > n3:
            menor = n3
        else:
            menor = n2
else:
    if n2 < n3:
        maior = n3
        menor = n1
    else:
        maior = n2
        if n1 > n3:
            menor = n3
        else:
            menor = n1
print(f'Dos três numeros que você escolheu, o {maior} é o maior e o {menor} é o menor')
