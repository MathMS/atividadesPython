'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999,
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a
soma entre eles'''
n = 0
c = 0
s = 0
while  n != 999:
    n = int(input('Digite um número: '))
    s = (s + n)
    c = c + 1
print('Foram digitados {} números, e a soma deles deu {}'.format(c-1, s-999))