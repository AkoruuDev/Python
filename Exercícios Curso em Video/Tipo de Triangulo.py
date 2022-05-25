# ex42
# Exercício da aula de Python - Mundo um (Curso em Video)

# Refaça o exercício 035 acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero - Todos os lados iguais;
# Isósceles - Apenas dois lados iguais;
# Escaleno - Nenhum lado igual

reta1 = int(input('Digite a primeira reta: '))
reta2 = int(input('Digite a segunda reta: '))
reta3 = int(input('Digite a terceira reta: '))
maior = reta1
soma = reta2 + reta3

if reta2 > reta3 and reta2 > reta1:
    maior = reta2
    soma = reta1 + reta3
elif reta3 > reta2 and reta3 > reta1:
    maior = reta3
    soma = reta1 + reta2

if maior < soma:
    if reta1 == reta2 and reta1 == reta3:
        tipo = 'EQUILÁTERO'
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        tipo = 'ISÓSCELES'
    else:
        tipo = 'ESCALENO'
    print(f'Dá pra fazer um triângulo do tipo {tipo}')
else:
    print('Não dá pra fazer um triangulo com essas retas')