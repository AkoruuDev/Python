# ex54
# Exercício da aula de Python - Mundo um (Curso em Video)

# Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas delas ainda não atingiram a maioridade e quantas já são maiores

from datetime import date

maior = 0
menor = 0

for i in range(1, 8):
    ano = int(input(f'Digite o ano de nascimendo da pessoa {i}: ')[:4])
    
    while ano > date.today().year:
        ano = int(input(f'Ano inválido, por favor, adicione mais uma vez a idade da pessoa {i}')[:4])
    
    if (date.today().year - ano) > 17:
        maior += 1
    else:
        menor += 1

print(f'{maior} pessoas já atingiram a maioridade\n{menor} pessoas ainda não atingiram a maioridade')
