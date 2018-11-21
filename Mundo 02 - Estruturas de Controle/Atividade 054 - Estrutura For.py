"""Crie um programa que leia o ano de nascimento de sete pessoas.
No final ostre quantas pessoas não a tingiram a maioridade e
quantas já são maiores."""
import datetime
maiores = 0
menores = 0
now = datetime.datetime.now().year
for c in range(1,6):
    nascimento = int(input('Digite o ano de nascimento: '))
    idade = now - nascimento
    if idade >= 18:
        maiores = maiores + 1
    else:
        menores = menores + 1
print('\n{} maior(es) de idade'.format(maiores))
print('{} menor(es) de idade'.format(menores))
