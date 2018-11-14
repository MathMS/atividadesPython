'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário perdeu ou venceu'''
import random
npc = random.randint(0,5)
nus = int(input('Adivinhe o número em que o computador pensou entre 0 e 5: '))
if nus == npc:
    print('\n\033[34mParabéns, você acertou!\033[m ')
else:
    print('\n\033[31mInfelizmente você perdeu!\033[m ')