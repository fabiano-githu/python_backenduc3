'''

8. Função que conta números pares em um intervalo
Exemplo: contar_pares(1, 20) → quantos pares existem?

	
'''


print("\n---Função que conta números pares em um intervalo---\n")


def contar_pares(inicio, fim):
    contador = 0

    for numero in range(inicio, fim + 1):
        if numero % 2 == 0:
            contador += 1

    return contador


print(contar_pares(1, 20))




print("\n------------------------------------------------------------------------\n")
