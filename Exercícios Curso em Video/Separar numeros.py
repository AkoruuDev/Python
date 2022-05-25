# ex23
# Exercício da aula de Python - Mundo um (Curso em Video)

# Faça um programa que leia um número de 0 à 9999 e mostre na tela cada um dos dígitos separados (milhar, centena, dezena, unidade)

n = int(input('Digite um número inteiro de qualquer entre 0 e 9999: '))
while n < 0 and n > 9999:
    n = int(input('Digitou um número inválido\nDigite um número inteiro de qualquer entre 0 e 9999: '))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'O número que você escolheu foi: {n}\n')
print(f'Milhar: {m}')
print(f'Centena: {c}')
print(f'Dezena: {d}')
print(f'Unidade: {u}')
