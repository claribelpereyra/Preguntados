import random

######### CONSTANTES ##################
tematicas = ["HISTORIA", "DEPORTE", "CIENCIA", "ARTE", "GEOGRAFIA", "ENTRETENIMIENTO"]


###########  FUNCIONES ###########

def eleccion_tematica():
    # TODO: Validaciones de input
    print("Bienvenido al preguntados, estas son las categorias disponibles: ")
    for i in range(len(tematicas)):
        print(i + 1, " - ", tematicas[i])
    print("O ingrese FIN para salir del juego. ")
    # Aca tambien puede elegir si terminar el juego o no
    opcion_elegida = input("Ingrese la opcion elegida: ")

    if opcion_elegida != "FIN":
        tematica = tematicas[int(opcion_elegida) - 1]
        del tematicas[int(opcion_elegida) - 1]
    else:
        tematica = opcion_elegida
    return tematica


def eleccion_preguntas(tematica):
    nro_preg = random.randint(0, 1)

    if tematica == 'HISTORIA':
        if nro_preg == 0:
            pregunta = ["pregunta historia 1?", "opcion1", "opcion2", "opcion3", 1]
        elif nro_preg == 1:
            pregunta = ["pregunta historia 2?", "opcion1", "opcion2", "opcion3", 1]

    elif tematica == "DEPORTE":
        if nro_preg == 0:
            pregunta = ["pregunta deporte 1?", "opcion1", "opcion2", "opcion3", 1]
        elif nro_preg == 1:
            pregunta = ["pregunta deporte 2?", "opcion1", "opcion2", "opcion3", 1]

    elif tematica == "CIENCIA":
        if nro_preg == 0:
            pregunta = ["pregunta ciencia 1?", "opcion1", "opcion2", "opcion3", 1]
        elif nro_preg == 1:
            pregunta = ["pregunta ciencia 2?", "opcion1", "opcion2", "opcion3", 1]

    elif tematica == "ARTE":
        if nro_preg == 0:
            pregunta = ["pregunta arte 1?", "opcion1", "opcion2", "opcion3", 1]
        elif nro_preg == 1:
            pregunta = ["pregunta arte 2?", "opcion1", "opcion2", "opcion3", 1]

    elif tematica == "GEOGRAFIA":
        if nro_preg == 0:
            pregunta = ["pregunta geografia 1?", "opcion1", "opcion2", "opcion3", 1]
        elif nro_preg == 1:
            pregunta = ["pregunta geografia 2 ?", "opcion1", "opcion2", "opcion3", 1]

    else:
        if nro_preg == 0:
            pregunta = ["pregunta entretenimiento 1 ?", "opcion1", "opcion2", "opcion3", 1]
        elif nro_preg == 1:
            pregunta = ["pregunta? entretenimiento 2 ?", "opcion1", "opcion2", "opcion3", 1]

    return pregunta


def ejecucion_juego():
    puntos = 0
    vidas = 5
    tematica = eleccion_tematica()

    while tematica != "FIN" and vidas > 0:
        pregunta = eleccion_preguntas(tematica)

        for i in range(len(pregunta) - 1):
            print(pregunta[i])

        opcion_elegida = int(input("Ingrese su respuesta: "))

        if opcion_elegida == pregunta[4]:
            print("Respuesta correcta")
            puntos += 10
        else:
            print("Respuesta incorrecta")
            while (opcion_elegida != pregunta[4]) and vidas > 0:
                vidas -= 1
                print("Te quedan ", vidas, "vidas.")

                if vidas > 0:
                    pregunta = eleccion_preguntas(tematica)

                    for i in range(len(pregunta) - 1):
                        print(pregunta[i])

                    opcion_elegida = int(input("Ingrese su respuesta: "))

                    if opcion_elegida == pregunta[4]:
                        print("Respuesta correcta")
                        puntos += 5
        if len(tematicas) > 0 and vidas > 0:
            tematica = eleccion_tematica()
        else:
            tematica = "FIN"

    if vidas > 0 and len(tematicas) == 0:
        print("GANASTE!!!")
        print("Respuestas correctas y puntos, ", puntos)
    elif vidas > 0 and len(tematicas) > 0:
        print("ABANDONASTE")

    elif vidas == 0 and len(tematicas) > 0:
        print("PERDISTE.")


ejecucion_juego()
