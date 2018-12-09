'''Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto'''

preco = float(input('Digite o preço do produto: '))
desconto = preco*0.05
preco_novo = preco-desconto
print('\nPelo preço do produto, você tem um desconto de \033[33mR${:.2f}\033[m, então o preço final fica \033[34mR${}\033[m!'.format(desconto, preco_novo))