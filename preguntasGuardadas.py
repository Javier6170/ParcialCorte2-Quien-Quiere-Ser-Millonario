from numpy import diff

from Dominio.respuesta import Respuesta
from Dominio.pregunta import Pregunta
from controladores.controlador_pregunta import Controlador_Pregunta
from Infraestructura.persistenciaPregunta import PersistenciaPregunta

inv_preguntas = Controlador_Pregunta()


def agregarPreguntasDificultadBaja():
    descripcion = '¿Cual de los siguientes seria traido por un iman?'
    respuestaCorrecta = 'Metal'
    respuestaIncorrecta1 = 'Plastico'
    respuestaIncorrecta2 = 'Madera'
    respuestaIncorrecta3 = 'El Hombre eqivocado'
    dificultad = 'Baja'
    valorAcomulado = 10000
    respuesta1 = Respuesta(respuestaIncorrecta1, respuestaIncorrecta2, respuestaIncorrecta3, respuestaCorrecta)
    pregunta1 = Pregunta(descripcion, dificultad, valorAcomulado, respuesta1)
    inv_preguntas.agregar_pregunta(pregunta1)
    PersistenciaPregunta().save_json(pregunta1)

    descripcion = '¿Que nombre tiene tradicionalmente la fiesta que se hace a una mujer que espera a un bebe?'
    respuestaIncorrecta1 = 'Baby drizzel'
    respuestaCorrecta = 'Baby shower'
    respuestaIncorrecta2 = 'Baby downpour'
    respuestaIncorrecta3 = 'Baby deluge'
    dificultad = 'Baja'
    valorAcomulado = 10000
    respuesta2 = Respuesta(respuestaIncorrecta1, respuestaIncorrecta2, respuestaIncorrecta3, respuestaCorrecta)
    pregunta2 = Pregunta(descripcion, dificultad, valorAcomulado, respuesta2)
    inv_preguntas.agregar_pregunta(pregunta2)
    PersistenciaPregunta().save_json(pregunta2)

    descripcion = 'En los hoteles elegantes,¿Que snack suele dejarse sobre la almohada?'
    respuestaIncorrecta1 = 'Banano'
    respuestaIncorrecta2 = 'Guayaba'
    respuestaCorrecta = 'Menta'
    respuestaIncorrecta3 = 'Juguito de maracuya'
    dificultad = 'Baja'
    valorAcomulado = 10000
    respuesta3 = Respuesta(respuestaIncorrecta1, respuestaIncorrecta2, respuestaIncorrecta3, respuestaCorrecta)
    pregunta3 = Pregunta(descripcion, dificultad, valorAcomulado, respuesta3)
    inv_preguntas.agregar_pregunta(pregunta3)
    PersistenciaPregunta().save_json(pregunta3)

    descripcion = '¿Que palabra se usa para referirse a lo abdominales bien marcados?'
    respuestaCorrecta = 'Lavadero'
    respuestaIncorrecta1 = 'Lavanda'
    respuestaIncorrecta2 = 'Lavadora'
    respuestaIncorrecta3 = 'Lavalosa'
    dificultad = 'Baja'
    valorAcomulado = 10000
    respuesta4 = Respuesta(respuestaIncorrecta1, respuestaIncorrecta2, respuestaIncorrecta3, respuestaCorrecta)
    pregunta4 = Pregunta(descripcion, dificultad, valorAcomulado, respuesta4)
    inv_preguntas.agregar_pregunta(pregunta4)
    PersistenciaPregunta().save_json(pregunta4)

    descripcion = '¿Cual de esta aplicaciones ofrecen masomenos el mismo tipo de servicio?'
    respuestaIncorrecta1 = 'Whatsapp y SHAREit'
    respuestaCorrecta = 'Lyft y Uber'
    respuestaIncorrecta2 = 'TikTok y Spotify'
    respuestaIncorrecta3 = 'Snapchat y Grubhub'
    dificultad = 'Baja'
    valorAcomulado = 10000
    respuesta5 = Respuesta(respuestaIncorrecta1, respuestaIncorrecta2, respuestaIncorrecta3, respuestaCorrecta)
    pregunta5 = Pregunta(descripcion, dificultad, valorAcomulado, respuesta5)
    inv_preguntas.agregar_pregunta(pregunta5)
    PersistenciaPregunta().save_json(pregunta5)

    descripcion = '¿Cual es el lugar de origen del whisky escoses?'
    respuestaIncorrecta1 = 'Irlanda'
    respuestaCorrecta = 'Escocia'
    respuestaIncorrecta2 = 'Gales'
    respuestaIncorrecta3 = 'Estados Unidos'
    dificultad = 'Baja'
    valorAcomulado = 10000
    respuesta6 = Respuesta(respuestaIncorrecta1, respuestaIncorrecta2, respuestaIncorrecta3, respuestaCorrecta)
    pregunta6 = Pregunta(descripcion, dificultad, valorAcomulado, respuesta6)
    inv_preguntas.agregar_pregunta(pregunta6)
    PersistenciaPregunta().save_json(pregunta6)

    descripcion = '¿Cual de estos nombres no aparece en el titulo de una obra de shakespare?'
    respuestaCorrecta = 'Darren'
    respuestaIncorrecta1 = 'Romeo'
    respuestaIncorrecta2 = 'Macbeth'
    respuestaIncorrecta3 = 'Hamlet'
    dificultad = 'Baja'
    valorAcomulado = 10000
    respuesta7 = Respuesta(respuestaIncorrecta1, respuestaIncorrecta2, respuestaIncorrecta3, respuestaCorrecta)
    pregunta7 = Pregunta(descripcion, dificultad, valorAcomulado, respuesta7)
    inv_preguntas.agregar_pregunta(pregunta7)
    PersistenciaPregunta().save_json(pregunta7)

    descripcion = '¿Cómo se llama la capital de Laos?'
    respuestaIncorrecta1 = 'España'
    respuestaCorrecta = 'Vientián'
    respuestaIncorrecta2 = 'Quindio'
    respuestaIncorrecta3 = 'Minsk'
    dificultad = 'Baja'
    valorAcomulado = 10000
    respuesta8 = Respuesta(respuestaIncorrecta1, respuestaIncorrecta2, respuestaIncorrecta3, respuestaCorrecta)
    pregunta8 = Pregunta(descripcion, dificultad, valorAcomulado, respuesta8)
    inv_preguntas.agregar_pregunta(pregunta8)
    PersistenciaPregunta().save_json(pregunta8)

    descripcion = '¿En cual de estas peliculas Whoopi goldberg aparece vestida de monja?'
    respuestaIncorrecta1 = 'Ghost'
    respuestaCorrecta = 'Cambio de habito'
    respuestaIncorrecta2 = 'How judas got, his groove back'
    respuestaIncorrecta3 = 'El color purpura'
    dificultad = 'Baja'
    valorAcomulado = 10000
    respuesta9 = Respuesta(respuestaIncorrecta1, respuestaIncorrecta2, respuestaIncorrecta3, respuestaCorrecta)
    pregunta9 = Pregunta(descripcion, dificultad, valorAcomulado, respuesta9)
    inv_preguntas.agregar_pregunta(pregunta9)
    PersistenciaPregunta().save_json(pregunta9)

    descripcion = 'Por las areas geograficas que representaban, los bandos opuestos de la guerra de seccion eran conocidos como...'
    respuestaCorrecta = 'El Norte y el sur'
    respuestaIncorrecta1 = 'Las colonias y valles'
    respuestaIncorrecta2 = 'Los fulanos y los meganos'
    respuestaIncorrecta3 = 'Oeste y este'
    dificultad = 'Baja'
    valorAcomulado = 10000
    respuesta10 = Respuesta(respuestaIncorrecta1, respuestaIncorrecta2, respuestaIncorrecta3, respuestaCorrecta)
    pregunta10 = Pregunta(descripcion, dificultad, valorAcomulado, respuesta10)
    inv_preguntas.agregar_pregunta(pregunta10)
    PersistenciaPregunta().save_json(pregunta10)


def agregarPreguntasDificultadMediana():
    descripcion = '¿Una locomotora valiente es la heroina de un clasico libro infantil llamado la locomotora que si?'
    respuestaIncorrecta1 = 'Logró'
    respuestaCorrecta = 'Pudo'
    respuestaIncorrecta2 = 'Alcanzo'
    respuestaIncorrecta3 = 'Llego'
    dificultad = 'Mediana'
    valorAcomulado = 20000
    respuesta1 = Respuesta(respuestaIncorrecta1, respuestaIncorrecta2, respuestaIncorrecta3, respuestaCorrecta)
    pregunta1 = Pregunta(descripcion, dificultad, valorAcomulado, respuesta1)
    inv_preguntas.agregar_pregunta(pregunta1)
    PersistenciaPregunta().save_json(pregunta1)

    descripcion = '¿Como se llama la parte que queda en el suelo despues de talar un arbol?'
    respuestaIncorrecta1 = 'Muñon'
    respuestaCorrecta = 'Tocon'
    respuestaIncorrecta2 = 'Joroba'
    respuestaIncorrecta3 = 'Restos'
    dificultad = 'Mediana'
    valorAcomulado = 20000
    respuesta2 = Respuesta(respuestaIncorrecta1, respuestaIncorrecta2, respuestaIncorrecta3, respuestaCorrecta)
    pregunta2 = Pregunta(descripcion, dificultad, valorAcomulado, respuesta2)
    inv_preguntas.agregar_pregunta(pregunta2)
    PersistenciaPregunta().save_json(pregunta2)

    descripcion = '¿En donde es mas probable que escuches la orden "Limpieza en el pasillo 5"?'
    respuestaCorrecta = 'En un supermercado'
    respuestaIncorrecta1 = 'En un banco'
    respuestaIncorrecta2 = 'Centro comercial'
    respuestaIncorrecta3 = 'En un jardin infantil'
    dificultad = 'Mediana'
    valorAcomulado = 20000
    respuesta3 = Respuesta(respuestaIncorrecta1, respuestaIncorrecta2, respuestaIncorrecta3, respuestaCorrecta)
    pregunta3 = Pregunta(descripcion, dificultad, valorAcomulado, respuesta3)
    inv_preguntas.agregar_pregunta(pregunta3)
    PersistenciaPregunta().save_json(pregunta3)

    descripcion = '¿Cuándo llegó el primer hombre a la Luna?'
    respuestaIncorrecta1 = '1965'
    respuestaCorrecta = '1969'
    respuestaIncorrecta2 = '1970'
    respuestaIncorrecta3 = '1977'
    dificultad = 'Mediana'
    valorAcomulado = 20000
    respuesta4 = Respuesta(respuestaIncorrecta1, respuestaIncorrecta2, respuestaIncorrecta3, respuestaCorrecta)
    pregunta4 = Pregunta(descripcion, dificultad, valorAcomulado, respuesta4)
    inv_preguntas.agregar_pregunta(pregunta4)
    PersistenciaPregunta().save_json(pregunta4)

    descripcion = '¿En qué año fue el descubrimiento de América?'
    respuestaIncorrecta1 = '1602'
    respuestaCorrecta = '1492'
    respuestaIncorrecta2 = '1510'
    respuestaIncorrecta3 = '1420'
    dificultad = 'Mediana'
    valorAcomulado = 20000
    respuesta3 = Respuesta(respuestaIncorrecta1, respuestaIncorrecta2, respuestaIncorrecta3, respuestaCorrecta)
    pregunta3 = Pregunta(descripcion, dificultad, valorAcomulado, respuesta3)
    inv_preguntas.agregar_pregunta(pregunta3)
    PersistenciaPregunta().save_json(pregunta3)

    descripcion = '¿En qué año se creó la Organización de las Naciones Unidas (ONU)?'
    respuestaCorrecta = '1945'
    respuestaIncorrecta1 = '1895'
    respuestaIncorrecta2 = '1947'
    respuestaIncorrecta3 = '1946'
    dificultad = 'Mediana'
    valorAcomulado = 20000
    respuesta1 = Respuesta(respuestaIncorrecta1, respuestaIncorrecta2, respuestaIncorrecta3, respuestaCorrecta)
    pregunta1 = Pregunta(descripcion, dificultad, valorAcomulado, respuesta1)
    inv_preguntas.agregar_pregunta(pregunta1)
    PersistenciaPregunta().save_json(pregunta1)

    descripcion = '¿En qué año fue asesinado John F. Kennedy?'
    respuestaIncorrecta1 = '1962'
    respuestaCorrecta = '1963'
    respuestaIncorrecta2 = '1964'
    respuestaIncorrecta3 = '1968'
    dificultad = 'Mediana'
    valorAcomulado = 20000
    respuesta2 = Respuesta(respuestaIncorrecta1, respuestaIncorrecta2, respuestaIncorrecta3, respuestaCorrecta)
    pregunta2 = Pregunta(descripcion, dificultad, valorAcomulado, respuesta2)
    inv_preguntas.agregar_pregunta(pregunta2)
    PersistenciaPregunta().save_json(pregunta2)

    descripcion = '¿En qué año se creó la World Wide Web?'
    respuestaIncorrecta1 = '1992'
    respuestaCorrecta = '1991'
    respuestaIncorrecta2 = '1993'
    respuestaIncorrecta3 = '1850'
    dificultad = 'Mediana'
    valorAcomulado = 20000
    respuesta3 = Respuesta(respuestaIncorrecta1, respuestaIncorrecta2, respuestaIncorrecta3, respuestaCorrecta)
    pregunta3 = Pregunta(descripcion, dificultad, valorAcomulado, respuesta3)
    inv_preguntas.agregar_pregunta(pregunta3)
    PersistenciaPregunta().save_json(pregunta3)

    descripcion = '¿En qué año se creó la Organización de las Naciones Unidas (ONU)?'
    respuestaCorrecta = '1945'
    respuestaIncorrecta1 = '1895'
    respuestaIncorrecta2 = '1947'
    respuestaIncorrecta3 = '1946'
    dificultad = 'Mediana'
    valorAcomulado = 20000
    respuesta1 = Respuesta(respuestaIncorrecta1, respuestaIncorrecta2, respuestaIncorrecta3, respuestaCorrecta)
    pregunta1 = Pregunta(descripcion, dificultad, valorAcomulado, respuesta1)
    inv_preguntas.agregar_pregunta(pregunta1)
    PersistenciaPregunta().save_json(pregunta1)

    descripcion = '¿En qué año fue asesinado John F. Kennedy?'
    respuestaIncorrecta1 = '1962'
    respuestaCorrecta = '1963'
    respuestaIncorrecta2 = '1964'
    respuestaIncorrecta3 = '1968'
    dificultad = 'Mediana'
    valorAcomulado = 20000
    respuesta2 = Respuesta(respuestaIncorrecta1, respuestaIncorrecta2, respuestaIncorrecta3, respuestaCorrecta)
    pregunta2 = Pregunta(descripcion, dificultad, valorAcomulado, respuesta2)
    inv_preguntas.agregar_pregunta(pregunta2)
    PersistenciaPregunta().save_json(pregunta2)


def agregarPreguntasDificultadAlta():
    descripcion = '¿En qué año se creó la World Wide Web?'
    respuestaIncorrecta1 = '1992'
    respuestaCorrecta = '1991'
    respuestaIncorrecta2 = '1993'
    respuestaIncorrecta3 = '1850'
    dificultad = 'Alta'
    valorAcomulado = 100000
    respuesta3 = Respuesta(respuestaIncorrecta1, respuestaIncorrecta2, respuestaIncorrecta3, respuestaCorrecta)
    pregunta3 = Pregunta(descripcion, dificultad, valorAcomulado, respuesta3)
    inv_preguntas.agregar_pregunta(pregunta3)
    PersistenciaPregunta().save_json(pregunta3)

    descripcion = '¿Cuál es la capital de Filipinas?'
    respuestaCorrecta = 'Manila'
    respuestaIncorrecta1 = 'Roma'
    respuestaIncorrecta2 = 'Kiev'
    respuestaIncorrecta3 = 'Varsovia'
    dificultad = 'Alta'
    valorAcomulado = 100000
    respuesta1 = Respuesta(respuestaIncorrecta1, respuestaIncorrecta2, respuestaIncorrecta3, respuestaCorrecta)
    pregunta1 = Pregunta(descripcion, dificultad, valorAcomulado, respuesta1)
    inv_preguntas.agregar_pregunta(pregunta1)
    PersistenciaPregunta().save_json(pregunta1)

    descripcion = '¿En qué océano se encuentra la isla de Guam?'
    respuestaIncorrecta1 = 'Oceano Atlantico'
    respuestaCorrecta = 'Oceano Pacifico'
    respuestaIncorrecta2 = 'Oceano Indico'
    respuestaIncorrecta3 = 'Oceano Artico'
    dificultad = 'Alta'
    valorAcomulado = 100000
    respuesta2 = Respuesta(respuestaIncorrecta1, respuestaIncorrecta2, respuestaIncorrecta3, respuestaCorrecta)
    pregunta2 = Pregunta(descripcion, dificultad, valorAcomulado, respuesta2)
    inv_preguntas.agregar_pregunta(pregunta2)
    PersistenciaPregunta().save_json(pregunta2)

    descripcion = '¿Qué presidente soviético instauró la Perestroika?'
    respuestaIncorrecta1 = 'João Lourenço'
    respuestaCorrecta = 'Mijaíl Gorbachov'
    respuestaIncorrecta2 = 'Abdelmadjid Tebboune'
    respuestaIncorrecta3 = 'Patrice Talon'
    dificultad = 'Alta'
    valorAcomulado = 100000
    respuesta3 = Respuesta(respuestaIncorrecta1, respuestaIncorrecta2, respuestaIncorrecta3, respuestaCorrecta)
    pregunta3 = Pregunta(descripcion, dificultad, valorAcomulado, respuesta3)
    inv_preguntas.agregar_pregunta(pregunta3)
    PersistenciaPregunta().save_json(pregunta3)

    descripcion = '¿Cuál fue la primera película en ganar el Óscar?'
    respuestaCorrecta = 'Alas'
    respuestaIncorrecta1 = 'El padrino'
    respuestaIncorrecta2 = 'El mago de Oz'
    respuestaIncorrecta3 = 'Pulp Fiction'
    dificultad = 'Alta'
    valorAcomulado = 100000
    respuesta1 = Respuesta(respuestaIncorrecta1, respuestaIncorrecta2, respuestaIncorrecta3, respuestaCorrecta)
    pregunta1 = Pregunta(descripcion, dificultad, valorAcomulado, respuesta1)
    inv_preguntas.agregar_pregunta(pregunta1)
    PersistenciaPregunta().save_json(pregunta1)

    descripcion = '¿En qué deporte destacaba Toni Elías?'
    respuestaIncorrecta1 = 'Natacion'
    respuestaCorrecta = 'motociclismo'
    respuestaIncorrecta2 = 'Futbolista'
    respuestaIncorrecta3 = 'Futbol Americano'
    dificultad = 'Alta'
    valorAcomulado = 100000
    respuesta2 = Respuesta(respuestaIncorrecta1, respuestaIncorrecta2, respuestaIncorrecta3, respuestaCorrecta)
    pregunta2 = Pregunta(descripcion, dificultad, valorAcomulado, respuesta2)
    inv_preguntas.agregar_pregunta(pregunta2)
    PersistenciaPregunta().save_json(pregunta2)

    descripcion = '¿Dónde se inventó el ping-pong?'
    respuestaIncorrecta1 = 'Colombia'
    respuestaCorrecta = 'Inglaterra'
    respuestaIncorrecta2 = 'Estados Unidos'
    respuestaIncorrecta3 = 'Suiza'
    dificultad = 'Alta'
    valorAcomulado = 100000
    respuesta3 = Respuesta(respuestaIncorrecta1, respuestaIncorrecta2, respuestaIncorrecta3, respuestaCorrecta)
    pregunta3 = Pregunta(descripcion, dificultad, valorAcomulado, respuesta3)
    inv_preguntas.agregar_pregunta(pregunta3)
    PersistenciaPregunta().save_json(pregunta3)

    descripcion = '¿Qué jugador de fútbol ha ganado más copas del mundo junto a su equipo?'
    respuestaCorrecta = 'Pelé'
    respuestaIncorrecta1 = 'Ronaldinho'
    respuestaIncorrecta2 = 'Maradona'
    respuestaIncorrecta3 = 'Cristiano Ronaldo SIUUUU'
    dificultad = 'Alta'
    valorAcomulado = 100000
    respuesta1 = Respuesta(respuestaIncorrecta1, respuestaIncorrecta2, respuestaIncorrecta3, respuestaCorrecta)
    pregunta1 = Pregunta(descripcion, dificultad, valorAcomulado, respuesta1)
    inv_preguntas.agregar_pregunta(pregunta1)
    PersistenciaPregunta().save_json(pregunta1)

    descripcion = '¿Cuándo se extinguieron los dinosaurios?'
    respuestaIncorrecta1 = 'hace unos 200 millones de años'
    respuestaCorrecta = 'hace unos 65 millones de años'
    respuestaIncorrecta2 = 'hace unos 82 millones de años'
    respuestaIncorrecta3 = 'hace unos 100 millones de años'
    dificultad = 'Alta'
    valorAcomulado = 100000
    respuesta2 = Respuesta(respuestaIncorrecta1, respuestaIncorrecta2, respuestaIncorrecta3, respuestaCorrecta)
    pregunta2 = Pregunta(descripcion, dificultad, valorAcomulado, respuesta2)
    inv_preguntas.agregar_pregunta(pregunta2)
    PersistenciaPregunta().save_json(pregunta2)

    descripcion = '¿Cuál es el nombre de la época geológica en la que nos encontramos actualmente?'
    respuestaIncorrecta1 = 'colonial'
    respuestaCorrecta = 'Holoceno'
    respuestaIncorrecta2 = 'Victoriana'
    respuestaIncorrecta3 = 'Medieval'
    dificultad = 'Alta'
    valorAcomulado = 100000
    respuesta3 = Respuesta(respuestaIncorrecta1, respuestaIncorrecta2, respuestaIncorrecta3, respuestaCorrecta)
    pregunta3 = Pregunta(descripcion, dificultad, valorAcomulado, respuesta3)
    inv_preguntas.agregar_pregunta(pregunta3)
    PersistenciaPregunta().save_json(pregunta3)


if __name__ == "__main__":
    agregarPreguntasDificultadAlta()
    agregarPreguntasDificultadMediana()
    agregarPreguntasDificultadBaja()
