'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre:
a) Quantos números foram digitados;
b) A lista de valores, ordenada de forma descrescente;
c) Se o valor 5 foi digitado e está ou não na lista.'''
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    decisao = str(input('Você deseja continuar? [S/N]')).strip().upper()
    if decisao == 'N':
        break
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} valores')
print(f'A ordem decrescente da lista é {lista}')
if 5 in lista:
    print('O valor 5 foi digitado e se encontra na lista!')
else:
    print('O valor 5 não está incluído na lista!')