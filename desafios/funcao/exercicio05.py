'''


5. Função que soma valores até o usuário digitar 0
Use while + break.


'''


print("\n------------Função que soma valores até o usuário digitar 0----------\n")


def somar_valores():
    soma = 0

    while True:
        valor = int(input("Digite um valor (0 para parar): "))

        if valor == 0:
            break

        soma += valor

    print("Soma dos valores:", soma)

somar_valores()


print("\n----------------------------------------------------------------------\n")
