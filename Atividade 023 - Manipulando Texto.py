'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados'''

num = int(input('Digite um número de 0 a 9999: '))
u = num//1%10
d = num//10%10
c = num//100%10
m = num//1000%10
print('\nUnidade = \033[33m{}\033[m'.format(u))
print('Dezena = \033[34m{}\033[m'.format(d))
print('Centena = \033[35m{}\033[m'.format(c))
print('Milhar = \033[36m{}\033[m'.format(m))
