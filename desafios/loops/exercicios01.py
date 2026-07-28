'''
1 - Leitura repetida até entrada válida
Objetivo: usar while para validar input.
Passos:
•	Pergunte por um número positivo.
•	Repita enquanto entrada inválida.

'''


print("\n---Usar while para validar input---\n")


numero = int(input("Digite um número positivo: "))

while numero <= 0:
    print("Número inválido! Digite um número maior que zero.")
    numero = int(input("Digite um número positivo: "))

print("Número válido:", numero)


print("\n----------------------------------------\n")
