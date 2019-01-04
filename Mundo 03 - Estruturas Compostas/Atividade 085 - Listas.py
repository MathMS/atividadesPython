'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados
os valores paras e ímpares. No final mostre os valores pares e ímpares em ordem crescente.'''

pares = []
impares = []
lista = []

for n in range(0, 7):
    numero = int(input(f'Digite o {n+1}° número: '))
    if numero%2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

