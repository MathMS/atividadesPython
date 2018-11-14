'''Desenvolva um programa que leia duas notas de um aluno, calcule e mostre sua média '''

n1 = int(input('Digite a primeira nota do aluno: '))
n2 = int(input('Digite a segunda nota do aluno: '))
t = n1+n2
m = (n1+n2)/2
print('\nO aluno tirou no total: \033[32m{}\033[m pontos, e a média dele é \033[31m{}\033[m pontos'.format(t, m))