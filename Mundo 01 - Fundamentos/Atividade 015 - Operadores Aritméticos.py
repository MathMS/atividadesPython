'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

km = float(input('Quantos Km foram percorridos pelo carro alugado? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
p_km = 0.15*km
p_dias = 60*dias
total = p_km+p_dias

print('De acordo com os dados, o total a pagar pela kilometragem é \033[33mR${:.2f}\033[m, e pelos dias utilizados é \033[34mR${}\033[m; somando um valor total de \033[35mR${:.2f}\033[m'.format(p_km, p_dias, total))