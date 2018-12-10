'''Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menos e o maior
valor que estão na tupla.'''
from random import randint as r
n = (r(0, 10), r(0, 10), r(0, 10), r(0, 10), r(0, 10))
print('Os numeros sorteados foram:', n)
n_maior = max(n)
n_menor = min(n)
print(f'O número maior é {n_maior}\nO número menor é {n_menor}')