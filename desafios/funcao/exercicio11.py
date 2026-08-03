'''

11. Função que simula três tentativas de login
Use while com contador + if.

	
'''


print("\n---Função que simula três tentativas de login---\n")

def login():
    tentativas = 0

    while tentativas < 3:
        senha = input("Digite a senha: ")

        if senha == "python123":
            print("Login realizado com sucesso")
            break
        else:
            print("Senha incorreta")

        tentativas += 1

    if tentativas == 3:
        print("Número de tentativas excedido")


login()

print("\n---------------------------------------------------\n")
