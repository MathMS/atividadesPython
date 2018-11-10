'''Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário , com 15% de aumento'''

s = float(input('Digite o salário do funcionário: '))
a = s*0.15
ns = s + a
print('\nO novo salário, teve um aumento de R${:.2f}, ficando agora com o salário total de R${:.2f}.'.format(a, ns))