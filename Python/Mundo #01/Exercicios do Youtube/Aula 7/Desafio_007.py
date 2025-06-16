#Desafio 007 = Desenvolva um programa que leia as duas
#notas de um aluno, calcula e mostre a sua média.

nota1 = int(input('Digite sua primeira nota: '))
nota2 = int(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
print('Com base na suas notas {:.1f} e {:.1f}, a média é {:.1f}!'.format(nota1, nota2,media))