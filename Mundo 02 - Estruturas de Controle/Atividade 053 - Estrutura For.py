"""Crie um programa que leia uma frase qualuqer e diga se ela é palíndroma,
desconsiderando os espaços"""

f = str(input('Digite uma frase qualquer: ')).strip().upper().split()
junto = ''.join(f)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]
print(junto, inverso)
if junto == inverso:
    print('\nÉ PALÍNDROMA!')
else:
    print('\nNÃO É PALÍNDROMA!')
