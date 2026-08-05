'''
8. Criar dicionário com input do usuário
Enunciado:
Peça nome, idade e setor e salve em um dicionário.


'''


print("\n--------Menu escolha-------\n")


funcionario = {}

funcionario["nome"] = input("Digite o nome: ")
funcionario["idade"] = int(input("Digite a idade: "))
funcionario["setor"] = input("Digite o setor: ")

print(funcionario)

print("\n---------------------------\n")
