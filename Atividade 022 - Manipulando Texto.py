'''Crie um programa que leia o nome completo de um pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas minúsculas
Quantas letras ao todo (sem considerar espaços)
Quantas letras em o primeiro nome'''

nome = str(input('Digite seu nome completo: ')).strip()
ma = nome.upper()
mi = nome.lower()
nome = nome.split()
tamanho = len(nome)-nome.count(' ')
pnome = len(nome[0])
print('\n1 - Maiúsculo: \033[33m{}\033[m'.format(ma))
print('2 - Minúsculo: \033[34m{}\033[m'.format(mi))
print('3 - Letras retirando espaço: \033[35m{} letras\033[m'.format(tamanho))
print('4 - Letras do primeiro nome: \033[36m{} letras\033[m'.format(pnome))