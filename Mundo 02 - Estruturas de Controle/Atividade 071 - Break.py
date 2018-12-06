'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início,
pergunte ao usuário qual será o valor a ser sacado (inteiro) e o programa vai informar quantas cédulas de
cada valor serão entregues.

Obs: Considere que o caixa possua cédulas de R$50, R$20, R$10 e R$1'''

N=int(input('Qual o valor você gostaria de sacar? '))
cedulas = [1, 10, 20, 50]
c = 3
while N > 0:
    nCedulas = N//cedulas[c]
    N -= nCedulas*cedulas[c]
    if nCedulas > 0:
        print(f'{nCedulas} cédulas de {cedulas[c]}')
    c -= 1