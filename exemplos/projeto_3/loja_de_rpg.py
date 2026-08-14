
# ==========================================
#      LOJA DE RPG
# ==========================================


#PRODUTOS DA LOJA


produtos = {
    "espada": {
        "preco": 100,
        "categoria": "Arma",
        "lendario": False,
        "estoque": 10
    },

    "escudo": {
        "preco": 80,
        "categoria": "Defesa",
        "lendario": False,
        "estoque": 5
    },

    "pocao": {
        "preco": 30,
        "categoria": "Poção",
        "lendario": False,
        "estoque": 20
    },

    "arco": {
        "preco": 70,
        "categoria": "Arma",
        "lendario": False,
        "estoque": 8
    },

    "excalibur": {
        "preco": 500,
        "categoria": "Arma",
        "lendario": True,
        "estoque": 1
    }
}



#DADOS DO JOGADOR


saldo = 600

inventario = {}



#FUNÇÃO DE DESCONTO


def aplicar_desconto(preco, desconto):

    valor_desconto = preco * desconto / 100

    preco_final = preco - valor_desconto

    return preco_final



#VISUALIZAR PRODUTOS


def visualizar_produtos():

    print("\n==========  PRODUTOS ==========")

    for nome, produto in produtos.items():

        print(f"\nNome: {nome}")
        print(f"Preço: R$ {produto['preco']:.2f}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Estoque: {produto['estoque']}")

        if produto["lendario"]:
            print(" ITEM LENDÁRIO")



#CONSULTAR PREÇO

def consultar_preco():

    produto = input("\nDigite o nome do produto: ").lower().strip()

    if produto not in produtos:

        print(" Item inexistente!")

        return

    preco = produtos[produto]["preco"]

    print(f"\ {produto}: R$ {preco:.2f}")



#COMPRAR PRODUTO


def comprar():

    global saldo

    produto = input("\nDigite o produto que deseja comprar: ").lower().strip()

    # Verifica se o produto existe
    if produto not in produtos:

        print("  Item inexistente!")

        return

    quantidade = int(input("Digite a quantidade: "))

    # Verifica quantidade
    if quantidade <= 0:

        print(" Quantidade inválida!")

        return

    # Verifica estoque
    estoque = produtos[produto]["estoque"]

    if quantidade > estoque:

        print(" Estoque insuficiente!")

        return

    # Pega o preço
    preco = produtos[produto]["preco"]

    # Calcula o valor total
    total = preco * quantidade

    # Desconto de 10% para compras acima de R$ 200
    desconto = 0

    if total >= 200:

        desconto = 10

        total = aplicar_desconto(total, desconto)

        print("\n  Desconto de 10% aplicado!")

    # Verifica saldo
    if saldo < total:

        print("\n Saldo insuficiente!")

        print(f"Saldo: R$ {saldo:.2f}")
        print(f"Total: R$ {total:.2f}")

        return

    # Realiza a compra
    saldo -= total

    produtos[produto]["estoque"] -= quantidade

    # Adiciona ao inventário
    if produto in inventario:

        inventario[produto] += quantidade

    else:

        inventario[produto] = quantidade

    print("\n COMPRA REALIZADA!")

    print(f"Produto: {produto}")
    print(f"Quantidade: {quantidade}")
    print(f"Total: R$ {total:.2f}")
    print(f"Saldo restante: R$ {saldo:.2f}")



#            MOSTRAR INVENTÁRIO


def mostrar_inventario():

    print("\n========== INVENTÁRIO ==========")

    if not inventario:

        print("Seu inventário está vazio.")

        return

    for produto, quantidade in inventario.items():

        print(f"{produto} → {quantidade} unidade(s)")


#  MOSTRAR SALDO


def mostrar_saldo():

    print("\n==========  SALDO ==========")

    print(f"Saldo disponível: R$ {saldo:.2f}")



# VENDER ITEM


def vender():

    global saldo

    produto = input("\nDigite o item que deseja vender: ").lower().strip()

    # Verifica se o jogador possui o item
    if produto not in inventario:

        print("❌ Você não possui esse item!")

        return

    quantidade = int(input("Digite a quantidade que deseja vender: "))

    # Verifica quantidade
    if quantidade <= 0:

        print("❌ Quantidade inválida!")

        return

    # Verifica se possui quantidade suficiente
    if quantidade > inventario[produto]:

        print("❌ Você não possui essa quantidade!")

        return


    preco = produtos[produto]["preco"]

   
    valor_venda = preco * 0.70

    total = valor_venda * quantidade

   
    saldo += total

    inventario[produto] -= quantidade

    
    if inventario[produto] == 0:

        del inventario[produto]

  
    produtos[produto]["estoque"] += quantidade

    print("\n VENDA REALIZADA!")

    print(f"Produto: {produto}")
    print(f"Quantidade: {quantidade}")
    print(f"Valor recebido: R$ {total:.2f}")
    print(f"Novo saldo: R$ {saldo:.2f}")



#  MOSTRAR ITENS LENDÁRIOS


def mostrar_lendarios():

    print("\n==========  ITENS LENDÁRIOS ==========")

    encontrou = False

    for nome, produto in produtos.items():

        if produto["lendario"]:

            encontrou = True

            print(f"\n {nome}")
            print(f"Preço: R$ {produto['preco']:.2f}")
            print(f"Categoria: {produto['categoria']}")
            print(f"Estoque: {produto['estoque']}")

    if not encontrou:

        print("Nenhum item lendário disponível.")


# ==========================================
#         MENU PRINCIPAL
# ==========================================

def menu():

    while True:

        print("\n")
        print("================================")
        print("        LOJA DE RPG")
        print("================================")
        print("1 -  Visualizar produtos")
        print("2 -  Consultar preço")
        print("3 -  Comprar")
        print("4 -  Ver saldo")
        print("5 -  Ver inventário")
        print("6 -  Vender item")
        print("7 -  Ver itens lendários")
        print("8 -  Sair")
        print("================================")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":

            visualizar_produtos()

        elif opcao == "2":

            consultar_preco()

        elif opcao == "3":

            comprar()

        elif opcao == "4":

            mostrar_saldo()

        elif opcao == "5":

            mostrar_inventario()

        elif opcao == "6":

            vender()

        elif opcao == "7":

            mostrar_lendarios()

        elif opcao == "8":

            print("\nSaindo da loja...")
            break

        else:

            print("\n Opção inválida!")


# ==========================================
# ▶ INICIAR PROGRAMA
# ==========================================

menu()