'''Escreva um programa que receba um medida em metros, e o exiba convertido em centímetros e milímetros'''

medida = float(input('Digite um medida em metros: '))
cm = medida*100
mm = cm*10
print('\nA medida de \033[33m{}m\033[m, equivale a \033[32m{}cm\033[m e \033[31m{}mm\033[m!'.format(medida, cm, mm))