'''

6. Função que cria um menu simples
Use while para repetir e if para opções:
1 – Somar
 2 – Subtrair
 0 – Sair

	
'''


print("\n------------------6. Função que cria um menu simples -----------------\n")


def menu():
    while True:
        print("1 - Somar")
        print("2 - Subtrair")
        print("0 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            print("Você escolheu Somar")
        elif opcao == 2:
            print("Você escolheu Subtrair")
        elif opcao == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida")

menu()



print("\n------------------------------------------------------------------------\n")
