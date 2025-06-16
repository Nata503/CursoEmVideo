#Desafio 011 = Faça um programa que leia a largura e a altura de uma
#parede em metros, calcule a sua área e a quantidade de tinta
#necessária para pintá-la, sabendo que cada litro de tinta,
#pinta uma área de 2m²

l = float(input('Largura da Parede: ')) #largura
a = float(input('Altura da Parede: ')) #altura
area = l * a
tinta = area / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².\nPara pintar essa parede, você precisará de {:.1f} de tinta'.format(l, a, area, tinta ))