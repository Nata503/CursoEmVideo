print('Seja Bem-Vindo ao Imovel facilitado, onde tr damos o valor das parcelas pra vc ter seu imóvel!. A seguir iremos fazer umas perguntas pra saber se voce é apto a ter o empréstimos e o valor certinho de cada parcela mensal!')
casa = float(input('Digite o valor do imovel: '))
salario = float(input('Agora precisamos saber o seu salário base: '))
anos = int(input('Agora, fala pra nos, em quantos anos voce pretende pagar o imovel: '))

meses = anos * 12
mensal = round(casa / meses, 2)
prestacao = 0.30 * salario

if mensal <= prestacao:
     print('Meus parabéns, foi aprovado seu empréstimo de R${:.3f} reais com {} parcelas de R${} reais. Com base em 30% do seu salário que é R${} reais!'.format(casa, meses, mensal, prestacao))
else:
      print('Infelizmente nao conseguimosl um empréstimo para o seu perfil, tente colocar mais anos ou um valor de imovel menor e tente novamente, a sua liberacão!')