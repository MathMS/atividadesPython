'''Crie um progrma que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final mostre:
a) Qual é o total gasto na compra;
b Quantos produtos custam mais de R$ 1000.00
c) Qual é o nome do produto mais barato.'''
total = 0
mais1000 = 0
precoA = 0
i = 0
while True:
    nome = str(input('Nome do produto: '))
    preco = int(input('Preço: R$'))
    if i >= 1 and preco <= precoA:
        menor = preco
        nome2 = nome
    total = total + preco
    precoA = preco
    if preco > 1000:
        mais1000 += 1
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
    i += 1
print(f'O total da compra deu R${total}')
print(f'Temos {mais1000} produtos acima de R$1000.00')
if i < 1:
    print(f'O produto mais barato foi {nome} que custa R${preco:.2f}')
else:
    print(f'O produto mais barato foi {nome2} que custa R${menor:.2f}')