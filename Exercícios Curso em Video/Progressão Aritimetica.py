# ex51
# Exercício da aula de Python - Mundo um (Curso em Video)

# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre na tela os 10 primeiros termos dessa progressão
# (Desafio pessoal) Mostre se a PA é crescente ou decrescente

termo = float(input('Digite o primeiro termo da sua PA: '))
razao = int(input('Digite a razão da sua PA: '))

if razao > 0:
    prog = 'Crescente'
else:
    prog = 'Decrescente'

print('Os próximos 10 termos dessa Progressão Aritimética são:')
t = termo
for i in range(1, 11):
    t = t + razao
    print(t)
print(f'Esta é uma PA {prog} de razão {razao} com o primeiro termo sendo {termo}')