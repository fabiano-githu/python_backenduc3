'''

3- Filtrar itens com for + if (par/impar)
Objetivo: combinar loops e condicionais.
Passos:
Itere 1..20 e exiba apenas pares.

'''


print("\n---Filtrar itens com for + if---\n")

for numero in range(1, 21):
    if numero % 2 == 0:
        print(f"o número é :{numero}")

print("\n---------------------------------\n")
