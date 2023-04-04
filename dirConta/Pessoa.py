from dirConta.Documentos.Doc import Doc
from Nome import Nome
from Telefone import Telefone


class Pessoa:
    def __init__(self, primeiro_nome: str, sobrenome: str, documento: str, telefone: str):
        self.primeiro_nome = Nome(primeiro_nome)
        self.sobrenome = Nome(sobrenome)
        self.Doc = Doc(documento)
        self.cpf = self.Doc.cpf
        self.cnpj = self.Doc.cnpj
        self.telefone = Telefone(telefone)

    def adiciona_cnpj(self, cnpj):
        self.Doc.adiciona_cnpj(cnpj)
        self.cnpj = self.Doc.cnpj

    def adiciona_cpf(self, cpf):
        self.Doc.adiciona_cpf(cpf)
        self.cpf = self.Doc.cpf

    def troca_cnpj(self, cnpj):
        self.Doc.troca_cnpj(cnpj)
        self.cnpj = self.Doc.cnpj

    def troca_cpf(self, cpf):
        self.Doc.troca_cpf(cpf)
        self.cpf = self.Doc.cpf

    def troca_telefone(self, telefone):
        self.telefone = Telefone(telefone)

