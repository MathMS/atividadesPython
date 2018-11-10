'''Crie um programa que leia quanto de dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
   Considere o Dólar: R$3,73 '''

r = float(input('Digite quanto de dinheiro você tem na carteira: '))
d = r/3.73
print('\nVocê consegue comprar com R${}, cerca de {:.2f} Dólares'.format(r, d))
