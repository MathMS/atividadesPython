'''O mesmo professor do desafio anterior quer sortear a ordem de apresntações de trabalho dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada'''
import random
n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite agora do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')
ae = (n1, n2, n3, n4)
random.shuffle(ae)
print('\nA ordem escolhida para apresentação é: ')
print(ae)
