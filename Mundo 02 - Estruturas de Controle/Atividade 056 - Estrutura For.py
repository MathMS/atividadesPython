"""Desenvolva um programa que leia nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
- A média de idade do grupo
- Qual é o nome do homem mais velho
- Quantas mulheres tem menos de 20 anos"""
si = 0
maioridade = 0
nomevelho = ''
mulher20 = 0
for c in range(1, 5):
    nome = str(input('Digite o {}° nome: '.format(c))).strip()
    idade = int(input('Digite a {}° idade: '.format(c)))
    sexo = str(input('Digite o {}° sexo: '.format(c))).strip()
    si = si + idade

    if c == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        mulher20 = mulher20+1
print('\nA idade média do grupo é: {}'.format(si/4))
print('O nome do homem mais velho é: {}'.format(nomevelho))
print('Existe(m) {} mulher(es) acima de 20 anos!'.format(mulher20))