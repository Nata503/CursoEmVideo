#Crie um programa que leia um número inteiro e mostre na tela
#se ele é par ou impar

n = int(input('Digite seu número: '))
resultado = n % 2
if resultado == 0:
    print('O número {} é par'.format(n))
else:
    print('O número {} é impar'.format(n))
