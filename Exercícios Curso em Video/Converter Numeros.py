# ex37
# Exercício da aula de Python - Mundo um (Curso em Video)

# Escreva um programa que leia um número inteiro qualquer e peça apra o usuário escolher qual será a base de conversão:
# 1. Binário
# 2. Octal
# 3. Hexadecimal

num = int(input('Digite um numero inteiro: '))
choise = int(input('\nQual será a base de conversão?\n(Digite apenas o numero de escolha)\n\n1. Binário\n2. Octal\n3. Hexadecimal\nOpção: '))
if choise == 1:
    conv = bin(num)
elif choise == 2:
    conv = oct(num)
else:
    conv = hex(num)
print(f'\nO numero {num} que você escolheu foi convertido para a opção {choise} e é apresentado da seguinte maneira: {conv[2::]}')