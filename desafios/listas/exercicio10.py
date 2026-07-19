
'''
Questão 10
Solicite ao usuário que digite 5 números.
Armazene esses números em uma lista.
Ao final, exiba:
•	A lista completa. 
•	A soma dos números digitados.

'''


print("\n--------Idade mínima-------\n")

numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

print(f"\nLista completa: {numeros}")
print(f"Soma dos números: {sum(numeros)}")

print("\n---------------------------\n")
