'''Melhore a atividade 061 - Estrutura While, perguntando para o usuário se ele que mostrar mais termos.
O programa encerra quando ele disser que quer mostrar 0 termos'''

n1 = int(input('Digite o primeiro termo: '))
n2 = int(input('Agora digite a razão da PA: '))
c = 0
c2 = 0
mais_termos = 'S'
soma = n1 + n2
while c != 10:
    soma = n1 + n2
    print('{} + {} = {}'.format(n1, n2, soma))
    n1 = soma
    c = c + 1
while mais_termos != 'N':
    mais_termos = str(input('\nVocê deseja mostrar mais termos? [S/N] ')).upper()
    if mais_termos == 'S':
        quantos_termos = int(input('Mais quantos termos você deseja mostrar? '))
        while c2 != quantos_termos:
            soma = n1 + n2
            print('{} + {} = {}'.format(n1, n2, soma))
            n1 = soma
            c2 = c2 + 1
