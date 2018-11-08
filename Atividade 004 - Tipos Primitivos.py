"""Faça um programa que leia algo pelo teclado e retorne na tela
o seu tipo primitivo e todas as informações sobre ele."""

algo = input("Digite algo no seu teclado: ")
print('\nTipo de dado: ', type(algo))
print(algo, 'é alphanumérico ?',algo.isalnum())
print(algo, 'é alpha ?',algo.isalpha())
print(algo, 'é decimal ?',algo.isdecimal())
print(algo, 'é dígito ?',algo.isdigit())
print(algo, 'é identificador ?',algo.isidentifier())
print(algo, 'é minúsculo ?',algo.islower())
print(algo, 'é numérico ?',algo.isnumeric())
print(algo, 'é printável ?',algo.isprintable())
print(algo, 'é espaço ?',algo.isspace())
print(algo, 'é título ?',algo.istitle())
print(algo, 'é maiúsculo ?',algo.isupper())
