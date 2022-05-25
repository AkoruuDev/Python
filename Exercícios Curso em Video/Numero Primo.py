# ex52
# Exercício da aula de Python - Mundo um (Curso em Video)

# Faça um programa que leia um numero inteiro e diga se ele é primo

num = int(input('Digite um número: '))
for i in range(2, num):
    if num % i == 0:
        status = 'NÃO É'
        break
    else:
        status = 'É'
print(f'O número {num} que você escolheu {status} um número primo')