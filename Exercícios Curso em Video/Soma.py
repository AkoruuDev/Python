# ex03
# Exercício da aula de Python - Mundo um (Curso em Video)

# Crie um script que leia dois numeros e mostre a soma entre eles

n1 = input('Digite um número: ')
while n1.isnumeric() == False:
    n1 = input('Acho que digitou alguma coisa errada, tente denovo.\nColoque um número inteiro: ')
n1 = int(n1)
n2 = input('Digite outro número: ')
while n2.isnumeric() == False:
    n2 = input('Acho que digitou alguma coisa errada, tente denovo.\nColoque um número inteiro: ')
n2 = int(n2)
soma = n1 + n2
print(f'A soma de {n1} e {n2} é de {soma}')