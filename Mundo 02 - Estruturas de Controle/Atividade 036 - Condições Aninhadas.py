"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensalr, sabendo que ela não pode exceder 30% do salário, ou então o empréstimo será negado"""

vlrCasa = float(input('Digite o valor da casa que deseja comprar: '))
vlrSalario = float(input('Digite agora o seu salário: '))
anos = int(input('E em quantos anos pretende pagar: '))
mesesTotal = anos*12

print('O valor da prestação mensal é de R${:.2f}'.format(vlrCasa/mesesTotal))

if vlrCasa/mesesTotal > vlrSalario*0.3:
    print('Seu empréstimo foi negado!')
else:
    print('Seu empréstimo foi aprovado!')