#Faça um programa que leia o comprimento do cateto oposto e do
#cateto adjacente de um triângulo retângulo, calcule e mostre
#o comprimento da hipotenusa

from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi = hypot(co, ca)

print('O cateto oposto {}  e o cateto adjacente {} tem sua hipotenusa igual á {:.2f}'.format(co,ca,hi))