'''Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.'''

temperatura_c = float(input('Informe a temperatura em °C: '))
fahrenheit = ((9*temperatura_c)/5)+32
print('\nA temperatura de \033[33m{}°C\033[m equivale a \033[34m{}°F\033[m!'.format(temperatura_c, fahrenheit))