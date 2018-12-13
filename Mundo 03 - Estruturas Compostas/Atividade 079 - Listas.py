'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma
lista. Caso o número já exista dentro, ele não será adicionado. No final, serão exibidos
todos os valores únicos digitados em ordem crescente.'''
lista = []
while True:
    numero = (int(input('Digite um valor: ')))
    if numero in lista:
        print('Valor duplicado, não irei adicionar!')
    else:
        print('Valor adicionado com sucesso!')
        lista.append(numero)
    decisao = str(input('\nVocê deseja continuar? [S/N]')).strip().upper()
    if decisao == 'N':
        break
lista.sort()
print(f'\nVocê digitou os valores {lista}')
