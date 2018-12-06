'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no
final do jogo'''
import random
c = 0
while True:
    n = int(input('Digite um valor: '))
    pi = str(input('Par ou ímpar? [P/I] ')).upper()
    PC = random.randint(0,10)
    print(f'Você jogou {n} e o PC {PC}. Total de {n+PC}')
    if (n+PC)%2 == 0 and pi == 'I':
        print('VOCÊ PERDEU! ')
        break
    elif (n+PC)%2 == 0 and pi == 'P':
        print('VOCê VENCEU! \n')
        c += 1
    elif (n + PC) % 2 != 0 and pi == 'P':
        print('VOCÊ PERDEU! ')
        break
    elif (n+PC)%2 != 0 and pi == 'I':
        print('VOCê VENCEU! \n')
        c+=1
print(f'GAME OVER! Você venceu {c} vezes!')