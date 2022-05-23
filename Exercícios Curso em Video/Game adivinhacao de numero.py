# ex28
# Exercício da aula de Python - Mundo um (Curso em Video)

# Crie um algorítmo que o computador "pense" em um número qualquer entre 1 e 5 para o usuário tentar adivinhar e mostre na tela se ele acertou ou errou o numero
# (Desafio pessoal) Dê a opção pro usuário colocar um número limite para o Chute
# (Desafio pessoal) Faça o programa em Loop para o usuário ir chutando e recebendo dicas (é maior ou menor) até acertar e mostre no fim quantas tentativas ele precisou até acertar
# (Desafio pessoal) Coloque dinamismo e cores para deixar mais divertido

import random
from time import sleep
cores = {
    'Limpar':'\33[m',
    'dicas':'\33[4;1;33m',
    'separacao':'\33[1;32m',
    'titulos':'\33[4;31m'
}
sep = '=*'*19+'='
print('{}{}{}'.format(cores['separacao'], sep, cores['Limpar']))
n = int(input('{}Vamos Brincar!{}\nQual é o número limite pra eu pensar? '.format(cores['titulos'], cores['Limpar'])))
x = random.randint(1, n)
sleep(1)
print('{}{}{}'.format(cores['separacao'], sep, cores['Limpar']))
print('Beleza!\nDeixa eu pensar aqui em um número...')
sleep(2)
y = int(input('{}Certo!{} Pensei em um número aqui entre {}1{} e {}{}{}. Tenta Adivinhar\n{}Eu pensei no número:{} '.format(cores['titulos'], cores['Limpar'], cores['dicas'], cores['Limpar'], cores['dicas'], n, cores['Limpar'], cores['titulos'], cores['Limpar'])))
tentativas = 1
while y != x:
    tentativas = tentativas + 1
    if y < x:
        status = '{}MAIOR{}'.format(cores['dicas'], cores['Limpar'])
    else:
        status = '{}MENOR{}'.format(cores['dicas'], cores['Limpar'])
    print(f'Você quase acertou, mas eu pensei em um numero {status}')
    print('{}{}{}'.format(cores['separacao'], sep, cores['Limpar']))
    y = int(input('Vamos tentar de novo\n{}Eu pensei no número:{} '.format(cores['titulos'], cores['Limpar'])))
print(f'PARABÉNS!\nEu realmente pensei no número {x}, que nem você falou.\nVocê usou {tentativas} tentativas para acertar, mas conseguiu!')