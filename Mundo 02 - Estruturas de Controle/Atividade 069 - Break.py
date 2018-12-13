'''Crie um programa que leia a idade e sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o  usuário
quer ou não continuar. No final, mostre:
a) quantas pessoas tem mais de 18 anos;
b) Quantos homens foram cadastrados;'
c) Quantas mulheres tem menos de 20 anos'''
idade18 = 0
sexo_m = 0
mulheres_menos = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    while sexo != 'M' or sexo != 'F':
        sexo = str(input('Sexo [M/F]: ')).upper()
    if idade > 18:
        idade18 += 1
    if sexo == 'M':
        sexo_m += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos += 1
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()
    if continuar == 'N':
        break
print(f'{idade18} pessoas tem mais de 18 anos!')
print(f'{sexo_m} pessoas tem o sexo Masculino!')
print(f'{mulheres_menos} são mulheres com menos de 20 anos!')
