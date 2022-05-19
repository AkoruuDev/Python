from time import sleep
import os

horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
sec = int(input('Segundos: '))
tempo = int(sec + (minutos * 60) + (horas * (60 * 60)))
os.system('cls')

while tempo >= 0:
    if sec == -1:
        if minutos > 0:
            minutos -= 1
            sec = 59
        else:
            if horas > 0:
                horas -= 1
                minutos = 59
                sec = 59
        
    horas = str(horas).rjust(2, '0')
    minutos = str(minutos).rjust(2, '0')
    sec = str(sec).rjust(2, '0')

    print(f'Contador em: {horas}:{minutos}:{sec}')
    sleep(1)
    os.system('cls')

    sec = int(sec) - 1
    minutos = int(minutos)
    horas = int(horas)

    tempo -= 1