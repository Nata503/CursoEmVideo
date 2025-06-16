#Desafio 012 = Faça um algoritmo que leia o preçõ de um produto
#e mostre o seu novo valor, com 5% de desconto

#produto = float(input('Digite o valor do produto: R$'))
#desconto = 5 #desconto de 5%
#valor_descontado = produto * (desconto / 100)
#valor_final = produto - valor_descontado
#print('O desconto aplicado o será d

produto = float(input('Digite o valor do Produto: R$'))
cinco = produto - (produto * 5 / 100)
dez = produto - (produto * 10 / 100)
quinze = produto - (produto * 15 / 100)
vinte = produto - (produto * 20 / 100)
vinte_cinco = produto - (produto * 25 /100)
trinta = produto - (produto * 30 / 100)
trinta_cinco = produto - (produto * 35 / 100)
quarenta = produto - (produto * 40 / 100)
quarenta_cinco = produto - (produto * 45 / 100)
cinquenta = produto - (produto * 50 / 100)

print('-' * 11)
print('O Produto custa R${} e com os descontos:\n05% = R${:.2f}\n10% = R${:.2f}\n15% = R${:.2f}\n20% = R${:.2f}\n25% = R${:.2f}\n30% = R${:.2f}\n35% = R${:.2f}\n40% = R${:.2f}\n45% = R${:.2f}\n50% = R${:.2f}'.format(produto, cinco, dez, quinze, vinte, vinte_cinco, trinta, trinta_cinco, quarenta, quarenta_cinco, cinquenta))
print('-' * 11)