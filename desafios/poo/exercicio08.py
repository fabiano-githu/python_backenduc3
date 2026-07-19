'''
8.	Classe com contador de objetos
Enunciado:
 Conte quantos objetos foram criados.

'''


print("\n--Classe contador objetos--\n")



class Pessoa:
    contador = 0

    def __init__(self):
        Pessoa.contador += 1



print("\n---------------------------\n")
