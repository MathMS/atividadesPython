'''Faça um programa que leia o sexo de uma pessoa, mas só aceite valores M ou F. Caso
esteja errado, peça a digitação novamente até ter um valo correto'''

sexo = input('Digite o seu sexo [M/F]: ').upper()
while sexo != 'M' and sexo != 'F':
    sexo = input('Digite corretamente o seu sexo, apenas M ou F: ').upper()
if sexo == 'M':
    print('Seu sexo é Masculino!')
else:
    print('Seu sexo é Feminino!')