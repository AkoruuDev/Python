# ex01
# Exercício da aula de Python - Mundo um (Curso em Video)

# Desenvolva uma lógica que leia o peso e a altura de uma pessoa e calcule seu IMC e mostre seu status de acordo com a tabela abaixo:
# Menor que 18.5 - abaixo do peso;
# Entre 18.6 e 25.0 - Peso ideal;
# Entre 25.1 e 30 - Sobrepeso;
# Entre 30.1 e 40 - Obesidade;
# Acima de 40 - Obesidade Mórbida

peso = float(input('Digite o peso: '))
alt = float(input('Digite a altura: '))
imc = peso / (alt * alt)

if imc < 18.5:
    status = 'ABAIXO DO PESO'
elif imc < 25:
    status = 'COM O PESO IDEAL'
elif imc < 30:
    status = 'COM SOBREPESO'
elif imc < 40:
    status = 'COM OBESIDADE'
else:
    status = 'COM OBESIDADE MÓRBIDA'

print(f'De acordo com seu peso e sua altura, pelo calculo do IMC, você está {status}')