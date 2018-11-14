'''Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto'''

p = float(input('Digite o preço do produto: '))
d = p*0.05
pf = p-d
print('\nPelo preço do produto, você tem um desconto de \033[33mR${:.2f}\033[m, então o preço final fica \033[34mR${}\033[m!'.format(d, pf))