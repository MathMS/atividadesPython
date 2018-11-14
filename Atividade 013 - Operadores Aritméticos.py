'''Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário , com 15% de aumento'''

s = float(input('Digite o salário do funcionário: '))
a = s*0.15
ns = s + a
print('\nO novo salário, teve um aumento de \033[33mR${:.2f}\033[m, ficando agora com o salário total de \033[34mR${:.2f}\033[m.'.format(a, ns))