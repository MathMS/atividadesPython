'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequencia.
No final mostre uma listagem de preços, organizando os dados em forma tabular.'''

material = ('Lápis',1.75,'Borracha',2.0,'Caderno',15.90,'Estojo',25.0,'Transferidor',4.20,'Compasso',9.99,'Mochila',120.32,'Canetas',22.30,'Livro',34.90)

nomes = material[::2]
precos = material[1::2]
print('-'*34)
print('{:^30}'.format('LISTAGEM DE PREÇOS'))
print('-'*34)

for count in range(0,len(nomes)):
    print('{:.<24} {}'.format(nomes[count],'R$'),end =' ')
    for poss in range(0,len(precos)):
        if count in range(0,len(nomes)) and count == poss:
            print('{:>6.2f}'.format(precos[count]))