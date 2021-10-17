from controladores.especificacion import Especificacion
from Dominio.pregunta import Pregunta


class Controlador_Pregunta:
    def __init__(self):
        self.preguntas = []

    def agregar_pregunta(self, pregunta):
        espec = Especificacion()
        espec.agregar_parametros('id', pregunta.id)
        if len(list(self.buscar_pregunta(espec))) == 0:
            self.preguntas.append(pregunta)
        else:
            raise Exception('¡pregunta repetida!')

    def buscar_pregunta(self, especificacion):
        for p in self.preguntas:
            if p.cumple_pregunta(especificacion):
                yield p
