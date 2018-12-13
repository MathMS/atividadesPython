'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final mostre qual foi o maior e o menor valor digitado e suas reespectivas
posições na lista'''
lista = []
i = 0
while i < 5:
    lista.append(int(input('Digite um valor: ')))
    i+=1
print(f'O maior valor da lista é o {max(lista)} e ele se encontra na {lista.index(max(lista))+1}° posição')
print(f'O menor valor da lista é o {min(lista)} e ele se encontra na {lista.index(min(lista))+1}° posição')