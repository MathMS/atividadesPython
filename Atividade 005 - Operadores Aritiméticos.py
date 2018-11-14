'''Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor'''
n = int(input('Digite um número qualquer: '))
a = n-1
s = n+1
print('\nO antecessor do número digitado é \033[35m{}\033[m e o sucessor é \033[33m{}\033[m!'.format(a, s))
