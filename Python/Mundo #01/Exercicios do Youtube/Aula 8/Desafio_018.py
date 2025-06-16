#Faça um programa que leia um ângulo qualquer e mostre na tela o
#valor do seno, cosseno e tangente desse ângulo

import math
an = float(input('Digite o Angulo: '))
rad = math.radians(an)

sen = math.sin(rad)
cos = math.cos(rad)
tang = math.tan(rad)

print('O ângulo de {:.1f} tem o SENO de {:.2f}'.format(an,sen))
print("O ângulo de {:.1f} tem o COSSENO de {:.2f}".format(an,cos))
print("O ângulo de {:.1f} tem a TANGENTE de {:.2f}".format(an,tang))