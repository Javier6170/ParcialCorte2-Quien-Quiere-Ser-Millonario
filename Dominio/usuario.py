from Dominio.contacto import Contacto


class Usuario:

    def __init__(self, nombre, apellido, documento, telefono, contacto):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.telefono = telefono
        self.contacto = contacto

    def __repr__(self):
        return f'nombre: {self.nombre}-\n' \
               f'Apellido: {self.apellido}-\n' \
               f'Telefono: {self.telefono}-\n' \
               f'numero Contacto: {self.contacto.numero}-\n' \
               f'Conocimiento Contacto: {self.contacto.conocimientoContacto}-\n' \
               f'documento: {self.documento}-\n'

    def cumple(self, especificacion):
        dict_usuario = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_usuario or dict_usuario[k] != especificacion.get_value(k):
                return False
        return True
