import random


class Personagem:

    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def calcular_dano(self, defensor):

        # Ataque aleatório
        ataque_aleatorio = random.randint(
            self.ataque - 10,
            self.ataque + 10
        )

        dano = ataque_aleatorio - defensor.defesa

        if dano <= 0:
            dano = 0

        return dano

    def atacar(self, defensor):

        dano = self.calcular_dano(defensor)

        defensor.vida -= dano

        if defensor.vida <= 0:
            defensor.vida = 0

        print(
            f"{self.nome} atacou {defensor.nome}, "
            f"causando {dano} de dano."
        )

        print(
            f"Vida de {defensor.nome}: "
            f"{defensor.vida}"
        )

    def esta_vivo(self):
        return self.vida > 0


# ==========================
# JOGADOR
# ==========================

jogador = Personagem(
    "Thor",
    500,
    60,
    10
)


# ==========================
# VÁRIOS INIMIGOS
# ==========================

inimigos = [

    Personagem(
        "Loki",
        80,
        25,
        10
    ),

    Personagem(
        "Hulk",
        120,
        35,
        15
    ),

    Personagem(
        "Thanos",
        200,
        50,
        20
    )
]


# ==========================
# BATALHA
# ==========================

print("===== BATALHA =====")

for inimigo in inimigos:

    if not jogador.esta_vivo():
        break

    print(f"\n⚔️ Você encontrou {inimigo.nome}!")

    while jogador.esta_vivo() and inimigo.esta_vivo():

        # --------------------------
        # TURNO DO JOGADOR
        # --------------------------

        print("\n--- Turno do jogador ---")

        jogador.atacar(inimigo)

        # Verifica se o inimigo morreu
        if not inimigo.esta_vivo():

            print(
                f"\n💀 {inimigo.nome} foi derrotado!"
            )

            break


        # --------------------------
        # TURNO DO INIMIGO
        # --------------------------

        print("\n--- Turno do inimigo ---")

        inimigo.atacar(jogador)

        # Verifica se o jogador morreu
        if not jogador.esta_vivo():

            print("\n💀 VOCÊ FOI DERROTADO!")
            break


# ==========================
# RESULTADO FINAL
# ==========================

if jogador.esta_vivo():

    print("\n🏆 VITÓRIA!")
    print("Você derrotou todos os inimigos!")

else:

    print("\n💀 DERROTA!")
    print("Você foi derrotado.")