class Senha:
    def __init__(self, senha):
        if self.senha_valida(senha):
            self.senha = senha
        else:
            raise ValueError('Senha não cadastrada')

    def senha_valida(self, senha):
        if len(senha) == 6:
            if senha.isdigit():
                if self.senha_igual(senha):
                    return True
                else:
                    raise ValueError('A senha não pode ter todos os digitos iguais')
            else:
                raise ValueError('A senha deve conter apenas números')
        else:
            raise ValueError('A senha deve ter 6 digitos')

    def senha_igual(self, senha):
        d = []
        for digito in senha:
            d.append(digito)
        if len(set(d)) == 1:
            return False
        else:
            return True
