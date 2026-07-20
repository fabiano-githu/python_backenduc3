'''
5.	Percorra o dicionário do exercício 1 e imprimindo chave → valor.

'''



print("\n--------Lista de Funcionários---------\n")


# Cria uma lista chamada funcionarios
# Essa lista vai guardar vários dicionários
funcionarios = [

    # Primeiro funcionário (dicionário)
    {
        # Chave nome recebe o valor Fabiano
        "nome": "Fabiano",

        # Chave idade recebe o valor 23
        "idade": 23,

        # Chave cargo recebe o valor Programador
        "cargo": "Programador",

        # Chave cidade recebe o valor RJ
        "cidade": "RJ"
    },


    # Segundo funcionário (dicionário)
    {
        # Chave nome recebe o valor Marcela
        "nome": "Marcela",

        # Chave idade recebe o valor 44
        "idade": 44,

        # Chave cargo recebe o valor Analista
        "cargo": "Analista",

        # Chave cidade recebe o valor Camará
        "cidade": "Camará"
    }

]


# Cria uma variável contador
# Ela será usada para numerar os funcionários
contador = 1


# Percorre a lista de funcionários
# A cada repetição pega um funcionário
for funcionario in funcionarios:


    # Mostra o número do funcionário atual
    print(f"\nFuncionário {contador}")


    # Percorre o dicionário do funcionário atual
    # items() retorna chave e valor juntos
    for chave, valor in funcionario.items():


        # Exibe a chave e o valor
        # Exemplo: nome → Fabiano
        print(chave, "→", valor)


    # Aumenta o contador em 1
    # Exemplo: 1 passa para 2
    contador += 1


# Exibe uma linha final para organização
print("\n---------------------------\n")


