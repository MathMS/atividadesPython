"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensalr, sabendo que ela não pode exceder 30% do salário, ou então o empréstimo será negado"""

vlr_casa = float(input('Digite o valor da casa que deseja comprar: '))
vlr_salario = float(input('Digite agora o seu salário: '))
anos = int(input('E em quantos anos pretende pagar: '))
meses_total = anos*12

print('O valor da prestação mensal é de R${:.2f}'.format(vlr_casa/meses_total))

if vlr_casa/meses_total > vlr_salario*0.3:
    print('Seu empréstimo foi negado!')
else:
    print('Seu empréstimo foi aprovado!')