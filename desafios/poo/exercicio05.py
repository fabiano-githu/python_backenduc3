'''
5.	Classe Livro com status
Enunciado:
 Crie classe Livro com título e um atributo 

'''


print("\n---classe título atributo---\n")

class Livro:
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero

livro = Livro("Dom Casmurro", "Romance")

print(f"Título: {livro.titulo}")
print(f"Gênero: {livro.genero}")



print("\n----------------------------\n")
