from Dominio.respuesta import Respuesta
import uuid


class Pregunta:
    def __init__(self, descripcion, dificultad, valor_acomulado, respuesta):
        self.descripcion = descripcion
        self.dificultad = dificultad
        self.valor_acomulado = valor_acomulado
        self.respuesta = respuesta
        self.id = uuid.uuid4()

    def __repr__(self):
        return f'descripcion: {self.descripcion}-\n' \
               f'dificultad: {self.dificultad}-\n' \
               f'valor_acomulado: {self.valor_acomulado}-\n' \
               f'pregunta Incorrecta 1: {self.respuesta.respuesta_incorrecta1}-\n' \
               f'pregunta Incorrecta 2: {self.respuesta.respuesta_incorrecta2}-\n' \
               f'pregunta Incorrecta 3: {self.respuesta.respuesta_incorrecta3}-\n' \
               f'respuesta: {self.respuesta.respuesta_correcta}-\n'

    def cumple_pregunta(self, especificacion):
        dict_pregunta = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_pregunta or dict_pregunta[k] != especificacion.get_value(k):
                return False
        return True

    def get_descripcion(self):
        return self.descripcion

    def get_dificultad(self):
        return self.descripcion

    def get_valorAcomulado(self):
        return self.descripcion

    def get_respuestaCorrecta(self):
        return self.respuesta.respuesta_correcta

    def get_respuestaIncorrecta1(self):
        return self.respuesta.respuesta_incorrecta1

    def get_respuestaIncorrecta2(self):
        return self.respuesta.respuesta_incorrecta2

    def get_respuestaIncorrecta3(self):
        return self.respuesta.respuesta_incorrecta3
