'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa devera realizar a operação solicitada em cada caso'''
a = int(input('Digite um primeiro número: '))
b = int(input('Digite um segundo número: '))
print('\nAgora escolha uma opção do que fazer com esses números!')
opcao = 0
while opcao != 5:
    print('\n[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair do programa')
    opcao = int(input('\nOpção: '))
    if opcao == 1:
        print('A soma entre esses dois números é {}!'.format(a+b))
        opcao = str(input('Deseja fazer uma nova operação? [S/N]')).upper()
        if opcao == 'N':
            opcao = 5
    if opcao ==2:
        print('O produto desses dois números é {}!'.format(a*b))
        opcao = str(input('\nDeseja fazer uma nova operação? [S/N]')).upper()
        if opcao == 'N':
            opcao = 5
    if opcao == 3:
        if a > b:
            print('{} é maior do que {}!'.format(a, b))
            opcao = str(input('\nDeseja fazer uma nova operação? [S/N]')).upper()
            if opcao == 'N':
                opcao = 5
        elif b > a:
            print('{} é maior do que {}!'.format(b, a))
            opcao = str(input('\nDeseja fazer uma nova operação? [S/N]')).upper()
            if opcao == 'N':
                opcao = 5
        else:
            print('Os dois são o mesmo número!')
            opcao = str(input('\nDeseja fazer uma nova operação? [S/N]')).upper()
            if opcao == 'N':
                opcao = 5
    if opcao == 4:
        a = int(input('Digite o novo primeiro valor: '))
        b = int(input('Digite o novo segundo valor: '))
        opcao = str(input('\nDeseja fazer uma nova operação? [S/N]')).upper()
        if opcao == 'N':
            opcao = 5

