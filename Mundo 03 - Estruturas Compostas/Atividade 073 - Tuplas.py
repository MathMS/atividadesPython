'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Apenas os 5 primeiros colocados;
b) Os últimos 4 colocados da tabela;
c) Uma lista com os times em ordem alfabética;
d) Em que posição na tabela está o time Chapecoense'''

times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
         'Bahia',  'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará SC', 'Vasco da Gama', 'Sport Recife', 'América-MG', 'EC Vitória', 'Paraná')

print(5*'='+'Os 4 primeiros colocados são'+5*'=')
for c in range(0,5):
    print(f'{c+1}° -> {times[c]}\n')
print(5*'='+'Os 4 últimos colocados são'+5*'=')
for c in range(19,15,-1):
    print(f'{c+1}° -> {times[c]}\n')
print(5*'='+'Times em ordem alfabética'+5*'=')
print(sorted(times), '\n')
print(5*'='+'Chapecoense está na posição de número'+5*'=')
print(times.index('Chapecoense')+1)

