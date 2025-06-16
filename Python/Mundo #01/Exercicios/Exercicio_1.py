Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> salario = float(input("Digite seu salario atual: R$"))
Digite seu salario atual: R$2500
>>> prestação = float(input("Digite o valor das prestações que deseja: R$"))
Digite o valor das prestações que deseja: R$1100
>>> limite = salario * 0.20
>>> if prestação > limite:
...     print("Empréstimo não concedido")
... else:
...     print("Empréstimo concedido")
... 
...     
Empréstimo não concedido
