from dirConta.Documentos.Doc import Doc


class Pessoa:
    def __init__(self, primeiro_nome: str, sobrenome: str, documento: str, telefone: str):
        self.primeiro_nome = primeiro_nome.title()
        self.sobrenome = sobrenome.title()
        self.Doc = Doc(documento)
        self.cpf = self.Doc.cpf
        self.cnpj = self.Doc.cnpj
        self.telefone = telefone

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

    def print_Doc(self):
        return self.Doc


pessoa = Pessoa('Henrique', 'Salles', "881.067.538-08", "(48)99140-1331")
pessoa.adiciona_cnpj("34.871.427/0001-87")

print(pessoa.Doc)
