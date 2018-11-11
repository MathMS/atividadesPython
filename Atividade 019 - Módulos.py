'''Um professor quer sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude
ele, lendo o nome deles e escrevendo o nome do escolhido'''
import random
n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite agora do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')
ae = (n1, n2, n3, n4)
print('\nO aluno escolhido foi o {}'.format(random.choice(ae)))
