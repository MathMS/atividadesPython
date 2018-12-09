'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de
um triângulo retângulo, calcule e mostre o comprimento da hipotenusa'''
from math import hypot

cateto_oposto = float(input('Digite o tamanho do cateto oposto: '))
cateto_adjacente = float(input('Digite o tamanho do cateto adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print('\nO comprimento da hipotenusa é cerca de \033[34m{:.3f}\033[m'.format(hipotenusa))