

'''
4. Classe Produto e desconto

Enunciado:
Crie uma classe Produto com preço e um método para aplicar desconto.
'''

print("\n---Classe Produto e desconto---\n")


class Produto:

    def __init__(self, preco):
        self.preco = preco

    def aplicar_desconto(self, desconto):
        self.preco -= desconto


produto = Produto(500)

produto.aplicar_desconto(20)

print(f"Preço final: R$ {produto.preco}")

print("\n-------------------------------\n")



