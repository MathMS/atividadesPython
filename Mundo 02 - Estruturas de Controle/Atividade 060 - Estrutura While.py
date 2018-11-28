'''Faça um programa que leia um número qualquer e mostre seu fatorial'''

n = int(input('Digite um número: '))
n2 = n
c = n - 1
fatorial = 0
while c != 0:
    fatorial = n * c
    n = fatorial
    c = c - 1
print('O fatorial de {} é: {}'.format(n2, fatorial))