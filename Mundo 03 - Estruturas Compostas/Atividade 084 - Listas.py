'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas;
b) Uma listagem cm as pessoas mais pesadas;
c) Uma listagem com as pessoas mais leves.'''

pessoas = []
pessoa = []
contador = 0
maior = menor = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if contador == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    pessoas.append(pessoa[:])
    pessoa.clear()
    escolha = str(input('Você deseja continuar? [S/N]'))
    if escolha in 'Nn':
        break
    contador += 1
print(f'\nAo todo você cadastrou {contador+1} pessoas.')
print(f'O maior peso foi {maior}Kg')
for p in pessoas:
    if p[1] == maior:
        print(f'Pessoas mais pesadas: {p[0]}')
print(f'\nO menor peso é {menor}Kg')
for p in pessoas:
    if p[1] == menor:
        print(f'Pessoas mais leves: {p[0]}')
