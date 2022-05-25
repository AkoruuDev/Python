# ex15
# Exercício da aula de Python - Mundo um (Curso em Video)

# Crie um programa que leia a quatidade de Km rodado por um carro alugado e a quantidade de dias que ele foi alugado. Considere R$60.00 por dia e R$0.15 por Km rodado

km = float(input('Digite quantos quilômetros foram rodados: '))
d = int(input('Digite quantos dias o carro ficou com você: '))
vkm = km*0.15
vd = d*60
p = vkm + vd
print (f'Você rodou {km}km durante o período de {d} dias.\no valor total a ser pago é de R$ {p}')