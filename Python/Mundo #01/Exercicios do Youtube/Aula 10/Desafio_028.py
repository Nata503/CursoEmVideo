from random import randint
from time import sleep
import emoji


print('Vamos jogar um jogo de adivinhacão?')
resposta = str(input('Sua resposta: ')).strip().lower()
if 'n' in resposta and 'o' in resposta:
     print('Okay então, quando quiser jogar estarei aqui! Ate mais👋')
     exit()
else:
    print('-=-' * 20)
print('Estou pensando em um Número......')
sleep(3)
print('Acabei de pensar em um número, Agora adivinhe em qual numero eu pensei!')
print('-=-' * 20)
num = randint(1,5)
num2 = int(input('Digite seu chute de 1 a 5(tem que ser numero inteiro): '))
if num2 == num:
       print('Voce Acertou meu número!, sendo assim voce acaba de ganhar o jogo, PARABENS! e volte logo')
else:
       print('Eu Ganhei!,infelizmente você perdeu,porém pode reiniciar o programa e tentar denovo')