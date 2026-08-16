'''
=========================================
 ENUNCIADO: PROJETO ARENA DE BATALHA
🎯 Objetivo do projeto

Criar um jogo de batalha em Python, 
que roda pelo terminal, no qual o jogador escolhe um personagem (herói) 
e enfrenta uma sequência de inimigos em um sistema de fases, 
vencendo um após o outro até se tornar campeão ou até ser derrotado.
=========================================

'''


# =========================================
# DICIONARIOS / LISTAS
# =========================================

personagens = [
    {
        "nome": "Wolverine",
        "vida": 100,
        "ataque": 100,
        "defesa": 500,
        "mana": 8,
        "pocoes": 3,
        "cura_pocao": 20
    },

    {
        "nome": "Homem-Aranha",
        "vida": 500,
        "ataque": 600,
        "defesa": 500,
        "mana": 8,
        "pocoes": 3,
        "cura_pocao": 20
    },

    {
        "nome": "Capitão América",
        "vida": 800,
        "ataque": 200,
        "defesa": 500,
        "mana": 8,
        "pocoes": 3,
        "cura_pocao": 20
    }
]


inimigos = [
    {
        "nome": "Duende Verde",
        "vida": 100,
        "ataque": 100,
        "defesa": 500,
        "mana": 8
    },

    {
        "nome": "Dentes-de-Sabre",
        "vida": 500,
        "ataque": 600,
        "defesa": 500,
        "mana": 8
    },

    {
        "nome": "Ossos Cruzados",
        "vida": 800,
        "ataque": 200,
        "defesa": 500,
        "mana": 8
    }
]


# =========================================
# FUNCAO ESCOLHER PERSONAGEM
# =========================================

def escolher_personagem():

    print("\n🦸 === ESCOLHER PERSONAGEM === 🦸")

    print("1️⃣  - Homem-Aranha 🕷️")
    print("2️⃣  - Capitão América 🛡️")
    print("3️⃣  - Wolverine 🐾")

    opcao = input("👉 Escolha seu personagem: ")

    if opcao == "1":

        print("\n✅ Você escolheu o Homem-Aranha!")
        return personagens[1].copy()

    elif opcao == "2":

        print("\n✅ Você escolheu o Capitão América!")
        return personagens[2].copy()

    elif opcao == "3":

        print("\n✅ Você escolheu o Wolverine!")
        return personagens[0].copy()

    else:

        print("\n❌ Opção inválida!")
        return None


# =========================================
# FUNCAO ESCOLHER INIMIGO
# =========================================

def escolher_inimigo():

    print("\n👹 === ESCOLHER INIMIGO === 👹")

    print("1️⃣  - Duende Verde 🟢")
    print("2️⃣  - Dentes-de-Sabre 🐯")
    print("3️⃣  - Ossos Cruzados 💀")

    opcao = input("👉 Escolha seu inimigo: ")

    if opcao == "1":

        print("\n⚔️ Você enfrentará o Duende Verde!")
        return inimigos[0].copy()

    elif opcao == "2":

        print("\n⚔️ Você enfrentará o Dentes-de-Sabre!")
        return inimigos[1].copy()

    elif opcao == "3":

        print("\n⚔️ Você enfrentará o Ossos Cruzados!")
        return inimigos[2].copy()

    else:

        print("\n❌ Opção inválida!")
        return None


# =========================================
# FUNCAO INICIAR BATALHA
# =========================================

def iniciar_batalha(personagem, inimigo):

    print("\n==============================")
    print("   🔥 INÍCIO DA BATALHA 🔥")
    print("==============================")

    print("\n🦸 JOGADOR")
    print(f"   Nome: {personagem['nome']}")
    print(f"   ❤️  Vida: {personagem['vida']}")
    print(f"   ⚔️  Ataque: {personagem['ataque']}")
    print(f"   🛡️  Defesa: {personagem['defesa']}")
    print(f"   🔮 Mana: {personagem['mana']}")
    print(f"   🧪 Poções: {personagem['pocoes']}")

    print("\n👹 INIMIGO")
    print(f"   Nome: {inimigo['nome']}")
    print(f"   ❤️  Vida: {inimigo['vida']}")
    print(f"   ⚔️  Ataque: {inimigo['ataque']}")
    print(f"   🛡️  Defesa: {inimigo['defesa']}")
    print(f"   🔮 Mana: {inimigo['mana']}")

    print("\n==============================")
    print("     ⚡ BATALHA INICIADA ⚡")
    print("==============================")


# =========================================
# FUNCAO MENU DE BATALHA
# =========================================

def menu_batalha():

    print("\n==============================")
    print("      🎮 MENU DE BATALHA")
    print("==============================")

    print("1️⃣  - Atacar ⚔️")
    print("2️⃣  - Usar poção 🧪")
    print("3️⃣  - Usar magia 🔮")
    print("4️⃣  - Ver status 📊")
    print("5️⃣  - Fugir 🏃")

    opcao = input("👉 Escolha uma ação: ")

    return opcao


# =========================================
# FUNCAO ATACAR
# =========================================

def atacar(personagem, inimigo):

    dano = personagem["ataque"] - inimigo["defesa"]

    if dano < 0:
        dano = 0

    inimigo["vida"] -= dano

    if inimigo["vida"] < 0:
        inimigo["vida"] = 0

    print("\n⚔️ Você atacou o inimigo!")
    print(f"💥 Você causou {dano} de dano!")
    print(f"❤️ Vida do inimigo: {inimigo['vida']}")


# =========================================
# FUNCAO USAR POCAO
# =========================================

def usar_pocao(personagem):

    if personagem["pocoes"] > 0:

        personagem["vida"] += personagem["cura_pocao"]

        personagem["pocoes"] -= 1

        print("\n🧪 Você usou uma poção!")
        print(
            f"💚 Você recuperou "
            f"{personagem['cura_pocao']} de vida!"
        )

        print(f"❤️ Sua vida agora é: {personagem['vida']}")
        print(f"🧪 Poções restantes: {personagem['pocoes']}")

    else:

        print("\n⚠️ Você não possui mais poções!")


# =========================================
# FUNCAO USAR MAGIA
# =========================================

def usar_magia(personagem, inimigo):

    if personagem["mana"] > 0:

        dano_magia = personagem["ataque"] * 2

        inimigo["vida"] -= dano_magia

        if inimigo["vida"] < 0:
            inimigo["vida"] = 0

        personagem["mana"] -= 1

        print("\n🔮 Você usou magia!")
        print(f"💥 A magia causou {dano_magia} de dano!")
        print(f"❤️ Vida do inimigo: {inimigo['vida']}")
        print(f"🔮 Mana restante: {personagem['mana']}")

    else:

        print("\n⚠️ Você não possui mana suficiente!")


# =========================================
# FUNCAO ATAQUE DO INIMIGO
# =========================================

def ataque_inimigo(personagem, inimigo):

    dano = inimigo["ataque"] - personagem["defesa"]

    if dano < 0:
        dano = 0

    personagem["vida"] -= dano

    if personagem["vida"] < 0:
        personagem["vida"] = 0

    print("\n👹 O inimigo atacou você!")
    print(f"💥 O inimigo causou {dano} de dano!")
    print(f"❤️ Sua vida: {personagem['vida']}")


# =========================================
# FUNCAO MOSTRAR STATUS
# =========================================

def mostrar_status(personagem, inimigo):

    print("\n==============================")
    print("     📊 STATUS DO JOGADOR")
    print("==============================")

    print(f"Nome: {personagem['nome']}")
    print(f"❤️  Vida: {personagem['vida']}")
    print(f"⚔️  Ataque: {personagem['ataque']}")
    print(f"🛡️  Defesa: {personagem['defesa']}")
    print(f"🔮 Mana: {personagem['mana']}")
    print(f"🧪 Poções: {personagem['pocoes']}")

    print("\n==============================")
    print("     📊 STATUS DO INIMIGO")
    print("==============================")

    print(f"Nome: {inimigo['nome']}")
    print(f"❤️  Vida: {inimigo['vida']}")
    print(f"⚔️  Ataque: {inimigo['ataque']}")
    print(f"🛡️  Defesa: {inimigo['defesa']}")
    print(f"🔮 Mana: {inimigo['mana']}")


# =========================================
# FUNCAO VERIFICAR VITORIA
# =========================================

def verificar_vitoria(inimigo):

    if inimigo["vida"] <= 0:

        print("\n==============================")
        print("      🏆 VOCÊ VENCEU! 🏆")
        print("==============================")

        print(f"\n☠️ Você derrotou {inimigo['nome']}!")

        return True

    return False


# =========================================
# FUNCAO VERIFICAR DERROTA
# =========================================

def verificar_derrota(personagem):

    if personagem["vida"] <= 0:

        print("\n==============================")
        print("      💀 VOCÊ PERDEU! 💀")
        print("==============================")

        print(f"\n☠️ {personagem['nome']} foi derrotado!")

        return True

    return False


# =========================================
# FUNCAO BATALHA
# =========================================

def batalha(personagem, inimigo):

    iniciar_batalha(personagem, inimigo)

    while True:

        opcao = menu_batalha()

        # =========================================
        # ATAQUE
        # =========================================

        if opcao == "1":

            atacar(personagem, inimigo)

            if verificar_vitoria(inimigo):
                return True  # 🏆 venceu essa fase

            ataque_inimigo(personagem, inimigo)

            if verificar_derrota(personagem):
                return False  # 💀 perdeu o jogo

        # =========================================
        # POCAO
        # =========================================

        elif opcao == "2":

            usar_pocao(personagem)

            ataque_inimigo(personagem, inimigo)

            if verificar_derrota(personagem):
                return False  # 💀 perdeu o jogo

        # =========================================
        # MAGIA
        # =========================================

        elif opcao == "3":

            mana_antes = personagem["mana"]

            usar_magia(personagem, inimigo)

            if personagem["mana"] < mana_antes:

                if verificar_vitoria(inimigo):
                    return True  # 🏆 venceu essa fase

                ataque_inimigo(personagem, inimigo)

                if verificar_derrota(personagem):
                    return False  # 💀 perdeu o jogo

        # =========================================
        # STATUS
        # =========================================

        elif opcao == "4":

            mostrar_status(personagem, inimigo)

        # =========================================
        # FUGIR
        # =========================================

        elif opcao == "5":

            print("\n🏃 Você fugiu da batalha!")

            return False  # fugir também encerra o jogo

        # =========================================
        # OPCAO INVALIDA
        # =========================================

        else:

            print("\n❌ Opção inválida!")


# =========================================
# FUNCAO VER PERSONAGENS
# =========================================

def ver_personagens():

    print("\n==============================")
    print("      🦸 PERSONAGENS 🦸")
    print("==============================")

    for personagem in personagens:

        print(f"\n👤 Nome: {personagem['nome']}")
        print(f"   ❤️  Vida: {personagem['vida']}")
        print(f"   ⚔️  Ataque: {personagem['ataque']}")
        print(f"   🛡️  Defesa: {personagem['defesa']}")
        print(f"   🔮 Mana: {personagem['mana']}")


# =========================================
# FUNCAO VER INIMIGOS
# =========================================

def ver_inimigos():

    print("\n==============================")
    print("        👹 INIMIGOS 👹")
    print("==============================")

    for inimigo in inimigos:

        print(f"\n👤 Nome: {inimigo['nome']}")
        print(f"   ❤️  Vida: {inimigo['vida']}")
        print(f"   ⚔️  Ataque: {inimigo['ataque']}")
        print(f"   🛡️  Defesa: {inimigo['defesa']}")
        print(f"   🔮 Mana: {inimigo['mana']}")


# =========================================
# FUNCAO MODO CAMPANHA (FASES AUTOMATICAS)
# =========================================

def modo_campanha(personagem):

    fase_atual = 0  # começa na primeira fase (índice 0 da lista)
    total_fases = len(inimigos)

    while fase_atual < total_fases:

        inimigo_da_fase = inimigos[fase_atual].copy()

        print("\n==============================")
        print(f"      🚩 FASE {fase_atual + 1} DE {total_fases}")
        print("==============================")

        venceu = batalha(personagem, inimigo_da_fase)

        if not venceu:
            # perdeu ou fugiu -> encerra a campanha
            print("\n💀 Sua jornada termina aqui...")
            return

        # venceu a fase -> avança pro próximo inimigo
        fase_atual += 1

        if fase_atual < total_fases:
            print(f"\n✅ Fase {fase_atual} concluída!")
            print("➡️  Prepare-se para o próximo inimigo...")

    # saiu do while porque venceu TODAS as fases
    print("\n==============================")
    print("   👑 VOCÊ É O CAMPEÃO! 👑")
    print("==============================")
    print(f"\n🎉 {personagem['nome']} derrotou todos os inimigos da arena!")


# =========================================
# MENU PRINCIPAL
# =========================================

while True:

    print("\n")
    print("===========================")
    print("   🏟️  ARENA DE BATALHA 🏟️")
    print("===========================")
    print("           MENU")
    print("---------------------------")
    print("1️⃣  - Jogar 🎮")
    print("2️⃣  - Ver Personagens 🦸")
    print("3️⃣  - Ver Inimigos 👹")
    print("4️⃣  - Sair 🚪")
    print("---------------------------")

    opcao = input("👉 Escolha uma opção: ")

    # =========================================
    # JOGAR
    # =========================================

    if opcao == "1":

        print("\n🎮 Você escolheu Jogar!")

        personagem_escolhido = escolher_personagem()

        if personagem_escolhido is not None:

            modo_campanha(personagem_escolhido)

    # =========================================
    # VER PERSONAGENS
    # =========================================

    elif opcao == "2":

        ver_personagens()

    # =========================================
    # VER INIMIGOS
    # =========================================

    elif opcao == "3":

        ver_inimigos()

    # =========================================
    # SAIR
    # =========================================

    elif opcao == "4":

        print("\n👋 Saindo do jogo...")
        print("🙏 Obrigado por jogar!")

        break

    # =========================================
    # OPCAO INVALIDA
    # =========================================

    else:

        print("\n❌ Opção inválida!")
