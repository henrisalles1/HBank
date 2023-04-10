from dirConta.dirPessoa.dirDocumentos.Cpf import Cpf
from dirConta.dirPessoa.dirDocumentos.Cnpj import Cnpj
from dirConta.dirPessoa.Telefone import Telefone
from dirConta.Senha import Senha
import datetime


class Conta:
    numero_conta: int = 0
    limite: float = 1000
    lista_contas: list = []

    def __init__(self, Pessoa, telefone: str, senha: str):
        # Verificações
        self.__pode_criar_conta_p_idade(Pessoa)
        self.__nao_tem_conta_com_doc_igual(Pessoa.cpf)
        self.__nao_tem_conta_com_doc_igual(Pessoa.cnpj)

        # Atributos de Pessoa
        self.__Pessoa = Pessoa
        self._documento = Pessoa.Doc
        self.telefone_preferivel = Telefone(telefone)
        self.telefone_pessoal = Pessoa.telefone
        self.__Nome_completo: str = f'{Pessoa.primeiro_nome} {Pessoa.sobrenome}'

        # Atributos novos
        self.__numero_conta: int = Conta.numero_conta
        self.__senha = Senha(senha).senha
        self.__limite: float = Conta.limite
        self.__limite_atual: float = self.limite
        self.__saldo: float = 0
        self.dia_quitacao: int = 10
        self.__divida: float = 0
        self._inadimplente = False

        # Vantagens de Status
        self.__status_cliente = 'Normal'
        self.__limite_divida = 25000

        # Mudanças em class
        Conta.numero_conta += 1
        Conta.lista_contas.append(self)

    def __str__(self):
        return f'Nº{self.__numero_conta}' \
               f'Nome: {self.__Nome_completo}\n' \
               f'{self._documento}\n' \
               f'Telefone: {self.telefone_preferivel}\n'

    # # # # Operações de cliente # # # #
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

    # # # # Senha methods # # # #
    def digite_sua_senha(self):
        senha = str(input('Digite sua senha: '))
        self.__valida_senha(senha)

    def __valida_senha(self, senha):
        if senha == str(self.__senha):
            pass
        else:
            raise ValueError('Senha Inválida!')

    # # # # Verificadores e Ajustes # # # #
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

    def __aumenta_divida_m(self):
        if self.__status_cliente == 'Normal' or 'Plus':
            self.__divida *= 0.1
        elif self.__status_cliente == 'Platinum':
            self.__divida *= 0.08
        elif self.__status_cliente == 'VIP':
            self.__divida *= 0.06
        else:
            self.__erro_status_cliente()

    def __e_o_dia(self, dia_def, mes: int):
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

    def __ajuste_limite_divida(self):
        if self.__status_cliente == 'Normal':
            self.__limite_divida = 25000
        elif self.__status_cliente == 'Plus':
            self.__limite_divida = 50000
        elif self.__status_cliente == 'Platinum':
            self.__limite_divida = 100000
        elif self.__status_cliente == 'VIP':
            self.__limite_divida = 250000

    # # # # Veficações de init # # # #
    def __pode_criar_conta_p_idade(self, pessoa):
        if pessoa.idade >= 18:
            pass
        else:
            raise ValueError('A pessoa é menor de 18 anos')

    def __nao_tem_conta_com_doc_igual(self, doc):
        if isinstance(doc, Cpf):
            for conta in range(len(Conta.lista_contas)):
                if doc == Conta.lista_contas[conta].__Pessoa.Doc.cpf:
                    raise ValueError('Documento CPF já existente no banco,\n'
                                     'procure mais informações para recuperar sua conta!')
                else:
                    pass
        elif isinstance(doc, Cnpj):
            for conta in range(len(Conta.lista_contas)):
                if doc == Conta.lista_contas[conta].__Pessoa.cnpj:
                    raise ValueError('Documento CNPJ já existente no banco,\n'
                                     'procure mais informações para recuperar sua conta!')
                else:
                    pass

    # # # # Status # # # #
    def status_de_conta(self):
        v_vip = 500000
        v_platinum = 100000
        v_plus = 10000
        if self.__status_cliente == 'Padrao':
            if self.__saldo >= v_vip:
                self.__status_cliente = 'VIP'
            elif self.__saldo >= v_platinum < v_vip:
                self.__status_cliente = 'Platinum'
            elif self.__saldo >= v_plus < v_platinum:
                self.__status_cliente = 'Plus'
        elif self.__status_cliente == 'Plus':
            if self.__saldo >= v_vip:
                self.__status_cliente = 'VIP'
            elif self.__saldo >= v_platinum < v_vip:
                self.__status_cliente = 'Platinum'
        elif self.__status_cliente == 'Platinum':
            if self.__saldo >= v_vip:
                self.__status_cliente = 'VIP'
        else:
            self.__erro_status_cliente()

    def status_inadimplente(self):
        if self.__divida >= self.__limite_divida:
            self._inadimplente = True
        else:
            self._inadimplente = False

    # # # # RAISE ERROS # # # #
    def __erro_status_cliente(self):
        raise ValueError('Erro em atributo __status_cliente, ative status_de_conta()')

    #  #  #  #  #  #  #  AJUSTE MENSAL / Interações AUTO  #  #  #  #  #  #  #
    def ajuste_mensal(self):
        dia: int = self.dia_quitacao
        mes = int(datetime.datetime.today().month)
        if self.__e_o_dia(dia, mes):
            self.status_de_conta()
            self.status_inadimplente()
            self.__aumenta_divida_m()
            self.quita_credito_m()
        else:
            pass
    #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
