#Desafio 010 = Crie um programa que leia quanto dinheiro
#uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Considere: US$1,00 = 3,27

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 3.27
peso = real / 0.0053
franco = real / 0.4217
euro = real / 6.16
libra = real / 7.396
iene = real / 0.0478
dolar_canadense = real / 3.965


print('Com R${:.2f}, você pode comprar: \nUS${:.2f} Dólares(cotação 3.27)\n${:.2f} Pesos Argentinos\n${:.2f} Francos Suíço\n${:.2f} Euro\n${:.2f} Libra Esterlina\n${:.2f} Iene\nC${:.2f} Dolar Canadense'.format(real,dolar,peso,franco,euro,libra,iene,dolar_canadense))