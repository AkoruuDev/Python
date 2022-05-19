# ex32
# Exercício da aula de Python - Mundo um (Curso em Video)

# Crie um programa que leia um ano qualquer e diga se esse ano é bissexto

ano = int(input('Digite um ano qualquer: '))
if ano % 4 == 0:
    res = 'É'
else:
    res = 'NÃO É'
print(f'O ano {ano} que você escolheu {res} um ano bissexto')