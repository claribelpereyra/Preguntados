import random

######### CONSTANTES ##################
tematicas = ["HISTORIA", "DEPORTE", "CIENCIA", "ARTE", "GEOGRAFIA", "ENTRETENIMIENTO"]
inputs_validos = ["FIN", '1', '2', '3', '4', '5', '6']


###########  FUNCIONES ###########

def eleccion_tematica(opcion_elegida):
    # TODO: Validaciones de input

    if opcion_elegida != "FIN":
        tematica = tematicas[int(opcion_elegida) - 1]
        del tematicas[int(opcion_elegida) - 1]
        del inputs_validos[-1]
    else:
        tematica = opcion_elegida
    return tematica


def validar_input(input):
    es_valido = False
    cant_validaciones = 0
    while es_valido is False and cant_validaciones < len(inputs_validos):
        for i in range(len(inputs_validos)):
            if str(input) == inputs_validos[i]:
                es_valido = True
            cant_validaciones += 1
    return es_valido


def imprimir_tematicas(tematicas):
    for i in range(len(tematicas)):
        print(i + 1, " - ", tematicas[i])
    print("O ingrese FIN para salir del juego. ")


def imprimir_pregunta(pregunta):
    for i in range(len(pregunta) - 1):
        print(pregunta[i])


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


def main():
    puntos = 0
    vidas = 5
    tematica = ""

    print(r" ____  ____  _____ ____ _   _ _   _ _____  _    ____   ___  ____")
    print(r"|  _ \|  _ \| ____/ ___| | | | \ | |_   _|/ \  |  _ \ / _ \/ ___|")
    print(r"| |_) | |_) |  _|| |  _| | | |  \| | | | / _ \ | | | | | | \___ \ ")
    print(r"|  __/|  _ <| |__| |_| | |_| | |\  | | |/ ___ \| |_| | |_| |___) |")
    print(r"|_|   |_| \_\_____\____|\___/|_| \_| |_/_/   \_\____/ \___/|____/ ")

    while tematica != "FIN" and vidas > 0:

        imprimir_tematicas(tematicas)

        tematica_elegida = input("Ingrese la opcion elegida: ")
        validacion = validar_input(tematica_elegida)

        while validacion is False:
            print("La opcion ingresada es incorrecta.")
            tematica_elegida = input("Ingrese la opcion elegida: ")
            validacion = validar_input(tematica_elegida)
        tematica = eleccion_tematica(tematica_elegida)
        if tematica != "FIN":
            pregunta = eleccion_preguntas(tematica)

            imprimir_pregunta(pregunta)

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

                        imprimir_pregunta(pregunta)

                        opcion_elegida = int(input("Ingrese su respuesta: "))

                        if opcion_elegida == pregunta[4]:
                            print("Respuesta correcta")
                            puntos += 5
        if len(tematicas) == 0 and vidas == 0:
            tematica = "FIN"

    if vidas > 0 and len(tematicas) == 0:
        print("GANASTE!!!")
        print("Respuestas correctas y puntos, ", puntos)
    elif vidas > 0 and len(tematicas) > 0:
        print("ABANDONASTE")

    elif vidas == 0 and len(tematicas) > 0:
        print("PERDISTE.")


main()
