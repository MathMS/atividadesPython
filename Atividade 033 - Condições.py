'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor'''

n1 = int(input('Digite um número qualquer: '))
n2 = int(input('Digite um segunto número: '))
n3 = int(input('Agora digite um terceiro número: '))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('\nO maior número é o {}'.format(maior))
print('O menor número é o {}'.format(menor))
