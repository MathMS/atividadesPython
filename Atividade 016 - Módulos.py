'''Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sa porção inteira'''
from math import trunc

n = float(input('Digite um número qualquer: '))
print('\nO número {} tem a parte inteira {}'.format(n, trunc(n)))