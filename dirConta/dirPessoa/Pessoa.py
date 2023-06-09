from dirConta.dirPessoa.dirDocumentos.Doc import Doc
from dirConta.dirPessoa.Nome import Nome
from dirConta.dirPessoa.Telefone import Telefone
from dirConta.dirPessoa.Idade import Idade



class Pessoa:
    def __init__(self, primeiro_nome: str, sobrenome: str, documento: str, telefone: str, data_nascimento: str):
        self.primeiro_nome = Nome(primeiro_nome)
        self.sobrenome = Nome(sobrenome)
        self.Doc = Doc(documento)
        self.cpf = self.Doc.cpf
        self.cnpj = self.Doc.cnpj
        self.telefone = Telefone(telefone)
        self.data_nascimento = data_nascimento
        self.idade = Idade(data_nascimento).idade

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

    def pega_idade(self):
        self.idade = Idade(self.data_nascimento)


pessoa = Pessoa('Teste', 'Teste', '07949574399', '+55(48)99140-1331', '16/10/2005')

