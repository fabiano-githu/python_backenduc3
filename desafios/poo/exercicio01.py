'''
1.PessoaCrie uma classe Pessoa
Enunciado:
 Crie uma classe Pessoa com nome e idade. Depois crie um objeto e imprima seus dados.


'''


print("\n-----classe Pessoa nome e idade objeto que imprime seus dados ------\n")

class Pessoa:

    #Atributo do objetos
    def __init__(self, nome, idade, Profissao):
        self.nome = nome
        self.idade = idade
        self.Profissao = Profissao

pessoa = Pessoa("Maria", 23, "analista")
pessoa1 = Pessoa("Fabiano", 44, "programador")
pessoa2 = Pessoa("Marcela ", 35, "Projetista")
pessoa3 = Pessoa("Marina", 66, "crochê")
pessoa4 = Pessoa("Rosângela", 23, "analista")

print(f"Nome: {pessoa.nome}")
print(f"Idade: {pessoa.idade}")
print(f"Profissão: {pessoa.Profissao}")

print("\n-------\n")

print(f"Nome: {pessoa1.nome}")
print(f"Idade: {pessoa1.idade}")
print(f"Profissão: {pessoa1.Profissao}")

print("\n-------\n")

print(f"Nome: {pessoa2.nome}")
print(f"Idade: {pessoa2.idade}")
print(f"Profissão: {pessoa2.Profissao}")

print("\n-------\n")

print(f"Nome: {pessoa3.nome}")
print(f"Idade: {pessoa3.idade}")
print(f"Profissão: {pessoa3.Profissao}")

print("\n-------\n")

print(f"Nome: {pessoa4.nome}")
print(f"Idade: {pessoa4.idade}")
print(f"Profissão: {pessoa4.Profissao}")





print("\n--------------------------------------------------------------------\n")
