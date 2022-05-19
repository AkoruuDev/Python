# ex40
# Exercício da aula de Python - Mundo um (Curso em Video)

# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# menor que 5: Reprovado;
# Entre 5 e 6.9: Recuperação;
# Maior que 7: Aprovado

nome = str(input('Digite o nome do aluno: '))
not1 = float(input('Digite a primeira nota do aluno: '))
not2 = float(input('Digite a segunda nota do aluno: '))
media = (not1 + not2) / 2
if media < 5:
    status = 'FOI REPROVADO'
elif media < 7:
    status = 'ESTÁ DE RECUPERAÇÃO'
else:
    status = 'FOI APROVADO'
print(f'\nDe acordo com a media atingida, o aluno {nome}:\n{status} com a média de {media}\n')