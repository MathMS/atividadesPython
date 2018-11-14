'''Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sa porção inteira'''
from math import trunc

n = float(input('Digite um número qualquer: '))
print('\nO número \033[33m{}\033[m tem a parte inteira \033[34m{}\033[m'.format(n, trunc(n)))