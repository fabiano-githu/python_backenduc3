'''

2- Soma acumulada com while
Objetivo: acumular valores com loop.	
Passos:
Peça valores até o usuário digitar 0.
Some e exiba total.

	
'''


print("\n------Soma acumulada com while------\n")


soma = 0

numero = input("Digite um número (Enter para sair): ")

while numero != "":
    soma += int(numero)
    numero = input("Digite outro número (Enter para sair): ")

print("A soma total é:", soma)


print("\n----------------------------------------\n")
