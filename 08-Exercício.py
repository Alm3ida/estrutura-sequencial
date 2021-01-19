# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

hora = float(input("Digite o valor da sua hora-trabalho: "))
quantHora = int(input("Digite a quantia de horas trabalhadas: "))

print(f'O Salário ao fim do mês será de: R${hora*quantHora}')