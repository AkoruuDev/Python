# ex25
# Exercício da aula de Python - Mundo um (Curso em Video)

# Leia o nome de uma pessoa e diga se ela tem o nome SILVA no nome

nome = input('Escreva seu nome aqui: ').strip()
ajuste = nome.upper()
silva = ajuste.find('SILVA')
if silva != -1:
    print('Seu nome TEM o nome Silva')
else:
    print('Seu nome NÃO TEM o nome Silva')