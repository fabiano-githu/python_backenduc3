'''
1.PessoaCrie uma classe Pessoa
Enunciado:
 Crie uma classe Pessoa com nome e idade. Depois crie um objeto e imprima seus dados.


'''


print("\n-----classe Pessoa nome e idade objeto que imprime seus dados ------\n")

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa = Pessoa("Maria", 23)

print(f"Nome: {pessoa.nome}")
print(f"Idade: {pessoa.idade}")


print("\n--------------------------------------------------------------------\n")
