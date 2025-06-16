#Podemos usar pow(4,3) para fazer potência
print(81 ** (1/2))
print(25 ** (1/2))
print(127 ** (1/3))

#Para limpar o código no console, clicamos no botão perto de /library

print('Oi' + 'Olá') # = 'OiOlá'
print('Oi' * 5) # = 'OiOiOiOiOi'
print('=' * 20) # = ====================

#O print é uma "builtin function" (função embutida), que é uma função
#do python que necessita de parênteses para ser acionada

nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:20}!' .format(nome))

# : Usando esse símbolo na máscara ele cria a quantidade de
# espacos que você deseja.
# < ele pode ficar alinhado a esquerda.
# > ele pode ficar alinhado a direita.
# ^ ele pode ficar centralizado entre os espaços que você deseja.
# = ele pode ficar centralizado, com espaço e ele coloca iguais em volta.

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, o produto é {} e a divisão é {}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))

#Não precisamos necessariamente de variavel de soma, usamos a variavel
#de soma quando usamos ela depois, a variavel serve para armazenar um
#dado que pode ser usado depois, quando queremos resultados na hora,
#podemos utilizar o format para soma e imprimir o valor da soma.

#podemos usar o end='' no final do print, normalmente depois do format
#para juntar 2 linhas de print numa única linha






