class Contacto:
    def __init__(self, numero, conocimientoContacto):
        self.numero = numero
        self.conocimientoContacto = conocimientoContacto

    def __repr__(self):
        return f'numero: {self.numero}-\n' \
               f'conocimiento contacto: {self.conocimientoContacto}-\n'
