"""Faça um programa que mostre na tela uma contagem regressia para o estouro de fogos de artifício,
indo de 10 até 0, com pausa de 1 segundo entre eles."""
import time

for c in range(10, 0, -1):
    time.sleep(1)
    print(c)
print('FELIZ ANO NOVO!')

