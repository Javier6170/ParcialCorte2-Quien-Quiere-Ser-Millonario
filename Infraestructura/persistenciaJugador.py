import jsonpickle


class PersistenciaUsuario:


    @classmethod
    def save_json(cls, usuario):
        text_open = open("filesPersonas/" + str(usuario.documento) + '.json', mode='w')
        json_gui = jsonpickle.encode(usuario)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json(cls, file_name):
        text_open = open("filesPersonas/" + file_name, mode='r')
        json_gui = text_open.readline()
        usuario = jsonpickle.decode(json_gui)
        text_open.close()
        return usuario
