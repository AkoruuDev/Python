# ex53
# Exercício da aula de Python - Mundo um (Curso em Video)

# Crie um programa que leia uma frase qualquer e diga se é um palindromo

phrase = str(input('Digite uma frase qualquer: ')).replace(' ', '').lower()

startbegin = 0
backbegin = len(phrase)-1
b = phrase[startbegin]
e = phrase[backbegin]

if b != e:
    status = 'NÃO É'
else:
    for i in range(1, backbegin):
        if b != e:
            status = 'NÃO É'
            break
        else:
            status = 'É'
        startbegin += 1
        backbegin -= 1
    
print(f'Essa frase {status} um palindromo')