'''
9.	Crie o verificador de final de semana e de dia da semana (switch)

'''


print("\n--verificador (switch)--\n")

dia = int(input("Digite o número do dia da semana (1-7): "))

match dia:
    case 1:
        print("Domingo - Final de semana")

    case 2:
        print("Segunda-feira")

    case 3:
        print("Terça-feira")

    case 4:
        print("Quarta-feira")

    case 5:
        print("Quinta-feira")

    case 6:
        print("Sexta-feira")

    case 7:
        print("Sábado - Final de semana")

    case _:
        print("Dia inválido")

print("\n------------------------\n")


