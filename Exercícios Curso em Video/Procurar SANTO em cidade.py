# ex24
# Exercício da aula de Python - Mundo um (Curso em Video)

# Crie um programa que leia o nome de uma cidade e diga se ela começa com o nome SANTO

city = input('Digite o nome da cidade: ').strip()
cort = city.split()
ajuste = cort[0].upper()
if ajuste == 'SANTO':
    print(f'A cidade de {city} COMEÇA com o nome "santo"')
else:
    print(f'A cidade de {city} NÃO COMEÇA com o nome "santo"')