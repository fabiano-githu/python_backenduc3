'''
4.	Sistema de acesso
•	Peça usuário e senha.
•	Se usuário for "admin" e senha "1234", mostre "Bem-vindo!".
•	Caso contrário, "Usuário ou senha incorretos.".

'''
usuario = "fabiano"
senha = input(" Digite senha: ")

if senha == "1234" :
    print("Acesso liberado!")
else:
    print("Acesso negado!")

