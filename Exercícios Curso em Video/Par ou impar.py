# ex30
# Exercício da aula de Python - Mundo um (Curso em Video)

# Crie um programa que leia um número inteiro qualquer e diga se é impar ou par

num = int(input('Digite um numero inteiro qualquer: '))
if num % 2 == 0:
    p = 'PAR'
else:
    p = 'IMPAR'
print(f'O numero {num} que você escolheu é {p}')