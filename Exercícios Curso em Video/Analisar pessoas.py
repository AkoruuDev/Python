# ex56
# Exercício da aula de Python - Mundo um (Curso em Video)

# Desenvolva um programa que leia o nome, idade, sexo de 4 pessoas. No final, mostre:
# A media de idade;
# O nome do homem mais velho;
# Quantas mulheres tem menos de 20 anos

tot = 0
comp = 0

for i in range(1, 5):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = int(input('Escolha seu sexo:\n[1] Homem\n[2] Mulher\n'))

    if sexo == 1:
        if idade > comp:
            hvelho = nome
            comp = idade
    else: 
        if 0 < idade < 20:
            tot += 1
    idade += idade

media = idade/4

print(f'A media de idade de todas essas pessoas é {media}')
print(f'{hvelho} é o homem mais velho dentre eles')
print(f'Há {tot} mulheres com menos de 20 anos')