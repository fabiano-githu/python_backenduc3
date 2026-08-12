import random


def jogar():

    numero_secreto = random.randint(1, 100)

    max_tentativas = 7
    tentativas = 0
    pontos = 0

    print("\n==============================")
    print("     JOGO DE ADIVINHAÇÃO")
    print("==============================")
    print("Adivinhe um número entre 1 e 100.")
    print("Você tem 7 tentativas.\n")

    while tentativas < max_tentativas:

        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite == numero_secreto:

            if tentativas == 1:
                pontos = 100
            elif tentativas == 2:
                pontos = 80
            elif tentativas == 3:
                pontos = 60
            elif tentativas == 4:
                pontos = 40
            elif tentativas == 5:
                pontos = 20
            elif tentativas == 6:
                pontos = 10
            else:
                pontos = 0

            print("\n VOCÊ VENCEU!")
            print(f"Tentativas: {tentativas}")
            print(f" Pontuação: {pontos} pontos")
            break

        elif palpite < numero_secreto:
            print("  O número secreto é MAIOR.")

        else:
            print(" O número secreto é MENOR.")

        print(f"  Tentativas: {tentativas}/{max_tentativas}")

    else:
        print("\n VOCÊ PERDEU!")
        print(f"O número secreto era {numero_secreto}.")


# CONTROLE DO JOGO

while True:

    jogar()

    resposta = input("\n Deseja jogar novamente? (s/n): ").lower()

    if resposta == "n":
        print("\n  Obrigado por jogar!")
        break

    elif resposta == "s":
        continue

    else:
        print("\n  Opção inválida. O jogo será encerrado.")
        break