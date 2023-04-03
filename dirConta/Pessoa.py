from dirConta.Documentos.Doc import Doc


class Pessoa:
    def __init__(self, primeiro_nome: str, sobrenome: str, documento: str, telefone: str):
        self.primeiro_nome = primeiro_nome.title()
        self.sobrenome = sobrenome.title()
        self.Doc = Doc(documento)
        self.cpf = self.Doc.cpf
        self.cnpj = self.Doc.cnpj
        self.telefone = telefone


p = Pessoa('Henrique', 'Salles', "881.067.538-08", "(48)99140-1331")

print(p.cpf)