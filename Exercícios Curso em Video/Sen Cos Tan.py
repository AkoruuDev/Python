# ex18
# Exercício da aula de Python - Mundo um (Curso em Video)

# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse âgulo.

import math as m
ang = float(input('Digite um angulo qualquer: '))
sen = float(m.sin(ang))
cos = float(m.cos(ang))
tan = float(m.tan(ang))
print(f'No angulo {ang} que você escolheu, seu seno é {sen}, o cosseno é {cos} e sua tangênte recebe o valor de {tan}')