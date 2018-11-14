'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

km = float(input('Quantos Km foram percorridos pelo carro alugado? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
pkm = 0.15*km
pdias = 60*dias
total = pkm+pdias

print('De acordo com os dados, o total a pagar pela kilometragem é \033[33mR${:.2f}\033[m, e pelos dias utilizados é \033[34mR${}\033[m; somando um valor total de \033[35mR${:.2f}\033[m'.format(pkm, pdias, total))