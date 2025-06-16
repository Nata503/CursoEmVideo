#Desafio 008 = Escreva um programa que leia um valor em
#metros e o exiba convertido em centímetros e milímetros

n = float(input('Uma distancia em metros: '))
km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000
print('A medida de {}m corresponde a:\n{}km\n{}hm\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(n,km,hm,dam,dm,cm,mm))