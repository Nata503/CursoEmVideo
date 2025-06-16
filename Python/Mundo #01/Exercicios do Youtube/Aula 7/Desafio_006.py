#Desafio 006 = Crie um algoritmo que leia um número
#mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite seu número: '))
d = n * 2
t = n * 3
rq = n ** (1/2)
print('O Número {} tem seu dobro {}, o seu triplo {} e sua raiz quadrada {:.2f}.'.format(n,d,t,rq))