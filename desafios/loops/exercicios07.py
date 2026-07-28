'''

7 - continue para pular negativos
•	Objetivo: somar números positivos da lista [-1,2,-3,4], pulando negativos com continue.
•	Usar: for, continue.
•	Dica: if n < 0: continue.


'''


print("\n---Somar números positivos da lista---\n")

lista = [-1, 2, -3, 4]

soma = 0

for n in lista:
    if n < 0:
        continue

    soma += n

print(soma)


'''

Para cada número na lista:

    Se o número for menor que 0:

        Pule para a próxima repetição.

    Senão:

        Some o número.

No final, mostre a soma.


'''


print("\n----------------------------------------\n")
