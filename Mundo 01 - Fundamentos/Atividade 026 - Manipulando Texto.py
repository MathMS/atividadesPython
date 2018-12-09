'''Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra A
Em que posição ela aparece na primeira vez
Em que posição ela aparece na última vez'''

frase = str(input('Diigite uma frase: ')).strip()
frase = frase.upper()
vezes = frase.count('A')
p_vez = frase.find('A')+1
u_vez = frase.rfind('A')+1
print('\nA letra A aparece \033[33m{}\033[m vezes'.format(vezes))
print('A primeira vez que ela aparece é na posição \033[34m{}\033[m'.format(p_vez))
print('A última vez que ela aparece é na posição \033[35m{}\033[m'.format(u_vez))