'''

12. Função que imprime apenas números ímpares pulando múltiplos de 7
Use for + continue.

	
'''


print("\n---Função que imprime apenas números ímpares pulando múltiplos de 7---\n")

def imprimir_impares():
    for numero in range(1, 51):

        if numero % 7 == 0:
            continue

        if numero % 2 != 0:
            print(numero)

imprimir_impares()


print("\n------------------------------------------------------------------------\n")
