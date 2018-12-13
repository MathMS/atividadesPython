"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acorso com sua idade:
- Se ele ainda vai se alistar no serviço militar
- Se é a hora de se alistar
- Se já passou do tempo de alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo"""
from datetime import datetime

ano = int(input('Digite o ano de seu nascimento: '))
now = datetime.now()
diferenca = now.year - ano
if 18 == diferenca:
    print('Está na hora de se alistar garoto!')
elif diferenca > 18:
    print('Você já devia ter se alistado há {} ano(s)!'.format(diferenca - 18))
elif diferenca < 18:
    print('Você ainda terá que se alistar daqui a {} ano(s)!'.format(18 - diferenca))