#Desafio 015 = Escreva um programa que pergunte a quantidade de Km
#percorridos por um carro alugado e a quantidade de dias pelos
#quais ele foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$ por dia e R$0.15 por Km rodado

d = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
cd = 60 * d #custo por dia do carro
ckm = 0.15 * km #custo por km do carro
total = cd + ckm #posso fazer dessa forma: pago = (d * 60) + (km * 0.15)

print('O total a pagar é de R${:.2f}'.format(total))