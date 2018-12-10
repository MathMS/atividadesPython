'''Crie um programa que tenha uma tupla com várias palavras. Depois disso, você deve mostrar, mara cada palavra,
quais são suas vogais'''

palavras = ('acucar', 'cafe', 'computador', 'celular', 'facebook', 'youtube', 'coco', 'playlist', 'musica', 'estudar', )

vogais = ('a','e','i','o','u')
for tab in palavras:
  print(f'\nNa palavra {tab.upper()} temos')
  for pega_vogais in vogais:
    if pega_vogais in tab:
      print(f'{pega_vogais.upper()}')