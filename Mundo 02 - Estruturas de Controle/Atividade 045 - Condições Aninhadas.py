"""Crie um programa que faça o computador jogar Jokenpô com você"""
import random
escolha = str(input("Escolha entre Pedra, Papel e Tesoura: "))
escolha = escolha.upper()
escolhas = ['Pedra', 'Papel', 'Tesoura']
escolha_pc = random.choice(escolhas)

if escolha_pc == 'Pedra' and escolha == 'PEDRA' or escolha_pc == 'Papel' and escolha == 'PAPEL' or escolha_pc == 'Tesoura' and escolha == 'TESOURA':
    print('EMPATE!')
elif escolha == 'Pedra' and escolha == 'TESOURA' or escolha == 'Tesoura' and escolha == 'PAPEL' or escolha == 'Papel' and escolha == 'PEDRA':
    print('VOCÊ PERDEU!')
elif escolha == 'Pedra' and escolha == 'PAPEL' or escolha == 'Tesoura' and escolha == 'PEDRA' or escolha == 'Papel' and escolha == 'TESOURA':
    print('VOCÊ VENCEU!')