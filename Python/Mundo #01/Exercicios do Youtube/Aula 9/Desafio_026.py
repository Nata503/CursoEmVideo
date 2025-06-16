#Desafio26
#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra 'A'.
#Em que posição ela aparece a primeira vez

frase = str(input('Digite uma Frase: ').strip().upper())

print('A Letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira Letra A apareceu na posição {}'.format(frase.find('A')+1,))
print('A última Letra A apareceu na posição {}'.format(frase.rfind('A')+1,))