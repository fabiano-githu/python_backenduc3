'''
10.	Crie um menu de escolha utilizando número a escolha tem de ser 1a 5 e no final deve mostrar o número escolhido.

'''


print("\n--------Menu escolha-------\n")

print("1 - Opção 1")
print("2 - Opção 2")
print("3 - Opção 3")
print("4 - Opção 4")
print("5 - Opção 5")

escolha = int(input("\nDigite uma opção de 1 a 5: "))

if escolha >= 1 and escolha <= 5:
    print(f"O número escolhido foi: {escolha}")
else:
    print("Opção inválida!")

print("\n---------------------------\n")
