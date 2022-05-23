# ex44
# Exercício da aula de Python - Mundo um (Curso em Video)

# Elabore um programa que calcule o valor a ser pago por um produto considerando seu valor e a forma de pagamento:
# A vista dinheiro / Cheque - 10% de desconto;
# A vista no cartão - 5% de desconto;
# Até 2x no cartão - Preço normal;
# 3x ou mais no cartão - 20% de juros

produto = float(input('Digite o valor do produto: R$ '))
pag = int(input('\nEscolha a forma de Pagamento:\n1. A vista dinheiro / cheque\n2. A vista no cartão\n3. Até 2x no cartão\n4. acima de 3x no cartão\nOpção: '))
if pag == 1:
    total = produto - (produto*(10/100))
if pag == 2:
    total = produto - (produto*(5/100))
if pag == 3:
    total = produto
if pag == 4:
    total = produto + (produto*(20/100))
print(f'Parabéns pela Compra!\n\nDevido à forma de pagamento escolhida, seu produto no valor de R$ {produto:.2f} foi reajustado para o valor de R$ {total:.2f}\n\nVolte Sempre!')