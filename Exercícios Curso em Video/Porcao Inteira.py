# ex16
# Exercício da aula de Python - Mundo um (Curso em Video)

# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porção inteira.
# Ex: Digite um número: '6.897'
#                       O número 6.897 tem a porção inteira 6.

import math
num = float(input('Digite um numero real: '))
i = math.trunc(num)
print(f'O numero que você digitou foi {num} e a porção inteira desse numero é {i}')