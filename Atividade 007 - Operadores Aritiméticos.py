'''Desenvolva um programa que leia duas notas de um aluno, calcule e mostre sua média '''

n1 = int(input('Digite a primeira nota do aluno: '))
n2 = int(input('Digite a segunda nota do aluno: '))
t = n1+n2
m = (n1+n2)/2
print('\nO aluno tirou no total: {} pontos, e a média dele é {} pontos'.format(t, m))