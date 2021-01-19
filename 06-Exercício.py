# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
from math import pi

raio = float(input('Digite o valor de um raio: '))

print(f'O valor da área do círculo de raio {raio} é: {pi*raio**2 :.3f}')
