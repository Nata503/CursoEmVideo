#Escreva um Programa que leia a velocidade de um carro
#Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi
#multado
#A multa vai custar R$7,00 por cada km acima do limite


km = float(input('Qual foi a velocidade maxima atingida? '))
multa = 7
limite = km - 80
final = (km - 80) * multa
pontos = limite / 5
if km >= 80:
    print('Você foi multado por ter ultrapassado {:.0f}km do limite permitido de 80km/h'.format(limite))
    print('Sendo assim sua multa é de R${:.2f} reais'.format(final))
    print('Portanto você perde {:.0f} pontos na carteira. Preste mais atenção!'.format(pontos))
else:
    print('Tenha um Bom dia! Você é um cidadão correto continue assim, Parabéns!')