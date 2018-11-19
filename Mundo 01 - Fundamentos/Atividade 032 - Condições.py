'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto'''

ano = int(input('Digite um ano qualquer: '))
if ano%4 == 0:
    print('\n\033[34mO ano é Bissexto!\033[m')
else:
    print('\n\033[35mO ano não é Bissexto!\033[m')