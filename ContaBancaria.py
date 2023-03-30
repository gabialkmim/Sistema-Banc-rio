
class ContaBancaria:
    def __init__(self):
        self.saldo = 0.0
        self.depositos = []
        self.saques = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > 0 and valor <= 500 and len(self.saques) < 3:
            if valor <= self.saldo:
                self.saldo -= valor
                self.saques.append(valor)
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Valor inválido para saque ou limite de saques diários atingido.")

    def extrato(self):
        print("Extrato:")
        for deposito in self.depositos:
            print(f"  Depósito: R$ {deposito:.2f}")
        for saque in self.saques:
            print(f"  Saque: R$ {saque:.2f}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")


conta = ContaBancaria()

conta.depositar(100.0)
conta.depositar(-38.5)
conta.sacar(200.0)
conta.depositar(350.50)
conta.depositar(638.97)
conta.sacar(235.00)

conta.extrato()
