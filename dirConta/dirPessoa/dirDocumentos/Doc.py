from dirConta.dirPessoa.dirDocumentos.Cpf import Cpf
from dirConta.dirPessoa.dirDocumentos.Cnpj import Cnpj
import re


class Doc:
    def __init__(self, documento):
        self.cpf = False
        self.cnpj = False
        documento = self.limpa_doc(documento)
        if len(documento) == 11:
            self.cpf = Cpf(documento)
        elif len(documento) == 14:
            self.cnpj = Cnpj(documento)
        else:
            print("Insira um documento válido (CPF ou CNPJ)")

    def __str__(self):
        if self.cpf and not self.cnpj:
            return f'CPF --- {self.cpf}'
        elif self.cnpj and not self.cpf:
            return f'CNPJ -- {self.cnpj}'
        elif self.cpf and self.cnpj:
            return f'CPF --- {self.cpf}\n' \
                   f'CNPJ -- {self.cnpj}\n'

    def adiciona_cpf(self, cpf: str):
        cpf = self.limpa_doc(cpf)
        if self.cpf:
            raise ValueError("O atributo CPF já tem valor, tente troca_cpf")
        else:
            self.cpf = Cpf(cpf)

    def adiciona_cnpj(self, cnpj: str):
        cnpj = self.limpa_doc(cnpj)
        if self.cnpj:
            raise ValueError("O atributo CNPJ já tem valor, tente troca_cnpj")
        else:
            self.cnpj = Cnpj(cnpj)

    def limpa_doc(self, doc):
        doc = re.sub('[-./]', '', doc)
        return doc

    def troca_cpf(self, cpf):
        cpf = self.limpa_doc(cpf)
        if self.cpf:
            self.cpf = Cpf(cpf)
        else:
            raise ValueError("Ainda não há um CPF cadastrado, tente adiciona_cpf")

    def troca_cnpj(self, cnpj):
        cnpj = self.limpa_doc(cnpj)
        if self.cpf:
            self.cpf = Cpf(cnpj)
        else:
            raise ValueError("Ainda não há um CPF cadastrado, tente adiciona_cpf")
