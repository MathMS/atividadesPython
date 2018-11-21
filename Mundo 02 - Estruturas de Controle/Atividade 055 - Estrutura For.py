'''Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e menor peso lido'''
peso = 0
for c in range(1,6):
    peso = float(input('Digite seu peso: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso>maior:
            maior = peso
        if peso < menor:
            menor = peso

print('\nO maior peso lido foi {}Kg e o menor foi {}Kg'.format(maior, menor))
