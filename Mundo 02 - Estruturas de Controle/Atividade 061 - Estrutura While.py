'''Refaça o exercício 051 - Estrutura For, lendo o primeiro termo e a razão de uma PA, mostrando
os 10 primeiros termos da progressão usando while'''

n1 = int(input('Digite o primeiro termo: '))
n2 = int(input('Agora digite a razão da PA: '))
c = 0
soma = n1 + n2
while c != 10:
    soma = n1 + n2
    print('{} + {} = {}'.format(n1, n2, soma))
    n1 = soma
    c = c + 1
