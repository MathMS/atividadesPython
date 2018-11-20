"""Desenvolva um programa que leia o peso e a alturo de uma pessoa, calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbita"""
1
peso = float(input('Digite seu peso: '))
tamanho = float(input('Digite sua altura em metros: '))
imc = peso / (tamanho * tamanho)

if imc < 18.5:
    print('\nAbaixo do peso!')
elif 18.5 <= imc <= 25:
    print('\nPeso ideal!')
elif 25 < imc <= 35:
    print('\nSobrepeso!')
elif 35 < imc <= 40:
    print('\nObesidade!')
elif 40 < imc:
    print('\nObesidade mórbita!')