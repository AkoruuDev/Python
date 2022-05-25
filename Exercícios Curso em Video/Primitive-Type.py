# ex04
# Exercício da aula de Python - Mundo um (Curso em Video)

# Crie um script que leia algo e mostre seu tipo primitivo e todas as informações possíveis sobre ele

n = input('Digite alguma coisa: ')
print(f'O tipo primitivo do que vc digitou é {type(n)}')
print('°#'*35 + '°')
print('Agora confere aqui embaio algumas outras informações sobre o que você digitou')
print('°#'*35 + '°')
print(f'O que você digitou é um número: {n.isnumeric()}')
print(f'O que você digitou é um texto: {n.isalpha()}')
print(f'O que você digitou é um número ou um texto: {n.isalnum()}')
print(f'O que você digitou está em capslock: {n.isupper()}')
print(f'O que você digitou está em minúsculo: {n.islower()}')
print(f'O que você digitou é só espaços: {n.isspace()}')
print(f'O que você digitou está captalizada: {n.istitle()}')