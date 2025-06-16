#Desenvolva um programa que pergunte a distância de uma viagem em km.
#Calcule o preço da passagem, cobrando R$0,50 por km
# para viagens de até 200Km e R$0,45 para viagens mais longas

v = float(input('Qual a distância da sua viagem? '))
if v <= 200:
    print('O custo da viagem é de R${:.2f} Reais'.format(v * 0.50))
else:
    print('O custo da viagem é de R${:.2f} Reais'.format(v * 0.45))
