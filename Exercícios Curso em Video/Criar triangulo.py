# ex01
# Exercício da aula de Python - Mundo um (Curso em Video)

# Faça um programa que leia o comprimento de de três retas e diga se pode ou não montar um triângulo

reta1 = int(input('Digite a primeira reta: '))
reta2 = int(input('Digite a segunda reta: '))
reta3 = int(input('Digite a terceira reta: '))
if reta1 > reta2:
    if reta1 < reta3:
        soma = reta1 + reta2
        maior = reta3
    else:
        maior = reta1
        soma = reta2 + reta3
else:
    if reta2 < reta3:
        soma = reta1 + reta2
        maior = reta3
    else:
        maior = reta2
        soma = reta1 + reta3
if soma > maior:
    print('Dá pra fazer um triângulo')
else:
    print('Não dá pra fazer um triangulo')
