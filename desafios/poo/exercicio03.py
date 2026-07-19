
'''
3. Contador simples

Enunciado:
Crie uma classe que represente um contador com um valor que começa em 0.
Crie métodos para aumentar e diminuir.
'''

print("\n------ Contador Simples ------\n")


class Contador:

    def __init__(self):
        self.valor = 0

    def aumentar(self):
        self.valor += 1

    def diminuir(self):
        self.valor -= 1


contador = Contador()

contador.aumentar()
contador.aumentar()
contador.diminuir()

print(contador.valor)




print("\n-------------------------------\n")
