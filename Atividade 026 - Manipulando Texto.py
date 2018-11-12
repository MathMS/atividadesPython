'''Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra A
Em que posição ela aparece na primeira vez
Em que posição ela aparece na última vez'''

frase = str(input('Diigite uma frase: ')).strip()
frase = frase.upper()
x = frase.count('A')
pv = frase.find('A')+1
uv = frase.rfind('A')+1
print('\nA letra A aparece {} vezes'.format(x))
print('A primeira vez que ela aparece é na posição {}'.format(pv))
print('A última vez que ela aparece é na posição {}'.format(uv))