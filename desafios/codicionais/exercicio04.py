'''
4.	Sistema de acesso
•	Peça usuário e senha.
•	Se usuário for "admin" e senha "1234", mostre "Bem-vindo!".
•	Caso contrário, "Usuário ou senha incorretos.".


'''

print("\n-----Sistema de acesso-----\n")

usuario = input("Digite seu login: ")
senha = input("Digite sua senha: ")

if usuario == "admin" and senha == "1234": 
    print("Bem-vindo!")
else:
    print("Usuário ou senha incorretos.")

print("\n---------------------------\n")
