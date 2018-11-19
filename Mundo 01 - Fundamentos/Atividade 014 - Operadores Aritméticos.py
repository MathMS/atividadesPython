'''Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.'''

c = float(input('Informe a temperatura em °C: '))
f = ((9*c)/5)+32
print('\nA temperatura de \033[33m{}°C\033[m equivale a \033[34m{}°F\033[m!'.format(c, f))