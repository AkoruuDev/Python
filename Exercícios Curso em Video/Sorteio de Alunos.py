# ex19
# Exercício da aula de Python - Mundo um (Curso em Video)

# Um professor quer sortear um dos quatro alunos para apagar o quadro. Faça um programa que o ajude lendo o nome deles e escrevendo o nome escolhido.

import random
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
e = random.choice([a1, a2, a3, a4])
print(f'Dos alunos que escolheu, o escolhido para apagar o quadro negro é {e}')