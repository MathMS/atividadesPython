'''Escreva um programa que pergunte o salário do funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00 calcule um aumento de 10%.
Para inferiores ou iguais, o aumento é de 15%'''

s = float(input('Digite o salário do funcionário: '))

if s > 1250:
    a = s*0.10
    print('\nO seu salário teve um aumento de 10%, ficando um total de \033[32mR${:.2f}\033[m'.format(s+a))
else:
    a = s*0.15
    print('\nO seu salário teve um aumento de 15%, ficando um total de \033[32mR${:.2f}\033[m'.format(s+a))