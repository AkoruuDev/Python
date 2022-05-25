# ex22
# Exercício da aula de Python - Mundo um (Curso em Video)

# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiusculas
# o nome com todas as letras minusculas
# Quantas letras ao todo sem espaços
# Quantas letras tem o primeiro nome

nome = input('Escreva seu nome completo: ')
big = nome.upper()
short = nome.lower()
qtd = int(len(nome)) - int(nome.count(' '))
fnom = int(len(nome.split()[0]))
print(f'Seu nome em MAIUSCULO é: {big}\nE seu nome em minusculo é: {short}')
print(f'Você tem {qtd} letras no seu nome')
print(f'Seu primeiro nome "{nome.split()[0]}" tem {fnom} letras')