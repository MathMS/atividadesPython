'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre um mensagem de que ele foi multado e com o valor dda multa.
Considere que a multa vai custar R$7,00 por cada Km acima do limite.'''
v = float(input('Digite a velocidade que o carro estava: '))
if v > 80:
    vlr = float((v - 80) * 7)
    print('\n\033[31mVocê foi multado, e deverá pagar uma multa no valor de R${:.2f}!\033[m'.format(vlr))
