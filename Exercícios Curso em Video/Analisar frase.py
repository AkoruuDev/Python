# ex26
# Exercício da aula de Python - Mundo um (Curso em Video)

# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra A
# Em qual posição aparece a primeira vez a letra A
# Em qual posição aparece a ultima vez a letra A

fras = input('Digite qualquer coisa: ').strip()
frase = fras.lower()
lettera = frase.count('a')
firsta = frase.find('a')
lasta = frase.rfind('a')
print(f'A frase que você digitou foi: "{fras}".\nVamos analisar?')
print('=='*10)
print(f'A letra "a" aparece {lettera} vezes na frase que você digitou')
print(f'A letra "a" aparece pela primeira vez na posição {firsta + 1}')
print(f'A Letra "a" aparece pela última vez na posição {lasta + 1} da sua frase')
