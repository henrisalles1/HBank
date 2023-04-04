
class Conta:
    numero_conta = 0
    def __init__(self, limite):
        Conta.numero_conta += 1
        self.numero_conta: int = Conta.numero_conta
        self.limite: float = limite
        self.limite_atual: float = limite
        self.saldo: float = 0

    def saque(self, valor):
        if self.verifica_pode_retirar(valor):
            self.saldo -= valor
            self.ajuste_limite()
            print(f'Efetuado o saque no valor de {valor}')
        else:
            raise ValueError('Saque nao efetuado por falta de limite')

    def verifica_pode_retirar(self, valor):
        if valor < self.saldo + self.limite_atual:
            return True
        else:
            return False

    def ajuste_limite(self):
        if self.saldo < 0:
            self.limite_atual = self.saldo
        else:
            pass

conta = Conta(1000)
conta.saque(999)
conta.saque(1)
print(conta.saldo)
print(conta.limite_atual)