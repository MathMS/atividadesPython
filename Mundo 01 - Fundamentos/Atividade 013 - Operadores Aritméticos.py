'''Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário , com 15% de aumento'''

salario = float(input('Digite o salário do funcionário: '))
aumento = salario*0.15
novo_salario = salario + aumento
print('\nO novo salário, teve um aumento de \033[33mR${:.2f}\033[m, ficando agora com o salário total de \033[34mR${:.2f}\033[m.'.format(aumento, novo_salario))