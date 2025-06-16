#Crie um programa que leia um número Real qualquer pelo teclado
#e mostre na tela a sua porção inteira
#Ex: Digite um número: 6.127
#O número 6.127 tem a parte inteira 6

from math import floor
num = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num,floor(num)))

#podemos usar o math.trunc() no .format porem quando importamos
#usando o from usamos o modulo somente com o nome dele trunc()
#caso usemos o import math, precisamos colocar math na frente
#math.trunc()

#num = float(input('Digite um valor: '))
#print('O valor digitado foi {} e a sua porção inteira é {}'.format(num,int(num)))