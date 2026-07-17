# Desafio Python 044: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_nascimento = int(input("Digite o ano de nascimento: "))

ano_atual = date.today().year

if ano_nascimento > ano_atual:
    print("Ano de nascimento inválido.")
else:
    idade = ano_atual - ano_nascimento

    if idade < 18:
        print(f"Faltam {18 - idade} anos para o alistamento.")
    elif idade == 18:
        print("É hora de se alistar!")
    else:
        print(f"Já se passaram {idade - 18} anos do prazo.")