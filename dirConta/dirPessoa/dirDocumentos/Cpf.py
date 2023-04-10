class Cpf:
    def __init__(self, cpf):
        self.cpf = str(cpf)

    def __str__(self):
        return f"{self.cpf[0:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}"

    def __eq__(self, outro):
        return self.cpf == outro.cpf


    def valida_cpf(self):
        if self.valida_p_soma():
            if self.valida_primeiro_digito():
                if self.valida_segundo_digito():
                    if self.valida_digitos_n_iguais():
                        print('CPF Cadastrado')
                    else:
                        raise ValueError('CPF inválido ! "Queda por digitos iguais"')
                else:
                    raise ValueError('CPF inválido ! "Queda por segundo digito validador"')
            else:
                raise ValueError('CPF inválido ! "Queda por primeiro digito validador"')
        else:
            raise ValueError('CPF inválido ! "Queda por soma de digitos"')

    def valida_digitos_n_iguais(self):
        d = []
        for x in range(len(self.cpf)):
            d.append(self.cpf[x])
        if len(set(d)) == 1:
            return False
        else:
            return True

    def valida_p_soma(self):
        soma_digitos = 0
        for x in range(0, len(self.cpf)):
            soma_digitos += int(self.cpf[x])
        soma_digitos = str(soma_digitos)
        digito_1 = soma_digitos[0]
        digito_2 = soma_digitos[1]
        if digito_1 == digito_2:
            return True
        else:
            return False

    def valida_primeiro_digito(self):
        self.digitos_validadores(9, 10)
        if self.digitos_validadores:
            return True
        else:
            return False

    def valida_segundo_digito(self):
        self.digitos_validadores(10, 11)
        if self.digitos_validadores:
            return True
        else:
            return False

    def digitos_validadores(self, index_digito: int, multiplicador_inicial: int):
        digito_verificador: str = self.cpf[index_digito]
        soma_digitos: int = 0
        multiplicador: int = multiplicador_inicial
        lista_digitos: list = []
        if multiplicador == 11:
            limite = 10
        elif multiplicador == 10:
            limite = 9
        else:
            raise ValueError('Erro em metodo digito_validadores')
        for x in range(0, limite):
            digito = int(self.cpf[x])
            digito_multiplicado = digito * multiplicador
            multiplicador -= 1
            lista_digitos.append(digito_multiplicado)
        for digito_multiplicado in lista_digitos:
            soma_digitos += digito_multiplicado
        resultado = str((soma_digitos * 10) % 11)
        if digito_verificador == resultado:
            return True
        else:
            return False
