from dirConta.Documentos.Cpf import Cpf
from dirConta.Documentos.Cnpj import Cnpj
import re


class Doc:
    def __init__(self, documento):
        self.cpf = False
        self.cnpj = False
        documento = re.sub('[-./]', '', documento)
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