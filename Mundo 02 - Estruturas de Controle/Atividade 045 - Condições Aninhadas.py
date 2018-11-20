"""Crie um programa que faça o computador jogar Jokenpô com você"""
import random
escolha = str(input("Escolha entre Pedra, Papel e Tesoura: "))
escolha = escolha.upper()
escolhas = ['Pedra', 'Papel', 'Tesoura']
escolhapc = random.choice(escolhas)

if escolhapc == 'Pedra' and escolha == 'PEDRA' or escolhapc == 'Papel' and escolha == 'PAPEL' or escolhapc == 'Tesoura' and escolha == 'TESOURA':
    print('EMPATE!')
elif escolha == 'Pedra' and escolha == 'TESOURA' or escolha == 'Tesoura' and escolha == 'PAPEL' or escolha == 'Papel' and escolha == 'PEDRA':
    print('VOCÊ PERDEU!')
elif escolha == 'Pedra' and escolha == 'PAPEL' or escolha == 'Tesoura' and escolha == 'PEDRA' or escolha == 'Papel' and escolha == 'TESOURA':
    print('VOCÊ VENCEU!')