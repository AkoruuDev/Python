# ex01
# Exercício da aula de Python - Mundo um (Curso em Video)

# Crie um pograma que faça o compútador jogar jokenpô com você

from random import randint
from time import sleep

# Seleção aleatória do jokenpo
i = randint(1, 3)
# Nomeando cada seleção
jokenpo = 'PEDRA'
if i == 2:
    jokenpo = 'PAPEL'
elif i == 3:
    jokenpo = 'TESOURA'

# Area visual (1 parte)
print('*-'*20+'*')
print('VAMOS BRINCAR DE JOKENPÔ')
print('*-'*20+'*')
e = int(input('\nFaça sua escolha:\n\n1. PEDRA\n2. PAPEL\n3. TESOURA\n\nOpção: '))

# Nomeando cada escolha
if e == 1:
    esc = 'PEDRA'
elif e == 2:
    esc = 'PAPEL'
else:
    esc = 'TESOURA'

# Calculando vitoria/derrota
status = 'PERDI'
if e == i:
    result = f'\n\nEu escolhi {jokenpo} também\nFoi empate!\n\n'
else:
    if e == 1 and i == 3:
        status = 'PERDI'
    elif e > i:
        status = 'PERDI'
    else:
        status = 'GANHEI'
    result = f'\n\nEu escolhi {jokenpo} e você escolheu {esc}!\nEu {status}\n\n'

# Area visual (2 parte)
print('\nCerto...\nVamos jogar!\n\n')
sleep(2)
print('Jo')
sleep(0.5)
print('ken')
sleep(0.5)
print('pô')
sleep(1)
print(result)