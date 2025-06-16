#Desafio 014 = Faça um algoritmo que converta uma temperatura
#digitada em °C e converta para °F
c = float(input('Informe a temperatura em °C: ')) #temperatura Celsius
f = c * 9 / 5 + 32

print('A temperatura de {}°C corresponde a {}°F!'.format(c, f))