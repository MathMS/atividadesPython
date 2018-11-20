"""Crie um programa que leia duas notas de aluno e calcule sua média, mostrando uma
mensagem no final, de acordo com a média atingida"""
a = float(input('Digite a primeira nota do aluno: '))
b = float(input('Digite a segunda nota do aluno: '))
media = (a+b)/2

if media < 5:
    print('Sua média foi {:.2f}, portanto está \033[31mREPROVADO!\033[m'.format(media))
elif 5 < media < 6.9:
    print('Sua média foi {:.2f}, portanto está de \033[32mRECUPERAÇÃO!\033[m'.format(media))
elif media >= 7:
    print('Sua média foi {:.2f}, portanto está \033[34mAPROVADO!\033[m'.format(media))