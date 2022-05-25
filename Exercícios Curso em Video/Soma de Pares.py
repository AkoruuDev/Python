# ex50
# Exercício da aula de Python - Mundo um (Curso em Video)

# Desenvolva um programa que leia seis numeros inteiros e mostre a soma daqueles que forem par

s = 0
for i in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s = s + n
print(f'A soma dos númers pares apresentado é: {s}')