from dirConta.dirPessoa.Pessoa import Pessoa
# CPF teste = 542.809.700-09
# CPNJ teste = 48.785.802/0001-80

def test_cria_pessoa():
    pessoa_teste = Pessoa('Henrique', 'Salles', '542.809.700-09', '+55(48)99140-1331', '16/10/2005')
    assert type(pessoa_teste) == Pessoa

def test_cria_pessoa_com_cpf():
    pessoa_teste = Pessoa('Teste', 'Teste', '542.809.700-09', '+55(48)99140-1331', '16/10/2005')
    assert pessoa_teste.cpf != False and pessoa_teste.cnpj == False

def test_cria_pessoa_com_cnpj():
    pessoa_teste = Pessoa('Teste', 'Teste', '48.785.802/0001-80', '+55(48)99140-1331', '16/10/2005')
    assert pessoa_teste.cnpj != False and pessoa_teste.cpf == False

def test_volta_telefone_certo_de_pessoa():
    telefone_certo = '+55(48)99140-1331'
    telefone = '+55(48)991401331'
    pessoa_teste = Pessoa('Teste', 'Teste', '48.785.802/0001-80', telefone, '16/10/2005')
    assert print(pessoa_teste.telefone) == print(telefone_certo)

def test_adiciona_cpf_tendo_cnpj():
    cpf = '542.809.700-09'
    cnpj = '48.785.802/0001-80'
    pessoa_teste = Pessoa('Teste', 'Teste', cnpj, '+55(48)99140-1331', '16/10/2005')
    pessoa_teste.adiciona_cpf(cpf)
    assert print(pessoa_teste.Doc) == print(f'CPF --- {cpf}\n'
                                            f'CNPJ -- {cnpj}')

def test_adiciona_cnpj_tendo_cpf():
    cpf = '542.809.700-09'
    cnpj = '48.785.802/0001-80'
    pessoa_teste = Pessoa('Teste', 'Teste', cpf, '+55(48)99140-1331', '16/10/2005')
    pessoa_teste.adiciona_cnpj(cnpj)
    assert print(pessoa_teste.Doc) == print(f'CPF --- {cpf}\n'
                                            f'CNPJ -- {cnpj}')





