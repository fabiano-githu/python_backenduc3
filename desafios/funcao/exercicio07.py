'''
7. Função que valida senha
Peça ao usuário uma senha.
Enquanto a senha for diferente de "python123", repita com while.
'''


print("\n------------------6. Função que cria um menu simples -----------------\n")


def validar_senha():
    senha = input("Digite a senha: ")

    while senha != "python123":
        senha = input("Digite a senha: ")

    print("Senha válida!")


validar_senha()

print("\n------------------------------------------------------------------------\n")
