import jsonpickle
from Dominio.pregunta import Pregunta


class PersistenciaPregunta:
    @classmethod
    def save_json(cls, pregunta):
        text_open = open("filesPreguntas/" + str(pregunta.id) + '.json', mode='w')
        json_gui = jsonpickle.encode(pregunta)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json(cls, file_name):
        text_open = open("filesPreguntas/" + file_name, mode='r')
        json_gui = text_open.readline()
        pregunta = jsonpickle.decode(json_gui)
        text_open.close()
        return pregunta
