import random


class Personagem:

    def __init__(self, dados):
        self.nome = dados["nome"]
        self.vida = dados["vida"]
        self.vida_maxima = dados["vida"]
        self.ataque = dados["ataque"]
        self.defesa = dados["defesa"]
        self.mana = dados.get("mana", 50)
        self.mana_maxima = self.mana
        self.pocoes = dados.get("pocoes", 3)
        self.esquiva = dados.get("esquiva", 20)
        self.critico = dados.get("critico", 20)

    # ==========================
    # VERIFICAR SE ESTÁ VIVO
    # ==========================

    def esta_vivo(self):
        return self.vida > 0

    # ==========================
    # CALCULAR DANO
    # ==========================

    def calcular_dano(self, defensor):

        ataque_aleatorio = random.randint(
            self.ataque - 10,
            self.ataque + 10
        )

        dano = ataque_aleatorio - defensor.defesa

        if dano <= 0:
            dano = 0

        # Ataque crítico
        if random.randint(1, 100) <= self.critico:

            dano *= 2

            print(" ATAQUE CRÍTICO!")
            print(" Dano dobrado!")

        return dano

    # ==========================
    # ATAQUE
    # ==========================

    def atacar(self, defensor):

        # Chance de esquiva
        if random.randint(1, 100) <= defensor.esquiva:

            print(
                f"🌀 {defensor.nome} "
                f"ESQUIVOU do ataque!"
            )

            return

        dano = self.calcular_dano(defensor)

        defensor.vida -= dano

        if defensor.vida <= 0:
            defensor.vida = 0

        print(
            f"⚔️ {self.nome} atacou "
            f"{defensor.nome}!"
        )

        print(
            f"💥 Dano: {dano}"
        )

        print(
            f"❤️ Vida de {defensor.nome}: "
            f"{defensor.vida}/{defensor.vida_maxima}"
        )

    # ==========================
    # MAGIA
    # ==========================

    def usar_magia(self, defensor):

        custo_mana = 20
        dano_magia = 40

        if self.mana < custo_mana:

            print("❌ Mana insuficiente!")

            return False

        self.mana -= custo_mana

        # Esquiva da magia
        if random.randint(1, 100) <= defensor.esquiva:

            print(
                f"🌀 {defensor.nome} "
                f"ESQUIVOU da magia!"
            )

            return True

        dano = dano_magia - defensor.defesa

        if dano <= 0:
            dano = 0

        defensor.vida -= dano

        if defensor.vida <= 0:
            defensor.vida = 0

        print(
            f"✨ {self.nome} lançou magia "
            f"contra {defensor.nome}!"
        )

        print(
            f"💥 Dano mágico: {dano}"
        )

        print(
            f"🔵 Mana: "
            f"{self.mana}/{self.mana_maxima}"
        )

        print(
            f"❤️ Vida de {defensor.nome}: "
            f"{defensor.vida}/{defensor.vida_maxima}"
        )

        return True

    # ==========================
    # POÇÃO
    # ==========================

    def usar_pocao(self):

        if self.pocoes <= 0:

            print("❌ Você não possui poções!")

            return False

        if self.vida == self.vida_maxima:

            print("❤️ Sua vida já está cheia!")

            return False

        cura = 30

        self.vida += cura

        if self.vida > self.vida_maxima:
            self.vida = self.vida_maxima

        self.pocoes -= 1

        print("🧪 Poção utilizada!")

        print(
            f"❤️ Vida: "
            f"{self.vida}/{self.vida_maxima}"
        )

        print(
            f"🧪 Poções restantes: "
            f"{self.pocoes}"
        )

        return True


# ==================================================
# FUNÇÃO PRINCIPAL DA BATALHA
# ==================================================

def jogar_batalha():

   
    # DICIONÁRIO DO JOGADOR
    

    dados_jogador = {
        "nome": "Thor",
        "vida": 100,
        "ataque": 60,
        "defesa": 10,
        "mana": 50,
        "pocoes": 3,
        "esquiva": 20,
        "critico": 20
    }

    # DICIONÁRIOS DOS INIMIGOS
    

    dados_inimigos = [

        {
            "nome": "Loki",
            "vida": 80,
            "ataque": 25,
            "defesa": 10,
            "mana": 30,
            "esquiva": 20,
            "critico": 15
        },

        {
            "nome": "Hulk",
            "vida": 120,
            "ataque": 35,
            "defesa": 15,
            "mana": 30,
            "esquiva": 10,
            "critico": 15
        },

        {
            "nome": "Thanos",
            "vida": 200,
            "ataque": 50,
            "defesa": 20,
            "mana": 50,
            "esquiva": 10,
            "critico": 20
        }
    ]

   
    # CRIANDO OS OBJETOS
   

    jogador = Personagem(dados_jogador)

    inimigos = []

    for dados in dados_inimigos:
        inimigo = Personagem(dados)
        inimigos.append(inimigo)

 
    # INÍCIO
  

    print("\n================================")
    print("       ⚔️ BATALHA RPG ⚔️")
    print("================================")

  
    # ENFRENTA OS INIMIGOS
    

    for inimigo in inimigos:

        print("\n================================")
        print(f"👹 INIMIGO: {inimigo.nome}")
        print("================================")

        while jogador.esta_vivo() and inimigo.esta_vivo():

    
            # STATUS
         

            print("\n-------------------------------")
            print("          STATUS")
            print("-------------------------------")

            print(
                f"❤️ Vida: "
                f"{jogador.vida}/{jogador.vida_maxima}"
            )

            print(
                f"🔵 Mana: "
                f"{jogador.mana}/{jogador.mana_maxima}"
            )

            print(
                f"🧪 Poções: "
                f"{jogador.pocoes}"
            )

            print(
                f"\n👹 {inimigo.nome}: "
                f"{inimigo.vida}/{inimigo.vida_maxima}"
            )

           
            # MENU
           

            print("\n===== ESCOLHA =====")
            print("1 - ⚔️ Atacar")
            print("2 - ✨ Magia")
            print("3 - 🧪 Poção")

            escolha = input("Escolha: ")

          
            # ATAQUE
            

            if escolha == "1":

                jogador.atacar(inimigo)

           
            # MAGIA
          

            elif escolha == "2":

                jogador.usar_magia(inimigo)

            
            # POÇÃO
           

            elif escolha == "3":

                jogador.usar_pocao()

           
            # OPÇÃO INVÁLIDA
           

            else:

                print("❌ Opção inválida!")

                continue

            
            # INIMIGO MORREU
           

            if not inimigo.esta_vivo():

                print(
                    f"\n💀 {inimigo.nome} foi derrotado!"
                )

                break

         
            # TURNO DO INIMIGO
           

            print(
                f"\n--- 👹 Turno de {inimigo.nome} ---"
            )

            inimigo.atacar(jogador)

          
            # JOGADOR MORREU
           

            if not jogador.esta_vivo():

                print("\n💀 VOCÊ FOI DERROTADO!")

                break

        # Se jogador morreu, termina o jogo
        if not jogador.esta_vivo():
            break

    
    # RESULTADO
   

    if jogador.esta_vivo():

        print("\n================================")
        print("          🏆 VITÓRIA!")
        print("================================")

        return True

    else:

        print("\n================================")
        print("          💀 DERROTA!")
        print("================================")

        return False


# ==================================================
# PROGRAMA PRINCIPAL
# ==================================================

while True:

    jogar_batalha()

    print("\n================================")
    resposta = input("Deseja jogar novamente? (sim/não): ")
    print("================================")

    resposta = resposta.strip().lower()

    if resposta == "não" or resposta == "nao":

        print("\n Obrigado por jogar!")
        break

    elif resposta == "sim":

        print("\n🔄 Iniciando uma nova batalha...")

    else:

        print(
            "\n Resposta inválida."
        )

        print(
            "Digite apenas: sim ou não."
        )