import os
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter.font as tkFont
import pygame
import random
from controladores.controlador_usuario import Controlador_Usuario
from Dominio.usuario import Usuario
from Dominio.contacto import Contacto
from Infraestructura.persistenciaJugador import PersistenciaUsuario
from controladores.especificacion import Especificacion
from Infraestructura.persistenciaPregunta import PersistenciaPregunta
from controladores.controlador_pregunta import Controlador_Pregunta

pygame.init()
pygame.mixer.init()
inv = Controlador_Usuario()
inv_pregunta = Controlador_Pregunta()
sonido_preguntas = pygame.mixer.Sound("sounds/Música preguntas 1 - 5 (Quien Quiere ser millonario).wav")
estado_persistencia = ''
for file in os.listdir("FilesPreguntas"):
    if '.json' in file:
        try:
            estado_persistencia = PersistenciaUsuario.load_json(file)
        except Exception as ex:
            pass


def abrirVentanaRegistro():
    def send_data():
        nombre = str(Nombre.get())
        apellido = str(Apellido.get())
        documento = str(Documento.get())
        telefono = str(Telefono.get())
        numeroContacto = str(TelefonoContacto.get())
        conocimiento = str(Conocimiento)
        contacto = Contacto(numeroContacto, conocimiento)
        usuario = Usuario(nombre, apellido, documento, telefono, contacto)
        inv.agregar_usuario(usuario)
        PersistenciaUsuario().save_json(usuario)
        messagebox.showwarning('Registro Jugador',
                               f'¡Se ha registrado correctamente la informacion!')
        Nombre.set('')
        Apellido.set('')
        Telefono.set('')
        Documento.set('')
        Conocimiento.set('')
        TelefonoContacto.set('')

    def regresarVentanaPrincipal():
        mywindow.withdraw()
        ventana.deiconify()

    ventana.withdraw()
    mywindow = tk.Toplevel()
    mywindow.geometry("290x580")
    mywindow.resizable(False, False)
    mywindow.title("Registro informacion - ¿Quieres ser el proximo millonario?")
    mywindow.iconbitmap("./img/icon.ico")
    mywindow.resizable(False, False)
    mywindow.config(background="RoyalBlue3")
    main_title = tk.Label(mywindow, text="INFORMACION IMPORTANTE", font=("Cambria", 14), bg="blue4", fg="black",
                          width="30",
                          height="2")
    main_title.pack()

    # Define Label Fields
    name_label = tk.Label(mywindow, text="Nombre", bg="RoyalBlue3")
    name_label.place(x=22, y=70)
    lastname_label = tk.Label(mywindow, text="Apellido", bg="RoyalBlue3")
    lastname_label.place(x=22, y=130)
    document_label = tk.Label(mywindow, text="Documento", bg="RoyalBlue3")
    document_label.place(x=22, y=190)
    phone_label = tk.Label(mywindow, text="Telefono", bg="RoyalBlue3")
    phone_label.place(x=22, y=250)
    phoneContact_label = tk.Label(mywindow, text="Numero de contacto ayuda", bg="RoyalBlue3")
    phoneContact_label.place(x=22, y=310)
    conocimiento_label = tk.Label(mywindow, text="Conocimiento del amigo (1 a 10)", bg="RoyalBlue3")
    conocimiento_label.place(x=22, y=370)

    # Get and store data from users
    Nombre = tk.StringVar()
    Apellido = tk.StringVar()
    Telefono = tk.StringVar()
    Documento = tk.StringVar()
    TelefonoContacto = tk.StringVar()
    Conocimiento = tk.StringVar()

    name_entry = tk.Entry(mywindow, textvariable=Nombre, width="40")
    lastname_entry = tk.Entry(mywindow, textvariable=Apellido, width="40")
    document_entry = tk.Entry(mywindow, textvariable=Documento, width="40")
    phone_entry = tk.Entry(mywindow, textvariable=Telefono, width="40")
    phoneContact_entry = tk.Entry(mywindow, textvariable=TelefonoContacto, width="40")
    conocimiento_entry = tk.Entry(mywindow, textvariable=Conocimiento, width="40")

    name_entry.place(x=22, y=100)
    lastname_entry.place(x=22, y=160)
    document_entry.place(x=22, y=220)
    phone_entry.place(x=22, y=280)
    phoneContact_entry.place(x=22, y=340)
    conocimiento_entry.place(x=22, y=400)

    # Submit Button
    submit_btn = tk.Button(mywindow, text="Registrar", width="30", height="2", command=send_data, bg="white")
    submit_btn.place(x=28, y=450)
    submit_btn = tk.Button(mywindow, text="Regresar", width="30", height="2", command=regresarVentanaPrincipal,
                           bg="white")
    submit_btn.place(x=28, y=520)


def abrirVentanaInicioSesion():
    def iniciar():
        especificacion = Especificacion()
        for file2 in os.listdir("FilesPersonas"):
            if '.json' in file2:
                try:
                    inv.agregar_usuario(PersistenciaUsuario.load_json(file2))
                except Exception as ex:
                    pass
        parametro = 'documento'
        documento = str(Documento.get())
        especificacion.agregar_parametros(parametro, documento)
        Documento.set('')
        if len(list(inv.buscar_usuario(especificacion))) > 0:
            win2.destroy()
            cargaInicioDeSesion()
        else:
            tk.messagebox.showwarning('Error', 'Esta persona no la hemos encontrado')

    def regresarVentanaPrincipal():
        win2.withdraw()
        ventana.deiconify()

    ventana.withdraw()
    win2 = tk.Toplevel()
    win2.geometry("400x200")
    win2.resizable(False, False)
    win2.configure(bg="RoyalBlue3")
    win2.iconbitmap("./img/icon.ico")
    win2.title("QUIEN QUIERE SER MILLONARIO")
    main_title = tk.Label(win2, text="INICIO DE SESION", font=("Cambria", 14), bg="blue4", fg="black",
                          width="40",
                          height="2")
    main_title.pack()

    Documento = tk.StringVar()

    name_label = tk.Label(win2, text="Documento", bg="RoyalBlue3")
    name_label.place(x=160, y=70)

    name_entry = tk.Entry(win2, textvariable=Documento, width="40")

    name_entry.place(x=70, y=100)

    tk.Button(win2, text="Regresar", bg="white", width=20, height=1, command=regresarVentanaPrincipal).place(x=215,
                                                                                                             y=150)
    tk.Button(win2, text="Iniciar Sesion", bg="white", width=20, height=1, command=iniciar).place(x=30, y=150)


def cargaInicioDeSesion():
    def regresarVentanaPrincipal():
        mywindow.withdraw()
        ventana.deiconify()

    def abrirVentanaEscogerDificultad():
        mywindow.withdraw()
        abrirVentana4()

    pygame.mixer.Sound.stop(sonido_preguntas)
    ventana.withdraw()
    mywindow = tk.Toplevel()
    mywindow.geometry("400x300")
    mywindow.resizable(False, False)
    mywindow.title("Que Deseas | Quien Quiere ser Millonario")
    mywindow.iconbitmap("./img/icon.ico")
    mywindow.config(background="RoyalBlue3")
    main_title = tk.Label(mywindow, text="Bienvenido", font=("Cambria", 14), bg="blue4", fg="black",
                          width="40",
                          height="2")
    main_title.pack()

    submit_btn = tk.Button(mywindow, text="Jugar nueva partida", command=abrirVentanaEscogerDificultad, width="30",
                           height="2",
                           bg="white")
    submit_btn.place(x=85, y=80)
    submit_btn = tk.Button(mywindow, text="Cargar Partida", width="30", height="2",
                           bg="white")
    submit_btn.place(x=85, y=130)
    submit_btn = tk.Button(mywindow, text="Historial de partidas", width="30", height="2",
                           bg="white")
    submit_btn.place(x=85, y=180)
    submit_btn = tk.Button(mywindow, text="Regresar", command=regresarVentanaPrincipal, width="30", height="2",
                           bg="white")
    submit_btn.place(x=85, y=230)


def contar():
    contador.set(str(int(contador.get()) + 100000))


def abrirVentanaDificultadBaja():
    def respuestaCorrecta():
        respuesta1.place(x=200, y=40)
        respuesta2.place(x=200, y=70)
        respuesta3.place(x=200, y=100)
        respuesta4.place(x=200, y=130)
        preguntaAleatoria()
        contar()
        premio10.config(text=contador.get())
        print(contador.get())
        win.update()

    def respuestaIncorrecta():
        tk.messagebox.showwarning('Mal', 'Ha terminado la partida')
        win.withdraw()
        contador.set(str(int(100000)))
        cargaInicioDeSesion()

    def preguntaCompleta():
        especificacion = Especificacion()
        for file2 in os.listdir("FilesPreguntas"):
            if '.json' in file2:
                try:
                    inv_pregunta.agregar_pregunta(PersistenciaPregunta.load_json(file2))
                except Exception as ex:
                    pass
        parametro = 'dificultad'
        dificultad = 'Baja'
        especificacion.agregar_parametros(parametro, dificultad)
        if len(list(inv_pregunta.buscar_pregunta(especificacion))) > 0:
            preguntas = list(inv_pregunta.buscar_pregunta(especificacion))
            r = random.choice(preguntas)
            return r

    def cincuenta_cincuenta(r):
        if respuesta1.cget("text") == r.get_respuestaCorrecta():
            respuesta2.place(x=10000, y=10000)
            respuesta3.place(x=10000, y=10000)
        elif respuesta2.cget("text") == r.get_respuestaCorrecta():
            respuesta1.place(x=10000, y=10000)
            respuesta3.place(x=10000, y=10000)
        elif respuesta3.cget("text") == r.get_respuestaCorrecta():
            respuesta1.place(x=10000, y=10000)
            respuesta2.place(x=10000, y=10000)
        elif respuesta4.cget("text") == r.get_respuestaCorrecta():
            respuesta1.place(x=10000, y=10000)
            respuesta3.place(x=10000, y=10000)

    def preguntaAleatoria():
        r = preguntaCompleta()

        def combinacion1():
            labelPregunta.config(text=r.get_descripcion())
            respuesta1.config(text=r.get_respuestaCorrecta(),
                              command=respuestaCorrecta),
            respuesta2.config(text=r.get_respuestaIncorrecta1(),
                              command=respuestaIncorrecta),
            respuesta3.config(text=r.get_respuestaIncorrecta2(),
                              command=respuestaIncorrecta),
            respuesta4.config(text=r.get_respuestaIncorrecta3(),
                              command=respuestaIncorrecta)

        def combinacion2():
            labelPregunta.config(text=r.get_descripcion())
            respuesta1.config(text=r.get_respuestaIncorrecta1(),
                              command=respuestaIncorrecta),
            respuesta2.config(text=r.get_respuestaCorrecta(),
                              command=respuestaCorrecta),
            respuesta3.config(text=r.get_respuestaIncorrecta2(),
                              command=respuestaIncorrecta),
            respuesta4.config(text=r.get_respuestaIncorrecta3(),
                              command=respuestaIncorrecta)

        def combinacion3():
            labelPregunta.config(text=r.get_descripcion())
            respuesta1.config(text=r.get_respuestaIncorrecta1(),
                              command=respuestaIncorrecta),
            respuesta2.config(text=r.get_respuestaIncorrecta2(),
                              command=respuestaIncorrecta),
            respuesta3.config(text=r.get_respuestaCorrecta(),
                              command=respuestaCorrecta),
            respuesta4.config(text=r.get_respuestaIncorrecta3(),
                              command=respuestaIncorrecta)

        def combinacion4():
            labelPregunta.config(text=r.get_descripcion())
            respuesta1.config(text=r.get_respuestaIncorrecta1(),
                              command=respuestaIncorrecta),
            respuesta2.config(text=r.get_respuestaIncorrecta2(),
                              command=respuestaIncorrecta),
            respuesta3.config(text=r.get_respuestaIncorrecta3(),
                              command=respuestaIncorrecta),
            respuesta4.config(text=r.get_respuestaCorrecta(),
                              command=respuestaCorrecta)

        listaCombinaciones = [combinacion1, combinacion2, combinacion3, combinacion4]
        combinacionelegida = random.choice(listaCombinaciones)
        if combinacionelegida == combinacion1:
            combinacion1()
        elif combinacionelegida == combinacion2:
            combinacion2()
        elif combinacionelegida == combinacion3:
            combinacion3()
        elif combinacionelegida == combinacion4:
            combinacion4()
        else:
            tk.messagebox.showwarning('Error', 'No hemos podido encontrar estas preguntas')
        return r

    pygame.mixer.Sound.play(sonido_preguntas, -1)
    ventana.withdraw()
    win = tk.Toplevel()
    win.geometry("740x350")
    win.resizable(False, False)
    win.configure(bg="blue")
    win.iconbitmap("./img/icon.ico")
    win.title("QUIEN QUIERE SER MILLONARIO")
    fontStyle = tkFont.Font(family="Lucida Grande", size=12)
    premio10 = tk.Label(win, text=contador.get(), bg="green", font=fontStyle)
    premio10.place(x=350, y=250)
    labelPregunta = tk.Label(win, text="pregunta", bg="white", width=100, height=1)
    labelPregunta.place(x=20, y=10)
    respuesta1 = tk.Button(win, text="A. respuesta 1", bg="white", width=50, height=1)
    respuesta1.place(x=200, y=40)
    respuesta2 = tk.Button(win, text="B. respuesta 2", bg="white", width=50, height=1)
    respuesta2.place(x=200, y=70)
    respuesta3 = tk.Button(win, text="C. respuesta 3", bg="white", width=50, height=1)
    respuesta3.place(x=200, y=100)
    respuesta4 = tk.Button(win, text="D. respuesta 4", bg="white", width=50, height=1)
    respuesta4.place(x=200, y=130)
    r = preguntaAleatoria()
    tk.Button(win, text="Guardar partida", bg="white", width=20, height=1).place(x=300, y=200)
    tk.Button(win, text="50:50", bg="white", width=20, height=1, command=lambda: cincuenta_cincuenta(r)).place(x=300,
                                                                                                               y=300)


def abrirVentanaDificultadMediana():
    def respuestaCorrecta():
        respuesta1.place(x=200, y=40)
        respuesta2.place(x=200, y=70)
        respuesta3.place(x=200, y=100)
        respuesta4.place(x=200, y=130)
        preguntaAleatoria()
        contar()
        premio10.config(text=contador.get())
        print(contador.get())
        win.update()

    def respuestaIncorrecta():
        tk.messagebox.showwarning('Mal', 'Ha terminado la partida')
        win.withdraw()
        contador.set(str(int(100000)))
        cargaInicioDeSesion()

    def preguntaCompleta():
        especificacion = Especificacion()
        for file2 in os.listdir("FilesPreguntas"):
            if '.json' in file2:
                try:
                    inv_pregunta.agregar_pregunta(PersistenciaPregunta.load_json(file2))
                except Exception as ex:
                    pass
        parametro = 'dificultad'
        dificultad = 'Mediana'
        especificacion.agregar_parametros(parametro, dificultad)
        if len(list(inv_pregunta.buscar_pregunta(especificacion))) > 0:
            preguntas = list(inv_pregunta.buscar_pregunta(especificacion))
            r = random.choice(preguntas)
            return r

    def cincuenta_cincuenta(r):
        if respuesta1.cget("text") == r.get_respuestaCorrecta():
            respuesta2.place(x=10000, y=10000)
            respuesta3.place(x=10000, y=10000)
        elif respuesta2.cget("text") == r.get_respuestaCorrecta():
            respuesta1.place(x=10000, y=10000)
            respuesta3.place(x=10000, y=10000)
        elif respuesta3.cget("text") == r.get_respuestaCorrecta():
            respuesta1.place(x=10000, y=10000)
            respuesta2.place(x=10000, y=10000)
        elif respuesta4.cget("text") == r.get_respuestaCorrecta():
            respuesta1.place(x=10000, y=10000)
            respuesta3.place(x=10000, y=10000)

    def preguntaAleatoria():
        r = preguntaCompleta()

        def combinacion1():
            labelPregunta.config(text=r.get_descripcion())
            respuesta1.config(text=r.get_respuestaCorrecta(),
                              command=respuestaCorrecta),
            respuesta2.config(text=r.get_respuestaIncorrecta1(),
                              command=respuestaIncorrecta),
            respuesta3.config(text=r.get_respuestaIncorrecta2(),
                              command=respuestaIncorrecta),
            respuesta4.config(text=r.get_respuestaIncorrecta3(),
                              command=respuestaIncorrecta)

        def combinacion2():
            labelPregunta.config(text=r.get_descripcion())
            respuesta1.config(text=r.get_respuestaIncorrecta1(),
                              command=respuestaIncorrecta),
            respuesta2.config(text=r.get_respuestaCorrecta(),
                              command=respuestaCorrecta),
            respuesta3.config(text=r.get_respuestaIncorrecta2(),
                              command=respuestaIncorrecta),
            respuesta4.config(text=r.get_respuestaIncorrecta3(),
                              command=respuestaIncorrecta)

        def combinacion3():
            labelPregunta.config(text=r.get_descripcion())
            respuesta1.config(text=r.get_respuestaIncorrecta1(),
                              command=respuestaIncorrecta),
            respuesta2.config(text=r.get_respuestaIncorrecta2(),
                              command=respuestaIncorrecta),
            respuesta3.config(text=r.get_respuestaCorrecta(),
                              command=respuestaCorrecta),
            respuesta4.config(text=r.get_respuestaIncorrecta3(),
                              command=respuestaIncorrecta)

        def combinacion4():
            labelPregunta.config(text=r.get_descripcion())
            respuesta1.config(text=r.get_respuestaIncorrecta1(),
                              command=respuestaIncorrecta),
            respuesta2.config(text=r.get_respuestaIncorrecta2(),
                              command=respuestaIncorrecta),
            respuesta3.config(text=r.get_respuestaIncorrecta3(),
                              command=respuestaIncorrecta),
            respuesta4.config(text=r.get_respuestaCorrecta(),
                              command=respuestaCorrecta)

        listaCombinaciones = [combinacion1, combinacion2, combinacion3, combinacion4]
        combinacionelegida = random.choice(listaCombinaciones)
        if combinacionelegida == combinacion1:
            combinacion1()
        elif combinacionelegida == combinacion2:
            combinacion2()
        elif combinacionelegida == combinacion3:
            combinacion3()
        elif combinacionelegida == combinacion4:
            combinacion4()
        else:
            tk.messagebox.showwarning('Error', 'No hemos podido encontrar estas preguntas')
        return r

    pygame.mixer.Sound.play(sonido_preguntas, -1)
    ventana.withdraw()
    win = tk.Toplevel()
    win.geometry("740x350")
    win.resizable(False, False)
    win.configure(bg="blue")
    win.iconbitmap("./img/icon.ico")
    win.title("QUIEN QUIERE SER MILLONARIO")
    fontStyle = tkFont.Font(family="Lucida Grande", size=12)
    premio10 = tk.Label(win, text=contador.get(), bg="green", font=fontStyle)
    premio10.place(x=350, y=250)
    labelPregunta = tk.Label(win, text="pregunta", bg="white", width=100, height=1)
    labelPregunta.place(x=20, y=10)
    respuesta1 = tk.Button(win, text="A. respuesta 1", bg="white", width=50, height=1)
    respuesta1.place(x=200, y=40)
    respuesta2 = tk.Button(win, text="B. respuesta 2", bg="white", width=50, height=1)
    respuesta2.place(x=200, y=70)
    respuesta3 = tk.Button(win, text="C. respuesta 3", bg="white", width=50, height=1)
    respuesta3.place(x=200, y=100)
    respuesta4 = tk.Button(win, text="D. respuesta 4", bg="white", width=50, height=1)
    respuesta4.place(x=200, y=130)
    r = preguntaAleatoria()
    tk.Button(win, text="Guardar partida", bg="white", width=20, height=1).place(x=300, y=200)
    tk.Button(win, text="50:50", bg="white", width=20, height=1, command=lambda: cincuenta_cincuenta(r)).place(x=300,
                                                                                                               y=300)


def abrirVentanaDificultadAlta():
    def respuestaCorrecta():
        respuesta1.place(x=200, y=40)
        respuesta2.place(x=200, y=70)
        respuesta3.place(x=200, y=100)
        respuesta4.place(x=200, y=130)
        preguntaAleatoria()
        contar()
        premio10.config(text=contador.get())
        print(contador.get())
        win.update()

    def respuestaIncorrecta():
        tk.messagebox.showwarning('Mal', 'Ha terminado la partida')
        win.withdraw()
        contador.set(str(int(100000)))
        cargaInicioDeSesion()

    def preguntaCompleta():
        especificacion = Especificacion()
        for file2 in os.listdir("FilesPreguntas"):
            if '.json' in file2:
                try:
                    inv_pregunta.agregar_pregunta(PersistenciaPregunta.load_json(file2))
                except Exception as ex:
                    pass
        parametro = 'dificultad'
        dificultad = 'Alta'
        especificacion.agregar_parametros(parametro, dificultad)
        if len(list(inv_pregunta.buscar_pregunta(especificacion))) > 0:
            preguntas = list(inv_pregunta.buscar_pregunta(especificacion))
            r = random.choice(preguntas)
            return r

    def cincuenta_cincuenta(r):
        if respuesta1.cget("text") == r.get_respuestaCorrecta():
            respuesta2.place(x=10000, y=10000)
            respuesta3.place(x=10000, y=10000)
        elif respuesta2.cget("text") == r.get_respuestaCorrecta():
            respuesta1.place(x=10000, y=10000)
            respuesta3.place(x=10000, y=10000)
        elif respuesta3.cget("text") == r.get_respuestaCorrecta():
            respuesta1.place(x=10000, y=10000)
            respuesta2.place(x=10000, y=10000)
        elif respuesta4.cget("text") == r.get_respuestaCorrecta():
            respuesta1.place(x=10000, y=10000)
            respuesta3.place(x=10000, y=10000)

    def preguntaAleatoria():
        r = preguntaCompleta()

        def combinacion1():
            labelPregunta.config(text=r.get_descripcion())
            respuesta1.config(text=r.get_respuestaCorrecta(),
                              command=respuestaCorrecta),
            respuesta2.config(text=r.get_respuestaIncorrecta1(),
                              command=respuestaIncorrecta),
            respuesta3.config(text=r.get_respuestaIncorrecta2(),
                              command=respuestaIncorrecta),
            respuesta4.config(text=r.get_respuestaIncorrecta3(),
                              command=respuestaIncorrecta)

        def combinacion2():
            labelPregunta.config(text=r.get_descripcion())
            respuesta1.config(text=r.get_respuestaIncorrecta1(),
                              command=respuestaIncorrecta),
            respuesta2.config(text=r.get_respuestaCorrecta(),
                              command=respuestaCorrecta),
            respuesta3.config(text=r.get_respuestaIncorrecta2(),
                              command=respuestaIncorrecta),
            respuesta4.config(text=r.get_respuestaIncorrecta3(),
                              command=respuestaIncorrecta)

        def combinacion3():
            labelPregunta.config(text=r.get_descripcion())
            respuesta1.config(text=r.get_respuestaIncorrecta1(),
                              command=respuestaIncorrecta),
            respuesta2.config(text=r.get_respuestaIncorrecta2(),
                              command=respuestaIncorrecta),
            respuesta3.config(text=r.get_respuestaCorrecta(),
                              command=respuestaCorrecta),
            respuesta4.config(text=r.get_respuestaIncorrecta3(),
                              command=respuestaIncorrecta)

        def combinacion4():
            labelPregunta.config(text=r.get_descripcion())
            respuesta1.config(text=r.get_respuestaIncorrecta1(),
                              command=respuestaIncorrecta),
            respuesta2.config(text=r.get_respuestaIncorrecta2(),
                              command=respuestaIncorrecta),
            respuesta3.config(text=r.get_respuestaIncorrecta3(),
                              command=respuestaIncorrecta),
            respuesta4.config(text=r.get_respuestaCorrecta(),
                              command=respuestaCorrecta)

        listaCombinaciones = [combinacion1, combinacion2, combinacion3, combinacion4]
        combinacionelegida = random.choice(listaCombinaciones)
        if combinacionelegida == combinacion1:
            combinacion1()
        elif combinacionelegida == combinacion2:
            combinacion2()
        elif combinacionelegida == combinacion3:
            combinacion3()
        elif combinacionelegida == combinacion4:
            combinacion4()
        else:
            tk.messagebox.showwarning('Error', 'No hemos podido encontrar estas preguntas')
        return r

    pygame.mixer.Sound.play(sonido_preguntas, -1)
    ventana.withdraw()
    win = tk.Toplevel()
    win.geometry("740x350")
    win.resizable(False, False)
    win.configure(bg="blue")
    win.iconbitmap("./img/icon.ico")
    win.title("QUIEN QUIERE SER MILLONARIO")
    fontStyle = tkFont.Font(family="Lucida Grande", size=12)
    premio10 = tk.Label(win, text=contador.get(), bg="green", font=fontStyle)
    premio10.place(x=350, y=250)
    labelPregunta = tk.Label(win, text="pregunta", bg="white", width=100, height=1)
    labelPregunta.place(x=20, y=10)
    respuesta1 = tk.Button(win, text="A. respuesta 1", bg="white", width=50, height=1)
    respuesta1.place(x=200, y=40)
    respuesta2 = tk.Button(win, text="B. respuesta 2", bg="white", width=50, height=1)
    respuesta2.place(x=200, y=70)
    respuesta3 = tk.Button(win, text="C. respuesta 3", bg="white", width=50, height=1)
    respuesta3.place(x=200, y=100)
    respuesta4 = tk.Button(win, text="D. respuesta 4", bg="white", width=50, height=1)
    respuesta4.place(x=200, y=130)
    r = preguntaAleatoria()
    tk.Button(win, text="Guardar partida", bg="white", width=20, height=1).place(x=300, y=200)
    tk.Button(win, text="50:50", bg="white", width=20, height=1, command=lambda: cincuenta_cincuenta(r)).place(x=300,
                                                                                                               y=300)


def abrirVentana4():
    def juegoDificultadBaja():
        win3.withdraw()
        abrirVentanaDificultadBaja()

    def juegoDificultadMediana():
        win3.withdraw()
        abrirVentanaDificultadMediana()

    def juegodificultadAlta():
        win3.withdraw()
        abrirVentanaDificultadAlta()

    ventana.withdraw()
    win3 = tk.Toplevel()
    win3.geometry("400x300")
    win3.resizable(False, False)
    win3.title("Que Deseas |")
    win3.iconbitmap("./img/icon.ico")
    win3.config(background="RoyalBlue3")
    main_title = tk.Label(win3, text="Escoge la dificultad", font=("Cambria", 14), bg="blue4", fg="black",
                          width="40",
                          height="2")
    main_title.pack()
    submit_btn1 = tk.Button(win3, text="Baja", width="30", height="2", command=juegoDificultadBaja, bg="white")
    submit_btn1.place(x=85, y=110)
    submit_btn2 = tk.Button(win3, text="Mediana", width="30", height="2", command=juegoDificultadMediana,
                            bg="white")
    submit_btn2.place(x=85, y=170)

    submit_btn3 = tk.Button(win3, text="Alta", width="30", height="2", command=juegodificultadAlta, bg="white")
    submit_btn3.place(x=85, y=230)


def cerrarVentana():
    ventana.destroy()


ventana = tk.Tk()
ventana.geometry("400x300")
ventana.configure(bg="blue")
ventana.iconbitmap("./img/icon.ico")
ventana.resizable(False, False)
ventana.title("QUIEN QUIERE SER MILLONARIO")
img = ImageTk.PhotoImage(Image.open("img/img3.png"))
label = tk.Label(ventana, image=img, bg="blue").place(x=71, y=10)
contador = tk.StringVar(ventana, "100000")
boton = tk.Button(text="Registrarse", bg="white", width=20, height=1, command=abrirVentanaRegistro).place(x=215, y=200)
boton2 = tk.Button(text="Iniciar Sesion", bg="white", width=20, height=1, command=abrirVentanaInicioSesion).place(x=30,
                                                                                                                  y=200)

ventana.mainloop()
