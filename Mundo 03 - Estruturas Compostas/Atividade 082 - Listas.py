'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso crie duas listas extras, que vão conter apenas os valores pares e os
valores ímpares digitados'''
lista = []
lista_par = []
lista_impar = []
while True:
    lista.append(int(input('Digite um valor: ')))
    decisao = str(input('Você deseja continuar? [S/N]')).strip().upper()
    if decisao == 'N':
        break
for cont in range(0,len(lista)):
    if lista[cont]%2 == 0:
        lista_par.append(lista[cont])
    else:
        lista_impar.append(lista[cont])
print(f'\nA lista completa digitada foi {lista}')
print(f'A lista de pares é {lista_par}')
print(f'A lista de impares é {lista_impar}')
