'''
5.	Percorra o dicionário do exercício 1 e imprimindo chave → valor.

'''



print("\n--------Fucionario 1---------\n")


funcionario = {
    "nome": "Carlos",
    "idade": 23,
    "cargo": "Programador"
}

funcionario["cidade"] = "Rj"
funcionario["nome"] = "Fabiano"

for chave, valor in funcionario.items():
    print(chave, "→", valor)
    





print("\n---------------------------\n")
