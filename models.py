class Caso:
    def __init__(self, numero, cliente, data_abertura, status, descricao, advogado):
        self.numero = numero
        self.cliente = cliente
        self.data_abertura = data_abertura
        self.status = status
        self.descricao = descricao
        self.advogado = advogado

    def __str__(self):
        return f'Caso Nº {self.numero} - Cliente: {self.cliente} - Status: {self.status}'
