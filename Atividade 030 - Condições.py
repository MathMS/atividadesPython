'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR'''
n = int(input('Digite um número qualquer: '))
if n%2 == 0:
    print('\nO número {} é par!'.format(n))
else:
    print('\nO número {} é impar!'.format(n))