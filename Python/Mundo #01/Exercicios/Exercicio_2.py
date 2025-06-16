Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ano_atual = 2025
>>> ano_nascimento = int(input("Digite seu ano de nascimento:"))
Digite seu ano de nascimento:2003
>>> idade_limite = 18
>>> idade_usuario = ano_atual - ano_nascimento
>>> nome_usuario = input("Digite seu nome:")
Digite seu nome:Nathanael
>>> if idade_usuario >= idade_limite:
...     print(f"{nome_usuario}, sua entrada foi permitida")
... else:
...     print(f"{nome_usuario}, sua entrada não foi permitida")
... 
...     
Nathanael, sua entrada foi permitida
