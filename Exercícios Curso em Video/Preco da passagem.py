# ex28
# Exercício da aula de Python - Mundo um (Curso em Video)

# Desenvolva um programa que leia a distância de uma viagem em Km. Calcule o preço da passagem colocando R$ 0.50 por Km em viagens até 200Km e R$ 0.45 para viagens mais longas

km = int(input('Digite a distancia em KM da viagem: '))
if km > 200:
    pkm = 0.45
else:
    pkm = 0.50
passagem = pkm * km
print(f'Sua viagem é de {km} Km e o valor da passagem é de R$ {passagem:.2f}')