# ex48
# Exercício da aula de Python - Mundo um (Curso em Video)

# Faça um programa que calcule a soma de todos os números ímpares que são multiplos de 3 entre 1 e 500

soma = 0
cont = 0
for i in range(1,501, 2):
    if i % 3 == 0:
        soma += i
        cont += 1
print(f'A soma de {cont} numeros é de: {soma}')