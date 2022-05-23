# ex36
# Exercício da aula de Python - Mundo um (Curso em Video)

# Escreva um programa de aprovação de emprestimo bancario. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado.
# (Desafio Pessoal) Caso o emprestimo seja negado, dê uma sugestão de acordo para que o valor ainda permaneça o mínimo possível para que seja aprovado

print('*-'*28+'*')
print('Bem vindo ao Emprestimo Aqui, faça seu empréstmo conosco!')
print('*-'*28+'*\n\n')
valor = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o salário do comprador: R$ '))
anos = int(input('Digite a quantidade de anos para pagamento: '))
meses = int(input('Digite a quantidade de meses para pagamento: '))
entrada = float(input('Digite o valor da entrada: R$ '))
tempo = (anos*12) + meses
ex = salario*(30/100)
prestacao = (valor - entrada) / tempo

if prestacao > ex:
    print(f'Infelizmente seu emprestimo não foi aceito\nO motivo disso é que no tempo de {tempo} meses, haveriam parcelas de R$ {prestacao:.2f} que acabam excedendo o valor mínimo de 30% do seu salário que era no valor de R$ {ex:.2f}')
else:
    print(f'Perfeito!\nSeu emprestimo para a casa no valor de R$ {valor:.2f} foi aprovada com sucesso\n\nVeja abaixo algumas infomrações:\nO valor total da casa é de R$ {valor:.2f}\nO valor de entrada foi de R$ {entrada:.2f}\nO pagamento foi dividido em {tempo} vezes\nO valor das parcelas serão de R$ {prestacao:.2f}')