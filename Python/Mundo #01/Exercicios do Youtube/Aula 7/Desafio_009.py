#Desafio 009 = Faça um programa que leia um número
#inteiro qualquer e mostre na tela sua tabuada

#n = int(input('Digite um número: '))
#tabuada = n * 1, n * 2, n * 3, n * 4, n * 5, n * 6, n * 7, n * 8, n * 9, n * 10
#print('A tabuada do número {} é {}'.format(n,tabuada))

num = int(input('Digite um número para ver sua tabuada: '))
print('-' * 11)
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10,num*10))
print('-' * 11)