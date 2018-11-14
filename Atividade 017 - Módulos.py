'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de
um triângulo retângulo, calcule e mostre o comprimento da hipotenusa'''
from math import hypot

co = float(input('Digite o tamanho do cateto oposto: '))
ca = float(input('Digite o tamanho do cateto adjacente: '))
h = hypot(co, ca)
print('\nO comprimento da hipotenusa é cerca de \033[34m{:.3f}\033[m'.format(h))