# ex012
# Exercício da aula de Python - Mundo um (Curso em Video)

# Faça um algorítimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
# (Desafio pessoal) Ofereça a possibilidade de oferecer o desconto ou não
# (Desafio pessoal) Ofereça a quantidade de desconto que o produto vai ter

produto = float(input('Digite o valor do produto: '))
d = input('Oferecer desconto? (s/n): ')
if d == 's':
    desc = (float(input('Quanto de desconto você gostaria de dar? (sem o sinal de %) ')))/100
    produto = produto-(produto*desc)
print(f'O valor final do produto é de R$ {produto}')