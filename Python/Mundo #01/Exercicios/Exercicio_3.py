Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> classe_a = 4,5,6
>>> classe_b = 7,8,9
>>> soma_classe_a = sum(classe_a)
>>> soma_classe_b = sum(classe_b)
>>> media_classe_a = soma_classe_a / len(classe_a)
>>> media_classe_b = soma_classe_b / len(classe_b)
>>> print(f"A média aritmética da Classe A é: {media_classe_a}")
A média aritmética da Classe A é: 5.0
>>> print(f"A média aritmética da Classe B é: {media_classe_b}")
A média aritmética da Classe B é: 8.0
>>> media_media = media_classe_a + media_classe_b
>>> print(f"A soma das médias da Classe A e Classe B é: {media_media}")
A soma das médias da Classe A e Classe B é: 13.0
>>> media_final = media_media / 2
>>> print(f"A média final calculada das 2 Classes é: {media_final}")
A média final calculada das 2 Classes é: 6.5
