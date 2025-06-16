#Padrão ANSI - Escape sequence
#Para começar nesse código é \033[ m
#print('\033[7;97mOlá, Mundo!\033[m')


a = 3
b = 5
print('Os valores são \033[32m{} \033[97me \033[31m{}'.format(a,b))

nome = 'Nathanael'
cores = {'limpa': '\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m' ,
         'pretoebranco':'\033[7:97m'}
print('Olá, Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'],nome,cores['limpa']))