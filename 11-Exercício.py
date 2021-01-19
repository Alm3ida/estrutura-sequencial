# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a) o produto do dobro do primeiro com metade do segundo .
# b) a soma do triplo do primeiro com o terceiro.
# c) o terceiro elevado ao cubo.


num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

print(f"""
o produto do dobro do primeiro com metade do segundo é: {2*num1 + num2/2}
a soma do triplo do primeiro com o terceiro é: {3*num1 + num3}
o terceiro elevado ao cubo é: {num3**3}
""")