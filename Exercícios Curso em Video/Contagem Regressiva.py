# ex46
# Exercício da aula de Python - Mundo um (Curso em Video)

# Faça um programa que mostre na tela uma contagem regresiva para o estouro dos fogos de artifício, indo de 10 à 0 com uma pausa de 1 segundos entre eles

# +----------------------------------------------------+
# |                   IMPORTAÇÕES                      |
# +----------------------------------------------------+
from time import sleep
from random import randint

# +----------------------------------------------------+
# |                    CABEÇALHO                       |
# +----------------------------------------------------+
print('\33[1;32m=*' * 15 + '=\33[m')
print('\33[31mUm novo ano, uma nova história!\33[m\n')
print('Dê enter para começar o programa')
print('\33[1;32m=*' * 15 + '=\33[m')
enter = input()

# +----------------------------------------------------+
# |                    CONTADOR                        |
# +----------------------------------------------------+
for i in range(10, 0, -1): # Contador de 10 à 0
    sleep(1) # Pausa de 1sec
    c = randint(30, 37) # Escolha de cores gerada aleatóriamente
    print('\33[{}m{}\33[m'.format(c, i))

# +----------------------------------------------------+
# |                     RODAPÉ                         |
# +----------------------------------------------------+
sleep(1)
print('\33[1;34m=*' * 15 + '=\33[m')
print('\n\t\33[4;31mFeliz ano novo!\33[m\n')
print('\33[1;34m=*' * 15 + '=\33[m')
