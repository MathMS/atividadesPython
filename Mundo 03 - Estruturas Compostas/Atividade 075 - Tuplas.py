'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final mostre:
a) Quantas vezes apareceu o número 9;
b) Em que posição foi digitado o primeiro valor 3;
c) Quais foram os números pares.'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o quarto número: '))
tupla = (n1, n2, n3, n4)
print(f'\nO número 9 apareceu {tupla.count(9)} vezes')
print(f'O número 3 apareceu na {tupla.index(3)+1}° posição')
print('Os números pares são: \n')
for c in range(0,4):
    if tupla[c]%2 == 0:
        print(f'O número {tupla[c]} é par')