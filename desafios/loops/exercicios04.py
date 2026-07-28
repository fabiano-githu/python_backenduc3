'''
4- Soma até zero
•	Objetivo: ler números até o usuário digitar 0; mostrar a soma.
•	Usar: while, input.
•	Dica: verifique antes de somar se o número é 0 para encerrar.

'''


print("\n--ler até digitar 0; mostrar a soma ----\n")

soma = 0

while True:
    numero = int(input("Digite um número (0 para sair): "))

    if numero == 0:
        break

    soma += numero

print(f"A soma total é: {soma}")









print("\n----------------------------------------\n")
