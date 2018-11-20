"""Escreva um programa que leia um número inteiro qualquer e peça o usuário para escolher qual será
a base de conversão:
 - 1 para binário
 - 2 para octal
  - 3 para hexadecimal"""

var = int(input('Digite um valor para ser convertido: '))
opcao = int(input('\nVocê deseja converter para qual base?\n'
                  '1 - Binário\n'
                  '2 - Octal\n'
                  '3 - Hexadecimal\n'
                  'Digite aqui => '))

if opcao == 1:
    um = bin(var)
    print('O número {} convertido para binário fica: {}'.format(var, um))
elif opcao == 2:
    dois = oct(var)
    print('O número {} convertido para octal fica: {}'.format(var, dois))
elif opcao == 3:
    tres = hex(var)
    print('O número {} convertido para hexadecimal fica: {}'.format(var, tres))
else:
    print('Opção inválida!')