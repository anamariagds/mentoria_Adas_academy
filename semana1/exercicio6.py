# Desafio Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input("Digite o nome da pessoa: ").strip().upper()
print(f"O nome da pessoa contém 'SILVA'? {('SILVA' in nome)}")