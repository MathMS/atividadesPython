'''Faça um programa que leia o nome de uma pessoa, mostrando em seguida o primeiro e o último nome
separadamente'''

nome = str(input('Digite o seu nome: ')).strip()
nome = nome.split()
print('\nO seu primeiro nome é: \033[33m{}\033[m'.format(nome[0]))
print('O seu último nome é: \033[34m{}\033[m'.format(nome[len(nome)-1]))