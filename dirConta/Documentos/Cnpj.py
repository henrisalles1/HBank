class Cnpj:
    def __init__(self, cnpj):
        self.cnpj = cnpj

    def __str__(self):
        return f'{self.cnpj[:2]}.{self.cnpj[2:5]}.{self.cnpj[5:8]}/{self.cnpj[8:12]}-{self.cnpj[12:]}'

    def valida_cnpj(self):
        if self.verifica_primeiro_digito():
            if self.verifica_segundo_digito():
                if self.digitos_n_iguais():
                    print('CNPJ cadastrado!')
                else:
                    raise ValueError('CNPJ inválido "Queda por digitos de cnpj iguais"')
            else:
                raise ValueError('CNPJ inválido "Queda por segundo digito verificcador"')
        else:
            raise ValueError('CNPJ inválido "Queda por primeiro digito verificador"')

    def verifica_primeiro_digito(self):
        limite1 = len(self.cnpj)-2
        limite2 = 4
        multiplicador1 = 5
        if self.digito_verificador(self.cnpj[12], limite1, limite2, multiplicador1):
            return True
        else:
            return False

    def verifica_segundo_digito(self):
        limite1 = len(self.cnpj)-1
        limite2 = 5
        multiplicador1 = 6
        if self.digito_verificador(self.cnpj[13], limite1, limite2, multiplicador1):
            return True
        else:
            return False

    def digito_verificador(self, digito_verificador: int, limite1: int, limite2: int, multiplicador):
        digitos = []
        soma_digitos: int = 0
        digito_verificador = int(digito_verificador)
        for x in range(0, limite1):
            digitos.append(int(self.cnpj[x]))
        m1 = multiplicador
        for x in range(0, limite2):
            digitos[x] *= m1
            m1 -= 1
        m2 = 9
        for x in range(limite2, len(digitos)):
            digitos[x] *= m2
            m2 -= 1
        for x in range(0, len(digitos)):
            soma_digitos += digitos[x]
        resultado = soma_digitos % 11
        if resultado < 2:
            resultado = 0
        else:
            resultado = 11 - resultado
        if resultado == digito_verificador:
            return True
        else:
            return False

    def digitos_n_iguais(self):
        d = []
        for x in range(len(self.cnpj)):
            d.append(self.cnpj[x])
        if len(set(d)) == 1:
            return False
        else:
            return True
