'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto'''

ano = int(input('Digite um ano qualquer: '))
if ano%4 == 0:
    print('\nO ano é Bissexto!')
else:
    print('\nO ano não é Bissexto!')