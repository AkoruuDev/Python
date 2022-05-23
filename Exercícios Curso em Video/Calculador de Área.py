# ex11
# Exercício da aula de Python - Mundo um (Curso em Video)

# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tintanecessária para pinta=la, sabendo que cada litro de tinta, pinta uma área de 2m²

h = float(input('Digite a altura da parede em metros: '))
l = float(input('Digite a largura da parede em metros: '))
a = h*l
print(f'Pelas informações passadas, sua parede tem uma área total de {a}m² e será necessário {a/2} litros de tinta para pinta-la')