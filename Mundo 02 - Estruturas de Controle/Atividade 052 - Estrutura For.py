"""Faça um program que leia um número inteiro e diga se ele é ou não
um número primo"""

valor = int(input("Digite um número: "))
primo = 0
for c in range(1, valor + 1):
    if valor % c == 0:
        primo = primo + 1
if primo == 2:
    print('É primo')
else:
    print('Não é primo')
