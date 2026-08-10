'''
#Class sem instancia
class Carro:
    pass # ainda vazia, só o modelo 

'''

'''
# Como criar objetos (instancia)

class Carro:
    def __init__(self, marca):
        self.marca = marca

meu_carro = Carro("Toyota") #criando objeto (instanciar)
print(type(meu_carro.marca))
print(meu_carro.marca)
'''
# Encapsulamento

class Banco:

    def __init__(self, saldo=0):
        self.__saldo = saldo

    # ENCAPSULAMENTO:
    # @property permite consultar o __saldo de forma controlada.
    @property
    def saldo_E50(self):
        return self.__saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor deve ser positivo")
        
        #  ENCAPSULAMENTO:
        # O saldo não é alterado diretamente pelo usuário.
        # A própria classe controla a alteração.
        self.__saldo += valor

    def debitar(self, valor):
        if valor <= 0:
            raise ValueError("O valor deve ser positivo")

        if valor <= self.__saldo:

            #  ENCAPSULAMENTO:
            # A classe controla a retirada do dinheiro
            # e só permite a operação se houver saldo.
            self.__saldo -= valor
        else:
            raise ValueError("Saldo insuficiente")


# Herança
class Conta(Banco):

    def __init__(self, saldo, agencia, num_conta, cliente):
        super().__init__(saldo)

        self.agencia = agencia
        self.num_conta = num_conta
        self.cliente = cliente

    def __str__(self):
        return (
            f"Cliente: {self.cliente}\n"
            f"Conta: {self.num_conta}\n"
            f"Agência: {self.agencia}\n"
        )


conta1 = Conta(200, 452, "236252829928-1", "Bruno Gomes")
conta2 = Conta(200, 452, "236251239289-1", "Márcia Luiza")

print("\n======CONTAS CLIENTES======")

print("\n-------CONTA1-------")

print(
    f"Cliente: {conta1.cliente}\n"
    f"Agência: {conta1.agencia}\n"
    f"Conta: {conta1.num_conta}\n"
    f"Saldo: {conta1.saldo_E50}"
)

print("\n-------CONTA2-------")

print(
    f"Cliente: {conta2.cliente}\n"
    f"Agência: {conta2.agencia}\n"
    f"Conta: {conta2.num_conta}\n"
    f"Saldo: {conta2.saldo_E50}"
)

print("\n========================\n")