from dirConta.Pessoa import Pessoa
from dirConta.Telefone import Telefone
from dirConta.Senha import Senha


class Conta:
    numero_conta = 0
    limite = 1000

    def __init__(self, Pessoa, telefone: str, senha: str):
        self.__Nome_completo = f'{Pessoa.primeiro_nome} {Pessoa.sobrenome}'
        self.__Pessoa = Pessoa
        self._documento = Pessoa.Doc
        self.telefone_preferivel = Telefone(telefone)
        self.telefone_pessoal = Pessoa.telefone
        self.__senha = Senha(senha).senha
        self.__limite = Conta.limite
        self.limite_atual = self.limite
        self.__saldo = 0

    def __str__(self):
        return f'Nome: {self.__Nome_completo}\n' \
               f'{self._documento}\n' \
               f'Telefone: {self.telefone_preferivel}\n'

    def saque(self, valor):
        self.digite_sua_senha()
        if self.verifica_pode_retirar(valor):
            self.ajuste_saldolimite(valor)
            print(f'Efetuado o saque no valor de {valor}')

    def deposito(self, valor):
        self.__saldo += valor

    def transferencia(self, destino, valor):
        self.digite_sua_senha()
        if self.verifica_pode_retirar(valor):
            self.ajuste_saldolimite(valor)
            destino.deposito(valor)
            print(f'Efetuado a transferencia no valor de {valor}')

    def ajuste_saldolimite(self, valor):
        if valor > self.__saldo:
            self.limite_atual -= valor - self.__saldo
            self.__saldo = 0
        else:
            self.__saldo -= valor

    def digite_sua_senha(self):
        senha = str(input('Digite sua senha: '))
        self.valida_senha(senha)

    def valida_senha(self, senha):
        if senha == str(self.__senha):
            pass
        else:
            raise ValueError('Senha Inválida!')

    def verifica_pode_retirar(self, valor):
        if valor <= self.__saldo + self.limite_atual:
            return True
        else:
            raise ValueError('Saque nao efetuado por falta de limite')

    def extrato(self):
        print(f'Saldo: {self.__saldo}\n'
              f'Limite atual: {self.limite_atual}\n'
              f'Limite Mensal: {self.limite}')


pessoa = Pessoa('Henrique', 'Salles', '079.495.743-99', '(48)99140-1331')
conta = Conta(pessoa, '(45)88945-1420', '491513')
print(conta)
