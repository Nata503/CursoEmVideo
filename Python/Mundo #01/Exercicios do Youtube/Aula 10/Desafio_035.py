#Desenvolva um programa que leia o comprimento de 3 retas e
#diga ao usuário se elas podem ou nao formar um triângulo

#r1 -----
#r2 -----------
#r2--------

r1 = float(input('Faça a primeira linha: '))
r2 = float(input('Faça a primeira linha: '))
r3 = float(input('Faça a primeira linha: '))

#r1_len = len(r1)
#r2_len = len(r2)
#r3_len = len(r3)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem FORMAR um triângulo!')
else:
    print('os segmentos acima NÂO PODEM FORMAR um triângulo!')




