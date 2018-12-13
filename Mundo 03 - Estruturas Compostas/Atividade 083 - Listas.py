'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá anaçisar se a expressão passada está com os parênteses abertos
e fechados na ordem correta'''

expr = str(input('Digite uma expressão: '))
lista = []
for par in expr:
    if par == '(':
        lista.append('(')
    elif par == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')