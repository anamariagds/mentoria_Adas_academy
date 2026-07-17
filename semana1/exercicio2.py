# Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

qntdKm = float(input("Quantos quilômetros você percorreu com o carro? "))
qntdDias = float(input("Quantos dias permaneceu com o carro? "))
calculoAluguel = (60 * qntdDias) + (0.15 * qntdKm)

print("O valor total a pagar do aluguel é R${:.2f}".format(calculoAluguel))