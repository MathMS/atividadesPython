'''O mesmo professor do desafio anterior quer sortear a ordem de apresntações de trabalho dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada'''
import random
n1 = input('\033[33mDigite o nome do primeiro aluno:\033[m ')
n2 = input('\033[34mDigite agora do segundo aluno:\033[m ')
n3 = input('\033[35mDigite o nome do terceiro aluno:\033[m ')
n4 = input('\033[36mDigite o nome do quarto aluno:\033[m ')
ae = (n1, n2, n3, n4)
random.shuffle(ae)
print('\nA ordem escolhida para apresentação é: ')
print(ae)
