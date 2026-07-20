'''

7. Atualizar vários campos de uma vez.
Atualize o funcionário com:
cargo = “Sênior”
salário = 5000


'''


print("\n--------Menu escolha-------\n")


funcionario = {
    "nome": "Carlos",
    "idade": 23,
    "cargo": "Programador"
}

funcionario.update({
    "cargo": "Sênior",
    "salario": 5000
})

print(funcionario)





print("\n---------------------------\n")
