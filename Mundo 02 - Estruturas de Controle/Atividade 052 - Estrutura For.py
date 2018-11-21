"""Faça um program que leia um número inteiro e diga se ele é ou não
um número primo"""

p = int(input("Digite um número: "))
a = p
primo = 0
for c in range(1, p+1):
    if p%c == 0:
        primo = primo + 1
if primo == 2:
    print('É primo')
else:
    print('Não é primo')