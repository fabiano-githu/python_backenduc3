'''


3. Função que calcula o fatorial usando FOR
Crie uma função fatorial(n) que usa um for para calcular o fatorial de um número.

	
'''


print("\n---Função que calcula o fatorial usando FOR---\n")


def fatorial(n):
    resultado = 1

    for i in range(1, n + 1):
        resultado *= i

    return resultado

print(fatorial(5))



print("\n-----------------------------------------------\n")
