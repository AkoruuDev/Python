# ex55
# Exercício da aula de Python - Mundo um (Curso em Video)

# Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos

maior = 0
menor = 0

for i in range(1, 6):
    pes = float(input(f'Digite o peso da pessoa {i}: '))
    if maior == 0:
        maior = pes
        menor = pes

    if pes > maior:
        maior = pes
    elif pes < menor:
        menor = pes
        
print(f'O maior peso lido foio de {maior}kg e o menor foi o de {menor}kg')