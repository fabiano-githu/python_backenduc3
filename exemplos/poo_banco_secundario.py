# Encapsulamento

class Banco:

    def __init__(self, saldo=0):
        self.__saldo = saldo

    @property
    def saldo_E50(self):
        return self.__saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor deve ser positivo")

        self.__saldo += valor

    def debitar(self, valor):
        if valor <= 0:
            raise ValueError("O valor deve ser positivo")

        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            raise ValueError("Saldo insuficiente")


# =================================
# BANCO MASTER
# =================================

banco_master = Banco(100)

print("===== BANCO MASTER =====")

print("Saldo inicial:", banco_master.saldo_E50)

banco_master.depositar(150)
print("Depois do depósito:", banco_master.saldo_E50)

banco_master.debitar(50)
print("Depois do débito:", banco_master.saldo_E50)


# =================================
# BANCO SECUNDÁRIO
# =================================

banco_secundario = Banco(500)

print("\n===== BANCO SECUNDÁRIO =====")

print("Saldo inicial:", banco_secundario.saldo_E50)

banco_secundario.depositar(300)
print("Depois do depósito:", banco_secundario.saldo_E50)

banco_secundario.debitar(100)
print("Depois do débito:", banco_secundario.saldo_E50)