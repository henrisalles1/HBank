from dirConta.Pessoa import Pessoa
from dirConta.Senha import Senha
from dirConta.Telefone import Telefone
# from dirConta.Conta import Conta

class ContaComercial:
    def __init__(self, Pessoa, telefone, senha):
        self.Nome_completo = f'{Pessoa.primeiro_nome} {Pessoa.sobrenome}'
        self.cnpj = Pessoa.cnpj
        self.telefone_preferivel = Telefone(telefone)
        self.telefone_pessoal = Pessoa.telefone
        self.__senha = Senha(senha)
        self.limite = 1000000
        self.saldo = 0

    def __str__(self):
        return f'Nome: {self.Nome_completo}\n' \
               f'CNPJ: {self.cnpj}\n' \
               f'Telefone: {self.telefone_preferivel}\n' \



pessoa1 = Pessoa('Henrique', 'Salles', '95278719000103', '48991402222')
conta1 = ContaComercial(pessoa1, '48922402222', '491640')
print(conta1)
