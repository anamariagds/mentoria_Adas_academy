# Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Informe o salário do funcionário: "))
novoSalario = salario + (salario * 15 / 100)

print("O novo salário com aumento de 15% fica em R${:.3f}".format(novoSalario))