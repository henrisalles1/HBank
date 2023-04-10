class Nome:
    def __init__(self, nome):
        if self.valida_nome(nome):
            self.nome = nome
        else:
            raise ValueError('Insira apenas um nome!\n'
                             'Ex: Nome- João Pedro Silva\n'
                             'Primeiro_nome: João\n'
                             'Sobrenome: Silva')
    def __str__(self):
        return self.nome

    def valida_nome(self, nome):
        nome = str(nome)
        if nome.isalpha():
            return True
