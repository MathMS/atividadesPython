'''Melhore o jogo da atividade 028 - Manipulando Texto, onde o computador vai pensar em um número
entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostranto quantas tentativas
foram necessárias para vencer'''

import random
numPC = random.randint(0,10)
palpite = int(input('Qual número você acha que o PC pensou entre 0 e 10? '))
c = 1
while palpite != numPC:
    palpite = int(input('Hmm..Não é esse ainda, tente um novo número: '))
    c = c + 1
print('Parabéns amigo(a), conseguiu depois de {} tentativas!!'.format(c))