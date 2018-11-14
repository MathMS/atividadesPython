'''Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada'''

n = int(input('Digite um número qualquer: '))
d = n*2
t = n*3
r = n**(1/2)
print('\nO dobro do número \033[31m{}\033[m é \033[33m{}\033[m, o triplo é \033[35m{}\033[m e a raiz quadrada é \033[37m{:.2f}\033[m!'.format(n, d, t, r))