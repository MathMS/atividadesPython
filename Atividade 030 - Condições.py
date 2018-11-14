'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR'''
n = int(input('Digite um número qualquer: '))
if n%2 == 0:
    print('\n\033[33mO número {} é par!\033[m'.format(n))
else:
    print('\n\033[34mO número {} é impar!\033[m'.format(n))