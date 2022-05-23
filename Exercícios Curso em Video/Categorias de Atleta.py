# ex41
# Exercício da aula de Python - Mundo um (Curso em Video)

# A Confederação Nascional de Natação prescisa de um programa que leia o ano de nascimeno de um atleta e mostre sua categoria de acordo com sua idade:
# Até 9 anos: Mirim;
# Até 14 anos: Infantil;
# Até 19 anos: Junior;
# Até 20 anos: Senior;
# Acima de 20 anos: Master

from datetime import date
nome = str(input('Digite o nome do camarada: '))
age = date.today().year - int(input('Digite o ano de nascimento do nadador: '))
if age < 10:
    status = 'MIRIM'
elif age < 15:
    status = 'INFANTIL'
elif age < 20:
    status = 'SENIOR'
else:
    status = 'MASTER'
print(f'Bem vindx {nome}\nSua categoria é: {status}')