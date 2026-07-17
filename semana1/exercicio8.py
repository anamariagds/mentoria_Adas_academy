# Desafio Python 045: Crie um jogo de Jokenpô (Pedra, Papel, Tesoura) entre o usuário e o computador.
import random

print("Bem-vindo ao Jokenpô!")
print("Escolha uma opção:")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")

opcao_usuario = int(input("Sua escolha: "))

if opcao_usuario not in [1, 2, 3]:
    print("Opção inválida!")
else:
    opcao_computador = random.randint(1, 3)

    if opcao_computador == 1:
        print("O computador escolheu Pedra.")
    elif opcao_computador == 2:
        print("O computador escolheu Papel.")
    else:
        print("O computador escolheu Tesoura.")

    if opcao_usuario == opcao_computador:
        print("Empate!")
    elif (opcao_usuario == 1 and opcao_computador == 3) or \
         (opcao_usuario == 2 and opcao_computador == 1) or \
         (opcao_usuario == 3 and opcao_computador == 2):
        print("Você venceu!")
    else:
        print("Computador venceu!")