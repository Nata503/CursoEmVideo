#Aula 10 -  Condições simples e compostas


#Ex:
#Carro.siga()
#Carro.esquerda()
#Carro.siga()
#Carro.direita()
#Carro.siga()
#Carro.direita()
#Carro.siga()
#Carro.esquerda()
#Carro.siga()

#Outro Ex:

#Carro.siga()
#Temos 2 caminhos diferentes:
#Agora temos possibilidades
#Igual acontece em jogos acontece no python, onde as ações
#do cliente mudam os caminhos

#Carro.siga
#Carro.direita
#Carro.siga
#Carro.direita
#Carro.esquerda
#Carro.siga
#Carro.direita
#Carro.siga
#Carro.pare

#Criamos um bloco de comandos caso eu vire pra esquerda
#E agora criaremos o bloco da direita:

#Carro.siga
#Carro.esquerda
#Carro.siga
#Carro.esquerda
#Carro.siga
#Carro.pare

#O waze é um exemplo dos comandos acima onde ele diz pra vc qual caminho é mais rápido para chegar no destino

#Temos 2 fluxo
#O fluxo verde se ele for pra esquerda
#O fluxo vermelho se ele for pra direita

#E no python usamos se:

#Se carro.esquerda()
#Senão

#Carro.siga
#Se carro.esquerda()
#Comandos
#Senão
#carro.siga()
#Carro.pare()

#Estrutura condicional

#Se carro.esquerdo()
#Bloco V
#Senão
#Bloco F

#Condição:

#if carro.esquerdo():
       #Bloco True
#else:
       #Bloco False

#Tempo = int(input('Quantos anos tem seu carro? '))

#if tempo <= 3:
   #print('Carro novo')
#else:
   #print('Carro velho')
#print('--FIM--')


#Condição simplificada

#Tempo = int(input('Quantos anos tem seu carro? '))
#print('Carro novo') if tempo<=3 else 'Carro velho')
#Print('--FIM--')

#Prática

#nome = str(input('Qual é sua nome? ')
#if nome == ('Gustavo':
    #print('Que nome lindo você tem!')
#else:
     #print('Seu nome é tão normal')
#print('Bom dia, {}'.format(nome)

#Quando temos else ele é Condição composta e quando kao tem é simples

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/ 2
print('A sua média foi {:.1f}'.format(m))
if m > 6.0:
     print('Sua média foi boa! PARABÉNS!')
else:
     print('Sua média foi ruim! ESTUDE MAIS!')

#Podemos fazer simples:

print('PARABÉNS!' if m>=6 else'ESTUDEMAIS!')