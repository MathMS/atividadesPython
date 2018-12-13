"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão."""

termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão da PA: "))
soma = razao + termo
print('{} + {} = {}'.format(termo, razao, soma))
for c in range(1,10):
    print('{} + {} = {}'.format(soma, razao, soma+razao))
    soma += razao