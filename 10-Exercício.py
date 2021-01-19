# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
#    (C*9)/5 + 32 = F
celsius = int(input('Digite a temperatura dada em Celsius: '))

print(f'{celsius}°C equivalem a {((celsius*9)/5 + 32) :.4f}°F')