#Podemos usar o .format para colocar algum texto ou numero dentro do print no lugar especifico

nome = input("Digite seu nome: ")
print("È um prazer te conhecer {}!" .format(nome))

#Podemos usar o .format para colocar 3 texto ou numero

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
s1 = n1 + n2
print("A soma entre {} e {} é igual a {}!".format(n1, n2, s1))