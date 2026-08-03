'''
1.	Verificação de login básico
•	Pergunte ao usuário um nome de usuário.
•	Se for igual a "admin", exiba "Acesso permitido".
•	Caso contrário, não mostro e nada (por enquanto).
'''

print("\n------------login básico---------------\n")

usuario = input("Digite o nome de usuário: ")

if usuario == "admin":
    print(f" Ola {usuario} Acesso permitido ")

print("\n---------------------------\n")