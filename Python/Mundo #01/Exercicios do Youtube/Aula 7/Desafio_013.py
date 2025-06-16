#Desafio 013 = Faça um algoritmo que leia o salário de um funcionário
#e mostre o seu novo salário, com 15% de aumento

#base = float(input('Digite seu salário: '))
#bonus = 0.15 #Bonus de 15% sobre o salario
#aumento = base * bonus
#novo_salario = base + aumento
#print('Seu salario Base R${} mais um aumento de 15%, agora seu novo salario será de R${:.2f}'.format(base, novo_salario))

salario = float(input('Qual é o seu salário? R$'))
cinco = salario + (salario * 5 / 100)
dez = salario + (salario * 10 / 100)
quinze = salario + (salario * 15 /100)
vinte = salario + (salario * 20 /100)
vinte_cinco = salario + (salario * 25 / 100)
trinta = salario + (salario * 30 /100)
trinta_cinco = salario + (salario * 35 / 100)
quarenta = salario + (salario * 40 / 100)
quarenta_cinco = salario + (salario * 45 / 100)
cinquenta = salario + (salario * 50 / 100)

print('-' * 15)
print('Seu salário é R${:.2f} e com os aumentos ficaria:\n05% = R${:.2f}\n10% = R${:.2f}\n15% = R${:.2f}\n20% = R${:.2f}\n25% = R${:.2f}\n30% = R${:.2f}\n35% = R${:.2f}\n40% = R${:.2f}\n45% = R${:.2f}\n50% = R${:.2f}'.format(salario, cinco, dez, quinze, vinte, vinte_cinco, trinta, trinta_cinco, quarenta, quarenta_cinco, cinquenta))
print('-' * 15)