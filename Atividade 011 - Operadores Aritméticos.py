'''Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pinta-la,
sabendo que cada litro de tinta , pinta uma área de 2m²'''

a = float(input('Digite a altura da parede: '))
l = float(input('Agora digite sua largura: '))
ar = a*l
t = ar/2
print('\nA área total da parede é de {}m², para pinta-la você precisará de {}L de tinta.'.format(ar, t))

