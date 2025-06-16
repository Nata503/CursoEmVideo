#Faça um programa que leia um ano
#qualquer e mostre se ela é bissexto

from datetime import date
ano = int(input('Digite um ano (Caso coloque 0 iremos analisar o ano atual): '))
bissexto = ano / 4
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#if bissexto % 4 == 0:
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))

