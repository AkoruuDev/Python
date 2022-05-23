# ex17
# Exercício da aula de Python - Mundo um (Curso em Video)


import math
oposto = float(input('Digite o comprimento do cateto oposto desse triangulo: '))
adjacente = float(input('Digite o comprimento do cateto adjacente desse triangulo: '))
hip = float(math.hypot(oposto, adjacente))
print(f'Para o triangulo com o cateto oposto comprindo {oposto} e com o adjacente comprindo {adjacente} tem a hipotenusa com o comprimento de {hip}')