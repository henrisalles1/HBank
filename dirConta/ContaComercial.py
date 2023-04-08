from dirConta.Pessoa import Pessoa
from dirConta.Senha import Senha
from dirConta.Telefone import Telefone
# from dirConta.Conta import Conta

class ContaComercial:




pessoa1 = Pessoa('Henrique', 'Salles', '95278719000103', '48991402222')
conta1 = ContaComercial(pessoa1, '48922402222', '491640')
print(conta1)
