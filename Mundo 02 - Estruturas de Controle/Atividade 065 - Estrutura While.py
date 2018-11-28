'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores digitados e entre eles qual foi
o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer continuar ou não
a digitar valores'''
c = 'S'
n = 0
cc = 0
soma = 0
maior = 0
menor = 0
while c == 'S':
    na = n
    n = int(input('Digite um número: '))
    if n >= na:
        maior = n
    elif n <= na:
        menor = n
    soma = n + soma
    cc = cc + 1
    media = soma/cc
    c = str(input('\nDeseja digitar mais um número [S/N]: '))
print('\nA média entre os valores deu: {:.2f}'.format(media))
print('O maior entre os valores é: {}'.format(maior))
print('O menor entre os valores é: {}'.format(menor))