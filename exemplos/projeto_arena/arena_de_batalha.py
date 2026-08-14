'''
=========================================
PROJETO: ARENA DE BATALHA
Objetivo

Criar um jogo de batalha em Python no qual 
o jogador escolhe um personagem
e enfrenta um inimigo.
O jogo deve funcionar pelo terminal.
==========================================

'''

def escolher_personagem():
    print("=== ESCOLHER PERSONAGEM ===")

    print("1 🕷️ Homem-Aranha")
    print("2 🛡️ Capitão América")
    print("3 🐺 Wolverine")

    opcao = input("Escolha seu personagem: ")

    if opcao == "1":
        print("Você escolheu o 🕷️ Homem-Aranha!")

    elif opcao == "2":
        print("Você escolheu o 🛡️ Capitão América!")

    elif opcao == "3":
        print("Você escolheu o 🐺 Wolverine!")

    else:
        print("Opção inválida!")


def escolher_inimigo():
    print("\n=== ESCOLHER INIMIGO ===")

    print("1 - 👺 Duende Verde")
    print("2 - 🐺 Dentes-de-Sabre")
    print("3 - ☠️ Ossos Cruzados")

    opcao = input("Escolha seu inimigo: ")

    if opcao == "1":
        print("Você enfrentará o Duende Verde!")

    elif opcao == "2":
        print("Você enfrentará o Dentes-de-Sabre!")

    elif opcao == "3":
        print("Você enfrentará o Ossos Cruzados!")

    else:
        print("Opção inválida!")


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
    print("        BATALHA INICIADA")
    print("==============================")




personagem = [
{"nome":"wolvwrine",
"vida": 100,
"ataque":100,
"defesa":500,
"mana":8,
"porção":20,
},
{"nome":"Homem Aranha",
"vida": 500,
"ataque":600,
"defesa":500,
"mana":8,
"porção":20,
},
{"nome":"Capitão America",
"vida": 800,
"ataque":200,
"defesa":500,
"mana":8,
"porção":20,}
]


inimigo = [
{"nome":"Duende Verde",
"vida": 100,
"ataque":100,
"defesa":500,
"mana":8,
"porção":20,
},
{"nome":"Dentes-de-Sabre",
"vida": 500,
"ataque":600,
"defesa":500,
"mana":8,
"porção":20,
},
{"nome":"Ossos Cruzados",
"vida": 800,
"ataque":200,
"defesa":500,
"mana":8,
"porção":20,}
]



while True:

    print("===========================")
    print(" ===⚔️ ARENA DE BATALHA===")
    print("===========================")
    print("        📋 MENU          ")
    print("--------------------------")
    print("OPÇÃO 1 ▶️  Jogar")
    print("OPÇÃO 2 🦸 Ver Personagens")
    print("OPÇÃO 3 👺 Ver Inimigos")
    print("OPÇÃO 4 🏃 Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Você escolheu Jogar")

    elif opcao == "2":
        print("Você escolheu Ver Personagens")
        print("\n\n")
        escolher_personagem()
        

    elif opcao == "3":
        print("Você escolheu Ver Inimigos")
        print("\n\n")
        escolher_inimigo()

    elif opcao == "4":
        print("Saindo do jogo...")
        break

    else:
        print("Opção inválida!")


