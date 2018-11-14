'''Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada'''

n = int(input('Digite um número qualquer: '))

print('\n\033[35mA tabuada do número {} completa é: '.format(n))
print('{}*0 = \033[32m{}'.format(n, n*0))
print('{}*1 = \033[33m{}'.format(n, n*1))
print('{}*2 = \033[34m{}'.format(n, n*2))
print('{}*3 = \033[35m{}'.format(n, n*3))
print('{}*4 = \033[36m{}'.format(n, n*4))
print('{}*5 = \033[37m{}'.format(n, n*5))
print('{}*6 = \033[31m{}'.format(n, n*6))
print('{}*7 = \033[32m{}'.format(n, n*7))
print('{}*8 = \033[33m{}'.format(n, n*8))
print('{}*9 = \033[34m{}'.format(n, n*9))
print('{}*10 = \033[35m{}'.format(n, n*10))
