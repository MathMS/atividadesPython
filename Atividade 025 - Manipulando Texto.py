'''Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome'''

nome = input('\033[34mDigite seu nome:\033[m ')
nome = nome.upper()
print('\nSILVA' in nome)