
'''

###############################
PROJETO 4: SISTEMA DE FASES
Esse é o projeto integrador.
🎯 Objetivo
Criar uma pequena aventura com:
•	jogador; 
•	níveis; 
•	experiência; 
•	inimigos; 
•	combate; 
•	vida; 
•	moedas; 
•	inventário; 
•	poções; 
•	progressão de fases.
##############################

'''

import random


# ==========================================================
# DICIONÁRIOS
# ==========================================================

jogador = {
    "nome": "",
    "vida": 100,
    "vida_maxima": 100,
    "ataque": 20,
    "nivel": 1,
    "xp": 0,
    "xp_proximo_nivel": 100,
    "moedas": 50,
    "fase": 1,
    "inventario": {
        "pocao": 3
    }
}


inimigos = [
    {
        "nome": "Goblin",
        "vida": 50,
        "ataque": 10,
        "xp": 30,
        "moedas": 20
    },
    {
        "nome": "Orc",
        "vida": 80,
        "ataque": 15,
        "xp": 50,
        "moedas": 30
    },
    {
        "nome": "Cavaleiro Sombrio",
        "vida": 120,
        "ataque": 20,
        "xp": 80,
        "moedas": 50
    },
    {
        "nome": "Dragão",
        "vida": 150,
        "ataque": 25,
        "xp": 120,
        "moedas": 100
    }
]


# ==========================================================
# FUNÇÕES
# ==========================================================


# mostrar_status

def mostrar_status():

    print("\n========== STATUS ==========")

    print(f"Nome: {jogador['nome']}")
    print(f"Nível: {jogador['nivel']}")
    print(f"Vida: {jogador['vida']}/{jogador['vida_maxima']}")
    print(f"Ataque: {jogador['ataque']}")
    print(f"XP: {jogador['xp']}/{jogador['xp_proximo_nivel']}")
    print(f"Moedas: {jogador['moedas']}")
    print(f"Fase: {jogador['fase']}")

    print("============================")


# mostrar_inventario

def mostrar_inventario():

    print("\n========== INVENTÁRIO ==========")

    print(f"Poções: {jogador['inventario']['pocao']}")

    print("===============================")


# usar_pocao

def usar_pocao():

    if jogador["inventario"]["pocao"] <= 0:

        print("\nVocê não possui poções!")

        return

    if jogador["vida"] == jogador["vida_maxima"]:

        print("\nSua vida já está cheia!")

        return

    cura = 30

    jogador["vida"] += cura

    if jogador["vida"] > jogador["vida_maxima"]:
        jogador["vida"] = jogador["vida_maxima"]

    jogador["inventario"]["pocao"] -= 1

    print("\nVocê usou uma poção!")

    print(
        f"Vida atual: "
        f"{jogador['vida']}/{jogador['vida_maxima']}"
    )


# verificar_nivel

def verificar_nivel():

    while jogador["xp"] >= jogador["xp_proximo_nivel"]:

        jogador["xp"] -= jogador["xp_proximo_nivel"]

        jogador["nivel"] += 1

        jogador["vida_maxima"] += 20

        jogador["vida"] = jogador["vida_maxima"]

        jogador["ataque"] += 5

        jogador["xp_proximo_nivel"] += 50

        print("\nVOCÊ SUBIU DE NÍVEL!")

        print(f"Novo nível: {jogador['nivel']}")


# ganhar_recompensas

def ganhar_recompensas(inimigo):

    jogador["xp"] += inimigo["xp"]

    jogador["moedas"] += inimigo["moedas"]

    print("\n========== RECOMPENSAS ==========")

    print(f"XP ganho: {inimigo['xp']}")
    print(f"Moedas ganhas: {inimigo['moedas']}")

    verificar_nivel()


# atacar

def atacar(inimigo):

    dano = random.randint(
        jogador["ataque"] - 5,
        jogador["ataque"] + 5
    )

    if dano < 1:
        dano = 1

    inimigo["vida"] -= dano

    if inimigo["vida"] < 0:
        inimigo["vida"] = 0

    print("\nVocê atacou!")

    print(f"Dano causado: {dano}")
    print(f"Vida do inimigo: {inimigo['vida']}")


# inimigo_atacar

def inimigo_atacar(inimigo):

    dano = random.randint(
        inimigo["ataque"] - 3,
        inimigo["ataque"] + 3
    )

    if dano < 1:
        dano = 1

    jogador["vida"] -= dano

    if jogador["vida"] < 0:
        jogador["vida"] = 0

    print("\nO inimigo atacou!")

    print(f"Dano recebido: {dano}")

    print(
        f"Sua vida: "
        f"{jogador['vida']}/{jogador['vida_maxima']}"
    )


# iniciar_combate

def iniciar_combate(inimigo):

    print("\n================================")
    print("          COMBATE")
    print("================================")

    print(f"Você encontrou um {inimigo['nome']}!")

    while jogador["vida"] > 0 and inimigo["vida"] > 0:

        print("\n---------- COMBATE ----------")

        print(
            f"Sua vida: "
            f"{jogador['vida']}/{jogador['vida_maxima']}"
        )

        print(f"Vida do inimigo: {inimigo['vida']}")

        print("\n1 - Atacar")
        print("2 - Usar poção")
        print("3 - Fugir")

        opcao = input("\nEscolha: ").strip()

        if opcao == "1":

            atacar(inimigo)

            if inimigo["vida"] <= 0:

                print("\nINIMIGO DERROTADO!")

                ganhar_recompensas(inimigo)

                return True

            inimigo_atacar(inimigo)

        elif opcao == "2":

            vida_antes = jogador["vida"]

            usar_pocao()

            if jogador["vida"] != vida_antes:

                inimigo_atacar(inimigo)

        elif opcao == "3":

            print("\nVocê fugiu!")

            return False

        else:

            print("\nOpção inválida!")

    if jogador["vida"] <= 0:

        print("\nVocê foi derrotado!")

        return False


# criar_inimigo

def criar_inimigo():

    indice = jogador["fase"] - 1

    if indice >= len(inimigos):

        indice = len(inimigos) - 1

    inimigo_base = inimigos[indice]

    inimigo = inimigo_base.copy()

    return inimigo


# explorar

def explorar():

    print("\n================================")
    print(f"          FASE {jogador['fase']}")
    print("================================")

    inimigo = criar_inimigo()

    venceu = iniciar_combate(inimigo)

    if not venceu:

        return False

    if jogador["fase"] >= len(inimigos):

        print("\nVOCÊ TERMINOU TODAS AS FASES!")

        return False

    jogador["fase"] += 1

    print("\nVocê avançou para a próxima fase!")

    print(f"Próxima fase: {jogador['fase']}")

    return True


# menu

def menu():

    while True:

        print("\n================================")
        print("        MENU PRINCIPAL")
        print("================================")

        print("1 - Explorar")
        print("2 - Ver status")
        print("3 - Ver inventário")
        print("4 - Usar poção")
        print("5 - Sair")

        opcao = input("\nEscolha: ").strip()

        if opcao == "1":

            resultado = explorar()

            if not resultado:

                if jogador["vida"] <= 0:

                    print("\nFIM DE JOGO!")

                    break

                if jogador["fase"] >= len(inimigos):

                    break

        elif opcao == "2":

            mostrar_status()

        elif opcao == "3":

            mostrar_inventario()

        elif opcao == "4":

            usar_pocao()

        elif opcao == "5":

            print("\nVocê saiu do jogo.")

            break

        else:

            print("\nOpção inválida!")


# ==========================================================
# INICIAR PROGRAMA
# ==========================================================


# iniciar_jogo

def iniciar_jogo():

    print("================================")
    print("       AVENTURA PYTHON")
    print("================================")

    nome = input("\nDigite o nome do jogador: ").strip()

    if nome == "":
        nome = "Herói"

    jogador["nome"] = nome

    print(f"\nBem-vindo, {jogador['nome']}!")

    print("Sua aventura vai começar...")

    menu()


iniciar_jogo()