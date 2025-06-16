#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
#Para salário superiores a R$1.250,00 Calcule um aumento de 10%
#Para salário inferiores ou iguais o aumento é de 15%

n = float(input('por gentileza, poderia informar seu salário: R$'))
if n <= 1250:
    aumento = n * 0.15
else:
    aumento = n * 0.10

salario_final = n + aumento
print('Com base no seu salário base, com o novo aumento ficaria R${:.2f} reais'.format(salario_final))