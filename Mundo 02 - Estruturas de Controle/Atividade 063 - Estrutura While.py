'''Escreva um programa que leia um número inteiro n qualquer e mostre na tela
os n primeiros elementos de uma sequência de Fibonacci'''

num = int(input('Entre com número para saber esta sequência fibonacci:'))
x = 1
y = 0
cont = 1
while cont <= num:
    fi = (x + y) - ((x + y) - y)
    print('{}'.format(fi), end=' ')
    x = x + y
    y = x - y
    cont += 1
