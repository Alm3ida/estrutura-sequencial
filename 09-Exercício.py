# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#    C = 5 * ((F-32) / 9).


fahre = int(input('Digite a temperatura dada em Fahrenheit: '))

print(f'{fahre}°F equivalem a {(5*(fahre-32)/9) :.4f}')