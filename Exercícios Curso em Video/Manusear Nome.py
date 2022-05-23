# ex026
# Exercício da aula de Python - Mundo um (Curso em Video)

# Faça um programa que leia o nome inteiro de uma pessoa e mostre na tela o primeiro e o ultimo nome separadamente

nome = input('Digite seu nome inteiro: ')
cort = nome.split()
spaces = nome.count(' ')
fnom = cort[0]
lnom = cort[spaces]
print(f'Seu nome completo é: {nome}')
print(f'Seu primeiro nome é: {fnom}')
print(f'Seu último nome é: {lnom}')