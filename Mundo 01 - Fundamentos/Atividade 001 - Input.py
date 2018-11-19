""""Faça um programa onde o usuário digite seu próprio nome e após o programa retorne uma mensagem de boas-vindas"""
from datetime import date
nome = input('\nQual seu nome? ')
print('\nSeja bem-vindo(a) \033[4;33m{}\033[m é um prazer te conhecer!'.format(nome))
