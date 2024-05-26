import random

######### CONSTANTES ##################
tematicas = ["HISTORIA", "DEPORTE", "CIENCIA", "ARTE", "GEOGRAFIA", "ENTRETENIMIENTO"]

preg_historia = [[1, "pregunta?", "opcion1", "opcion2", "opcion3"],
                 [2, "pregunta?", "opcion1", "opcion2", "opcion3"]]
preg_deporte = [[1, "pregunta?", "opcion1", "opcion2", "opcion3"],
                [2, "pregunta?", "opcion1", "opcion2", "opcion3"]]
preg_ciencia = [[1, "pregunta?", "opcion1", "opcion2", "opcion3"],
                [2, "pregunta?", "opcion1", "opcion2", "opcion3"]]
preg_arte = [[1, "pregunta?,", "opcion1", "opcion2", "opcion3"],
             [2, "pregunta?", "opcion1", "opcion2", "opcion3"]]
preg_geografia = [[1, "pregunta?", "opcion1", "opcion2", "opcion3"],
                  [2, "pregunta?", "opcion1", "opcion2", "opcion3"]]
preg_entretenimiento = [[1, "pregunta?", "opcion1", "opcion2", "opcion3"],
                        [2, "pregunta?", "opcion1", "opcion2", "opcion3"]]


###########  FUNCIONES ###########

def eleccion_tematica():
    # TODO: Validaciones de input
    # Aca tambien puede elegir si terminar el juego o no
    tematica = int(input("Ingrese la tematica ...... : "))

    return tematica


def eleccion_preguntas(tematica):
    nro_preg = random.randint(0, 1)

    if tematica == 1:
        if nro_preg == 0:
            pregunta = ["pregunta?", "opcion1", "opcion2", "opcion3", "opcionok"]
        elif nro_preg == 1:
            pregunta = ["pregunta?", "opcion1", "opcion2", "opcion3", "opcionok"]

    elif tematica == 2:
        if nro_preg == 0:
            pregunta = ["pregunta?", "opcion1", "opcion2", "opcion3", "opcionok"]
        elif nro_preg == 1:
            pregunta = ["pregunta?", "opcion1", "opcion2", "opcion3", "opcionok"]

    elif tematica == 3:
        if nro_preg == 0:
            pregunta = ["pregunta?", "opcion1", "opcion2", "opcion3", "opcionok"]
        elif nro_preg == 1:
            pregunta = ["pregunta?", "opcion1", "opcion2", "opcion3", "opcionok"]

    elif tematica == 4:
        if nro_preg == 0:
            pregunta = ["pregunta?", "opcion1", "opcion2", "opcion3", "opcionok"]
        elif nro_preg == 1:
            pregunta = ["pregunta?", "opcion1", "opcion2", "opcion3", "opcionok"]

    elif tematica == 5:
        if nro_preg == 0:
            pregunta = ["pregunta?", "opcion1", "opcion2", "opcion3", "opcionok"]
        elif nro_preg == 1:
            pregunta = ["pregunta?", "opcion1", "opcion2", "opcion3", "opcionok"]

    else:
        if nro_preg == 0:
            pregunta = ["pregunta?", "opcion1", "opcion2", "opcion3", "opcionok"]
        elif nro_preg == 1:
            pregunta = ["pregunta?", "opcion1", "opcion2", "opcion3", "opcionok"]

    return pregunta


def ejecucion_juego():
    puntos = 0
    tematica = 0

    while tematica != -1:

        tematica = eleccion_tematica()
        pregunta = eleccion_preguntas(tematica)

        for i in range(len(pregunta)-1):
            print(pregunta[i])

        opcion_elegida = int(input("Ingrese su respuesta: hola "))

        if opcion_elegida == pregunta[4]:
            print("Respuesta correcta, Felicitaciones!!")
            puntos += 10
        else:
            print("Respuesta incorrecta")

        tematica = eleccion_tematica()


print("Respuestas correctas y puntos")
