'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e
 tangente desse ângulo'''
import math

angulo = float(input('Digite um ângulo qualquer: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('\nO seno, cosseno e tangente do ângulo de \033[33m{}°\033[m, são respectivamente: \033[34m{:.2f}\033[m, \033[35m{:.2f}\033[m, \033[36m{:.2f}\033[m.'.format(angulo, seno, cosseno, tangente))