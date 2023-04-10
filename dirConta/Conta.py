from dirConta.dirPessoa.Pessoa import Pessoa
from dirConta.dirPessoa.Telefone import Telefone
from dirConta.Senha import Senha
import datetime

class Conta:
    numero_conta: int = 0
    limite: float = 1000

    def __init__(self, Pessoa, telefone: str, senha: str):
        # Atributos de Pessoa
        self.__Pessoa = Pessoa
        self._documento = Pessoa.Doc
        self.telefone_preferivel = Telefone(telefone)
        self.telefone_pessoal = Pessoa.telefone
        self.__Nome_completo: str = f'{Pessoa.primeiro_nome} {Pessoa.sobrenome}'
        # Atributos novos
        self.__senha = Senha(senha).senha
        self.__limite: float = Conta.limite
        self.__limite_atual: float = self.limite
        self.__saldo: float = 0
        self.dia_quitacao: int = 10
        self.__divida: float = 0
        # Verificações
        self.__pode_criar_conta_p_idade()

    def __str__(self):
        return f'Nome: {self.__Nome_completo}\n' \
               f'{self._documento}\n' \
               f'Telefone: {self.telefone_preferivel}\n'

    #### Operações de cliente ####
    def saque(self, valor):
        self.digite_sua_senha()
        if self.__verifica_pode_retirar(valor):
            self.__ajuste_saldolimite(valor)
            print(f'Efetuado o saque no valor de {valor}')

    def deposito(self, valor):
        self.__saldo += valor

    def transferencia(self, destino, valor):
        self.digite_sua_senha()
        if self.__verifica_pode_retirar(valor):
            self.__ajuste_saldolimite(valor)
            destino.deposito(valor)
            print(f'Efetuado a transferencia no valor de {valor}')

    def extrato(self):
        print(f'Saldo: {self.__saldo}\n'
              f'Limite atual: {self.__limite_atual}\n'
              f'Limite Mensal: {self.limite}')

    #### Senha methods ####
    def digite_sua_senha(self):
        senha = str(input('Digite sua senha: '))
        self.__valida_senha(senha)

    def __valida_senha(self, senha):
        if senha == str(self.__senha):
            pass
        else:
            raise ValueError('Senha Inválida!')

    #### Regras do Banco ####
    def __pode_criar_conta_p_idade(self):
        if self.__Pessoa.idade >= 18:
            pass
        else:
            raise ValueError('A pessoa é menor de 18 anos')

    #### Verificadores e Ajustes ####
    def __ajuste_saldolimite(self, valor):
        if valor > self.__saldo:
            self.__limite_atual -= valor - self.__saldo
            self.__saldo = 0
        else:
            self.__saldo -= valor

    def __verifica_pode_retirar(self, valor):
        if valor <= self.__saldo + self.__limite_atual:
            return True
        else:
            raise ValueError('Saque nao efetuado por falta de limite')

    def ajuste_mensal(self):
        dia: int = self.dia_quitacao
        mes = datetime.datetime.month
        print(mes)
        if self.__e_o_dia(dia, mes):
            self.__aumenta_divida_m()
            self.quita_credito_m()
        else:
            pass

    def __aumenta_divida_m(self):
        self.__divida *= 0.1

    def __e_o_dia(self, dia_def, mes):
        data_atual = datetime.datetime.now()
        dia = data_atual.day
        if dia == dia_def:
            mes += 1
            return True, mes

    def quita_credito_m(self):
        limite_gasto = self.__limite - self.__limite_atual
        if self.__saldo >= limite_gasto:
            self.__saldo -= limite_gasto
            self.__limite_atual = self.__limite
        else:
            self.__saldo -= limite_gasto
            self.__divida = self.__saldo
            self.__saldo = 0

pessoa = Pessoa('Henrique', 'Salles', '079.495.743-99', '(48)99140-1331', '16/10/2004')
conta = Conta(pessoa, '(45)88945-1420', '491513')
conta.ajuste_mensal()
