Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> salario = float(input("Digite seu salário: R$"))
Digite seu salário: R$2650
>>> reajuste = float(input("Digite seu reajuste em porcentagem (%): ").replace(',','.'))
Digite seu reajuste em porcentagem (%): 35.5
>>> salario_novo = salario * (1 + reajuste / 100)
>>> print(f"Seu novo salário com o reajuste é R${salario_novo}")
Seu novo salário com o reajuste é R$3590.75
