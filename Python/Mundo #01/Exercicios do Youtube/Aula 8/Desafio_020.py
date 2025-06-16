#O mesmo professor do desafio anterior, quer sortear a ordem
#da apresentação de trabalhos dos alunos. Faça um programa que
#leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle
nom1 = str(input('Digite o nome: '))
nom2 = str(input('Digite o nome: '))
nom3 = str(input('Digite o nome: '))
nom4 = str(input('Digite o nome: '))

nomes = [nom1,nom2,nom3,nom4]
shuffle(nomes)

print('A ordem doe apresentação será {}'.format(nomes))