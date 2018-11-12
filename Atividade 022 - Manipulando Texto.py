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
print('\n1 - Maiúsculo: {}'.format(ma))
print('2 - Minúsculo: {}'.format(mi))
print('3 - Letras retirando espaço: {} letras'.format(tamanho))
print('4 - Letras do primeiro nome: {} letras'.format(pnome))