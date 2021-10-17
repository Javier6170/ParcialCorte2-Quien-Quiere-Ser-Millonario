class Especificacion:
    def __init__(self):
        self.dict = dict()

    def get_keys(self):
        return self.dict.keys()

    def get_value(self, k):
        return self.dict[k]

    def agregar_parametros(self, llave, valor):
        self.dict[llave] = valor
