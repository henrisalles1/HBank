import datetime
import re


class Idade:
    def __init__(self, data_nascimento: str):
        data_nascimento = self.limpa_data(data_nascimento)
        data_nascimento = self.transforma_em_datetime(data_nascimento)
        data_atual = datetime.datetime.now()
        idade = data_atual - data_nascimento
        self.idade = int(idade.days/356.25)

    def limpa_data(self, data):
        data = re.sub('/', ' ', data)
        data = data.split()
        return list(data)

    def transforma_em_datetime(self, data: list):
        data = datetime.datetime(int(data[2]), int(data[1]), int(data[0]))
        return data
