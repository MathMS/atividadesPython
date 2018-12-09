'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados'''

num = int(input('Digite um número de 0 a 9999: '))
unidade = num//1%10
dezena = num//10%10
centena = num//100%10
milhar = num//1000%10
print('\nUnidade = \033[33m{}\033[m'.format(unidade))
print('Dezena = \033[34m{}\033[m'.format(dezena))
print('Centena = \033[35m{}\033[m'.format(centena))
print('Milhar = \033[36m{}\033[m'.format(milhar))
