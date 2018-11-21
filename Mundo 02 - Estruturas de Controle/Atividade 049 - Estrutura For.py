"""Refaça a Atividade 009 - Operadores Aritméticos, mostrando a tabuada de um número que o usuário
escolher, só que agora utilizando um laço for"""

n = int(input('Digite um número para realizar a tabuada: '))

for c in range(1, 11):
    print('{} x {} = {}'.format(c, n, c*n))
