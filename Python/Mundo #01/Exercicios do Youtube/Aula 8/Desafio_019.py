#Um professor quer sortear um dos seus quatros alunos para apagar
#o quadro. Faça um programa que ajude ele, lendo o nome deles e
#escrevendo o nome do escolhido

from random import choice

num1 = str(input('Digite um nome: '))
num2 = str(input('Digite um nome: '))
num3 = str(input('Digite um nome: '))
num4 = str(input('Digite um nome: '))

nomes = [num1,num2,num3,num4]

escolhido = choice(nomes)

print('O Aluno escolhido foi {}'.format(escolhido))
