'''Crie um programa que leia vários números inteiros do teclado. O programa só vai parar quando o usuário digitar
o número 999, que é a condição de parada. No final mostre quantos números foram digitados
e qual foi a soma entre eles'''
c = 0
s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Você digitou {c} números, e a soma entre eles deu {s}')