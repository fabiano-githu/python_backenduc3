'''


6.Crie uma lista com 3 funcionários (cada um é um dicionário) e depois exiba na seguinte ordem :
ex: 
id: 01   - nome: Valdir   -  cargo: gerente
id: 02   - nome: José   -  cargo: suporte
id: 03   - nome: Maria  -  cargo: analista


'''


print("\n--------Lista de fucionario-------\n")

funcionarios = [
    {
        "id": "01",
        "nome": "Fabiano",
        "cargo": "Analista"
    },
    {
        "id": "02",
        "nome": "Marcela",
        "cargo": "Projetista"
    },
    {
        "id": "03",
        "nome": "Carlos",
        "cargo": "Analista"
    }
]

for funcionario in funcionarios:
    print(
        "id:", funcionario["id"],
        "- nome:", funcionario["nome"],
        "- cargo:", funcionario["cargo"]
    )


print("\n---------------------------\n")
