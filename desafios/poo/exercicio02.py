'''
2.	Classe Aluno com método estudar
Enunciado:
 Crie uma classe Aluno que tenha nome e um método estudar() que imprime uma mensagem.

	
'''


print("\n---Crie classe Aluno nome método estudar() que imprime uma mensagem ---\n")

class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def estudar(self):
        print(f"{self.nome} está estudando Python.")

aluno = Aluno("Maria")

aluno.estudar()

print("\n------------------------------------------------------------------------\n")
