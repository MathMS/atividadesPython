"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de
um atleta e mostre sua categoria de acorso com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 20 anos: SÊNIOR
 - Acima: MASTER"""
from datetime import datetime

now = datetime.now()
ano = int(input('Digite o ano de nascimento do atleta: '))
diferenca = now.year - ano

if diferenca <= 9:
    print('\nAtleta Mirim!')
elif diferenca > 9 and diferenca <=14:
    print('\nAtleta Infantil!')
elif diferenca > 14 and diferenca <= 19:
    print('\nAtleta Júnior!')
elif diferenca > 19 and diferenca <= 20:
    print('\nAtleta Sênior!')
elif diferenca > 20:
    print('\nAtleta Master!')

