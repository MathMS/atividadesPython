'''Escreva um programa que pergunte o salário do funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00 calcule um aumento de 10%.
Para inferiores ou iguais, o aumento é de 15%'''

salario = float(input('Digite o salário do funcionário: '))

if salario > 1250:
    aumento = salario*0.10
    print('\nO seu salário teve um aumento de 10%, ficando um total de \033[32mR${:.2f}\033[m'.format(salario+aumento))
else:
    aumento = salario*0.15
    print('\nO seu salário teve um aumento de 15%, ficando um total de \033[32mR${:.2f}\033[m'.format(salario+aumento))