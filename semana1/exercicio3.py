# Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input("Digite um ângulo em graus: "))
angulo_rad = math.radians(angulo)
print(f"O ângulo de {angulo} graus tem:")
print(f"Sen: {math.sin(angulo_rad):.2f}")
print(f"Cos: {math.cos(angulo_rad):.2f}")
print(f"Tan: {math.tan(angulo_rad):.2f}")