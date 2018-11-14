"""Faça um programa que leia algo pelo teclado e retorne na tela
o seu tipo primitivo e todas as informações sobre ele."""

algo = input("Digite algo no seu teclado: ")
print('\n\33[37mTipo de dado: ', type(algo))
print(algo, '\033[31mé alphanumérico ?',algo.isalnum())
print(algo, '\033[32mé alpha ?',algo.isalpha())
print(algo, '\033[33mé decimal ?',algo.isdecimal())
print(algo, '\033[34mé dígito ?',algo.isdigit())
print(algo, '\033[35mé identificador ?',algo.isidentifier())
print(algo, '\033[36mé minúsculo ?',algo.islower())
print(algo, '\033[37mé numérico ?',algo.isnumeric())
print(algo, '\033[31mé printável ?',algo.isprintable())
print(algo, '\033[32mé espaço ?',algo.isspace())
print(algo, '\033[33mé título ?',algo.istitle())
print(algo, '\033[34mé maiúsculo ?',algo.isupper())
