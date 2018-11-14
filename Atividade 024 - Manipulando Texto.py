'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome SANTO '''

nome = str(input('\033[33mDigite o nome da Cidade:\033[m ')).strip()
nome = nome.upper()
print(nome[:5] == 'SANTO')
