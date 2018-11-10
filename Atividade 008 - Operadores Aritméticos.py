'''Escreva um programa que receba um medida em metros, e o exiba convertido em centímetros e milímetros'''

m = float(input('Digite um medida em metros: '))
cm = m*100
mm = cm*10
print('\nA medida de {}m, equivale a {}cm e {}mm!'.format(m, cm, mm))