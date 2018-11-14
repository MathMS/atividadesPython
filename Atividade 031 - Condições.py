'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km e R$0.45 para
viagens mais longas.'''

v = float(input('Qual o tamanho da viagem em Km? '))
if v <= 200:
    print('\nVocê gastará com passagem cerca de \033[33mR${}\033[m!'.format(v*0.50))
else:
    print('\nVocê gastará com passagem cerca de \033[33mR${}\033[m!'.format(v*0.45))
