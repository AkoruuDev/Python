# ex29
# Exercício da aula de Python - Mundo um (Curso em Video)

# Escreva um algorítmo que leia a velocidade de um carro. Se ele passar de 80Km/h, mostre uma mensagem dizendo que ele foi multado e a multa é de R$ 7.00 por cada km acima do limite

vel = int(input('Digite a velocidade do carro: '))
if vel > 80:
    i = float((vel - 80) * 7)
    print(f'Você foi multado!\nDeverá pagar a multa de R$ {i:.2f}')
else:
    print('Boa viagem')
