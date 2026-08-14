'''
=========================================
PROJETO: ARENA DE BATALHA

Objetivo

Criar um jogo de batalha em Python no qual
o jogador escolhe um personagem
e enfrenta um inimigo.

O jogo deve funcionar pelo terminal.
=========================================
'''


# =========================================
# DICIONARIOS / LISTAS
# =========================================

personagem = [
    {
        "nome": "Wolverine",
        "vida": 100,
        "ataque": 100,
        "defesa": 500,
        "mana": 8,
        "porção": 20
    },

    {
        "nome": "Homem Aranha",
        "vida": 500,
        "ataque": 600,
        "defesa": 500,
        "mana": 8,
        "porção": 20
    },

    {
        "nome": "Capitão America",
        "vida": 800,
        "ataque": 200,
        "defesa": 500,
        "mana": 8,
        "porção": 20
    }
]


inimigo = [
    {
        "nome": "Duende Verde",
        "vida": 100,
        "ataque": 100,
        "defesa": 500,
        "mana": 8,
        "porção": 20
    },

    {
        "nome": "Dentes-de-Sabre",
        "vida": 500,
        "ataque": 600,
        "defesa": 500,
        "mana": 8,
        "porção": 20
    },

    {
        "nome": "Ossos Cruzados",
        "vida": 800,
        "ataque": 200,
        "defesa": 500,
        "mana": 8,
        "porção": 20
    }
]


# =========================================
# FUNCOES
# =========================================

def escolher_personagem():

    print("\n=== ESCOLHER PERSONAGEM ===")

    print("1 - 🕷️ Homem-Aranha")
    print("2 - 🛡️ Capitão América")
    print("3 - 🐺 Wolverine")

    opcao = input("Escolha seu personagem: ")

    if opcao == "1":
        print("Você escolheu o 🕷️ Homem-Aranha!")
        return personagem[1]

    elif opcao == "2":
        print("Você escolheu o 🛡️ Capitão América!")
        return personagem[2]

    elif opcao == "3":
        print("Você escolheu o 🐺 Wolverine!")
        return personagem[0]

    else:
        print("Opção inválida!")
        return None


def escolher_inimigo():

    print("\n=== ESCOLHER INIMIGO ===")

    print("1 - 👺 Duende Verde")
    print("2 - 🐺 Dentes-de-Sabre")
    print("3 - ☠️ Ossos Cruzados")

    opcao = input("Escolha seu inimigo: ")

    if opcao == "1":
        print("Você enfrentará o Duende Verde!")
        return inimigo[0]

    elif opcao == "2":
        print("Você enfrentará o Dentes-de-Sabre!")
        return inimigo[1]

    elif opcao == "3":
        print("Você enfrentará o Ossos Cruzados!")
        return inimigo[2]

    else:
        print("Opção inválida!")
        return None


def iniciar_batalha(personagem, inimigo):

    print("\n==============================")
    print("       INÍCIO DA BATALHA")
    print("==============================")

    print("\nJOGADOR")
    print(f"Nome: {personagem['nome']}")
    print(f"Vida: {personagem['vida']}")
    print(f"Ataque: {personagem['ataque']}")
    print(f"Defesa: {personagem['defesa']}")
    print(f"Mana: {personagem['mana']}")

    print("\nINIMIGO")
    print(f"Nome: {inimigo['nome']}")
    print(f"Vida: {inimigo['vida']}")
    print(f"Ataque: {inimigo['ataque']}")
    print(f"Defesa: {inimigo['defesa']}")
    print(f"Mana: {inimigo['mana']}")

    print("\n==============================")
    print("      BATALHA INICIADA")
    print("==============================")


def menu_batalha():

    print("\n==============================")
    print("        MENU DE BATALHA")
    print("==============================")

    print("1 - ⚔️ Atacar")
    print("2 - 🧪 Usar poção")
    print("3 - 🔮 Usar magia")
    print("4 - 📊 Ver status")
    print("5 - 🏃 Fugir")

    opcao = input("Escolha uma ação: ")

    return opcao


def batalha(personagem, inimigo):

    iniciar_batalha(personagem, inimigo)

    while True:

        opcao = menu_batalha()

        if opcao == "1":

            print("\nVocê atacou o inimigo!")

        elif opcao == "2":

            print("\nVocê usou uma poção!")

        elif opcao == "3":

            print("\nVocê usou magia!")

        elif opcao == "4":

            print("\n=== STATUS DO JOGADOR ===")
            print(f"Nome: {personagem['nome']}")
            print(f"Vida: {personagem['vida']}")
            print(f"Ataque: {personagem['ataque']}")
            print(f"Defesa: {personagem['defesa']}")
            print(f"Mana: {personagem['mana']}")

            print("\n=== STATUS DO INIMIGO ===")
            print(f"Nome: {inimigo['nome']}")
            print(f"Vida: {inimigo['vida']}")
            print(f"Ataque: {inimigo['ataque']}")
            print(f"Defesa: {inimigo['defesa']}")
            print(f"Mana: {inimigo['mana']}")

        elif opcao == "5":

            print("\nVocê fugiu da batalha!")
            break

        else:

            print("\nOpção inválida!")


# =========================================
# MENU PRINCIPAL
# =========================================

while True:

    print("\n")
    print("===========================")
    print("   ⚔️ ARENA DE BATALHA")
    print("===========================")
    print("        📋 MENU")
    print("---------------------------")
    print("OPÇÃO 1 ▶️ Jogar")
    print("OPÇÃO 2 🦸 Ver Personagens")
    print("OPÇÃO 3 👺 Ver Inimigos")
    print("OPÇÃO 4 🏃 Sair")
    print("---------------------------")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        print("\nVocê escolheu Jogar!")

        personagem_escolhido = escolher_personagem()

        if personagem_escolhido is not None:

            inimigo_escolhido = escolher_inimigo()

            if inimigo_escolhido is not None:

                batalha(
                    personagem_escolhido,
                    inimigo_escolhido
                )


    elif opcao == "2":

        print("\nVocê escolheu Ver Personagens")
        print("\n")

        escolher_personagem()


    elif opcao == "3":

        print("\nVocê escolheu Ver Inimigos")
        print("\n")

        escolher_inimigo()


    elif opcao == "4":

        print("\nSaindo do jogo...")
        break


    else:

        print("\nOpção inválida!")