#Faça um programa que leia algo pelo teclado e mostre na tela o seu
#primitivo e todas as informações possiveis sobre ele.

n = input("Digite algo: ")
print('O Tipo primitivo desse valor é ',type(n))
print('Só tem espacos? ',n.isspace())
print('È um número? ',n.isalnum())
print('È alfabético? ',n.isalpha())
print('Está em maiúscula? ',n.isupper())
print('Está em minúscula? ',n.islower())
print('Está capitalizada?',n.istitle())

#fazer esse exercicio usando o .format

