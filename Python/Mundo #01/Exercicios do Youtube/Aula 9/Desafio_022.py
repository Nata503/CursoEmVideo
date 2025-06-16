#Desafio22
#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas as letras minúsculas
#Quantas Letras tem o seu nome(Sem contar Espaços)

nome = str(input('Digite seu nome: ')).strip()
print('O seu nome em maiúsculo fica assim:{}'.format(nome.upper()))
print('O seu nome em minúsculo fica assim:{}'.format(nome.lower()))
print('O seu nome contém {} Letras'.format(len(nome)-nome.count(' ')))
#print('O seu Primeiro nome {} contém {} Letras'.format(nome, nome.find(' ')))
separa = nome.split()
print('O seu Primeiro nome {} contém {} Letras'.format(separa[0], len(separa[0])))