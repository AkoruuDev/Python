# ex39
# Exercício da aula de Python - Mundo um (Curso em Video)

# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar no serviço militar;
# Se é hora dele se alistar;
# Se já passou do tempo de alistamento.
# O programa também deverá informar o tempo que falta ou que passou do  prazo de alistamento.

from datetime import date
nasc = date.today().year - int(input('Digite o ano de nascimento: '))
print(f'Você tem {nasc} anos')
if nasc < 18:
    print('Ainda vai se alistar no serviço militar')
    print(f'Anda falta {18 - nasc} anos para o ano de alistamento')
elif nasc == 18:
    print('Este é o ano ideal de alistamento')
else:
    print('Já passou da hora de se alistar no serviço militar')
    print(f'Ao que parece, já se passaram {nasc - 18} anos do ano ideal para alistamento')