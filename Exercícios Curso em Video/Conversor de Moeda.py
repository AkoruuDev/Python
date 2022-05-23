# ex10
# Exercício da aula de Python - Mundo um (Curso em Video)

# Crie um programa que leia quanto dinheio uma pessoa tem na carteira e mostre quantos dólares ela pode comprar considerando US$ 1.00 == R$ 3.27

carteira = float(input('Quantos reais você tem na sua carteira? R$ '))
print(f'Com R$ {carteira} você pode comprar até US$ {carteira/3.27} considerando que o dólar está a 3.27 atualmente')