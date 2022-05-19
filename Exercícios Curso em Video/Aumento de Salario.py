# ex34
# Exercício da aula de Python - Mundo um (Curso em Video)

# Faça um algorítmo que leia o salário de um funcionário e mostre pra ele seu aumento. Se for maior que R$ 1250.00, um aumento de 10%, se for menor ou igual, um aumento de 15%.

salario = float(input('Digite seu salário: '))
if salario < 1250.00:
    val = 15
else:
    val = 10
aumento = salario*(val/100)
print(f'Parabéns pelo seu aumento! Agora como aumento de {val}%, seu salário ajustado é de R$ {salario+aumento:.2f}')