"""Refaça a Atividade 035 - Condições, dos triângulos, acrescentando o recurso de mostrar que tipo
de triângulo será formado:
- Equilátero;
- Isósceles;
- Escaleno"""

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('\nForma um triângulo!')
    if r1 == r2 == r3:
        print('\nÉ um triângulo equilátero!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('\nÉ um triângulo isósceles!')
    elif r1 != r2 != r3:
        print('\nÉ um triângulo escaleno!')
else:
    print('\nNão forma um triângulo!')
