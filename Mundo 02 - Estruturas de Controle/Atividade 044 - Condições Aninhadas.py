"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
preço normal e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros"""

preco = float(input('Digite o valor a ser pago pelo produto: '))
pagamento = int(input('\nComo deseja realizar o pagamento: '
                      '\n1 - À vista dinheiro/cheque: 10% de desconto'
                      '\n2 - À vista no cartão: 5% de desconto'
                      '\n3 - Em até 2x no cartão: preço normal'
                      '\n4 - 3x ou mais no cartão: 20% de juros'
                      '\nDigite aqui => '))

if pagamento == 1:
    print(preco - (preco*0.1))
elif pagamento == 2:
    print(preco - (preco * 0.05))
elif pagamento == 3:
    print(preco)
elif pagamento == 4:
    print(preco + (preco * 0.2))
