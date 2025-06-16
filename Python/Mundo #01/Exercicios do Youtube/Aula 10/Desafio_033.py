#Faça um programa que leia 3 números e
#mostre qual é o maior e qual é o menos

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

maior = n1 if n1 > n2 else n2
menor = n1 if n1 < n2 else n2
maior = n3 if n3 > maior else maior
menor = n3 if n3 < menor else menor

#menor = a
#if b < a and b < c:
    #menor = b
#if c < a and c < b:
    #menor = c
#maior = a
#if b > a and b > c:
    #maior = b
#if c > a and c > b:
    #maior = c
print('O maior número é {} e o menor é {}'.format(maior, menor))