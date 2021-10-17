from controladores.especificacion import Especificacion


class Controlador_Usuario:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, usuario):
        espec = Especificacion()
        espec.agregar_parametros('documento', usuario.documento)
        if len(list(self.buscar_usuario(espec))) == 0:
            self.usuarios.append(usuario)
        else:
            raise Exception('¡jugador repetido!')

    def buscar_usuario(self, especificacion):
        for u in self.usuarios:
            if u.cumple(especificacion):
                yield u
