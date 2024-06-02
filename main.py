import random

# CONSTANTES
dificultad = ["BÁSICO", "DIFÍCIL", "EXPERTO"]
inputs_validosDificultad = ["FIN", '1', '2', '3']
categorias = ["HISTORIA", "DEPORTE", "CIENCIA", "ARTE", "GEOGRAFIA", "ENTRETENIMIENTO"]
inputs_validos_categorias = ["FIN", '1', '2', '3', '4', '5', '6']

# FUNCIONES

def dificultad_seleccionada(eleccion_dificultad):
    """Va a mostrar la dicultad correspondiente a la opción ingresada.
    :param dificultad_elegida: es un string, por lo que 
     muestra el valor correspondiente a la dificultad elegida. 
    Solo acpeta "FIN" o un número entre 1
    y el largo de la lista dificultad
    """
    if eleccion_dificultad == "1":
        return "BÁSICO"
    elif eleccion_dificultad == "2":
        return "DIFÍCIL"
    elif eleccion_dificultad == "3":
        return "EXPERTO"
    else:
        return None

def imprimir_dificultades(dificultad):
    for i in range(len(dificultad)):
        print(i + 1, " - ", dificultad[i])
    print("O ingresá FIN para salir del juego. ")

def validarDificultad(eleccion):
    return eleccion in inputs_validosDificultad

# FUNCIONES

def eleccion_categoria(categoria_elegida):
    """ Devuelve la categoria correspondiente a la opción ingresada.
    :param categoria_elegida: Str, valor correspondiente a la categoria elegida. Tiene que ser "FIN" o un número entre 1
                              y el largo de la lista categorias.
    :return tematica: Str, categoria válida."""

    if categoria_elegida != "FIN":
        # Buscamos la categoria correspondiente al numero ingresado, como las opciones van de 1 al largo de la lista
        # para tener el indice correcto vamos a restarle una a la opcion ingresada.
        tematica = categorias[int(categoria_elegida) - 1]
        # Borramos la categoria elegida para que ya no sea una opción para el usuario.
        del categorias[int(categoria_elegida) - 1]
        # Borramos el ultimo elemento de la lista de inputs validos, ya que va a tener una opcion menos disponible
        # para ingresar.
        del inputs_validos_categorias[-1]
    else:
        tematica = categoria_elegida
    return tematica


def validar_input(dato_ingresado):
    """Valida que el input ingresado para las categorias este en el rango correcto de opciones disponibles.
    :param dato_ingresado: Str, valor ingresado por teclado del usuario.
    :return es_valido: Bool, devuelve True si es un input valido o False en caso contrario."""

    es_valido = False
    i = 0
    # Mientras el input no sea valido y todavia queden elementos en la lista de inputs_validos_categorias para comparar,
    # se comparara el dato ingresado con los valores esperados.
    while es_valido is False and i < len(inputs_validos_categorias):
        # Si el dato ingresado es igual a alguno de los datos que en la lista inputs_validos_categorias cambia el valor
        # de es_valido a True.
        if dato_ingresado == inputs_validos_categorias[i]:
            es_valido = True
        i += 1
    return es_valido


def imprimir_categorias():
    """ Muestra por pantalla las categorias disponibles que tiene el usuario para elegir. """
    print("Elegi alguna de las categorias disponibles o ingresa FIN para salir del juego: ")
    for i in range(len(categorias)):
        print(i + 1, " - ", categorias[i])


def imprimir_pregunta(pregunta):
    """ Muestra por pantalla la pregunta y las opciones disponibles que tiene el usuario para elegir.
    :param pregunta: List, lista de cinco elementos."""

    # Imprime hasta el anteúltimo elemento, ya que el último indica la opcion
    # correcta contra la que validamos el resultado.
    for i in range(len(pregunta) - 1):
        print(pregunta[i])


def imprimir_resultado(vidas, tematicas, puntos):
    """ Muestra por pantalla el resultado del juego segun la cantidad disponible de categorias y vidas. """
    if vidas > 0 and len(tematicas) == 0:
        print("██████╗  █████╗ ███╗   ██╗ █████╗ ███████╗████████╗███████╗")
        print("██╔════╝ ██╔══██╗████╗  ██║██╔══██╗██╔════╝╚══██╔══╝██╔════╝")
        print("██║  ███╗███████║██╔██╗ ██║███████║███████╗   ██║   █████╗")
        print("██║   ██║██╔══██║██║╚██╗██║██╔══██║╚════██║   ██║   ██╔══╝")
        print("╚██████╔╝██║  ██║██║ ╚████║██║  ██║███████║   ██║   ███████╗")
        print("╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝")

        print("Vos si que sos más argentino que #completar ahre")

        print("Sumaste en total: ", puntos, "puntos.")
    elif vidas > 0 and len(tematicas) > 0:
        print("█████╗ ██████╗  █████╗ ███╗   ██╗██████╗  ██████╗ ███╗   ██╗ █████╗ ███████╗████████╗███████╗")
        print("██╔══██╗██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔═══██╗████╗  ██║██╔══██╗██╔════╝╚══██╔══╝██╔════╝")
        print("███████║██████╔╝███████║██╔██╗ ██║██║  ██║██║   ██║██╔██╗ ██║███████║███████╗   ██║   █████╗")
        print("██╔══██║██╔══██╗██╔══██║██║╚██╗██║██║  ██║██║   ██║██║╚██╗██║██╔══██║╚════██║   ██║   ██╔══╝")
        print("██║  ██║██████╔╝██║  ██║██║ ╚████║██████╔╝╚██████╔╝██║ ╚████║██║  ██║███████║   ██║   ███████╗")
        print("╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝")

        print("Que pecho frio, anda a estudiar y volve!")

    elif vidas == 0 and len(tematicas) > 0:
        print(r"PERDISTE y por eso ni un banner te hacemos ¯\_(ツ)_/¯ ")


def eleccion_preguntas(categoria):
    """Según la categoria ingresada devuelve una pregunta elegida de manera random.
    :param categoria: Str, nombre de la categoria elegida.
    :return pregunta: List, lista con la pregunta, las opciones disponibles y la opcion correcta."""

    nro_preg = random.randint(0, 1)

    if categoria == 'HISTORIA':
        if nro_preg == 0:
            pregunta = ["pregunta historia 1?", "opcion1", "opcion2", "opcion3", 1]
        elif nro_preg == 1:
            pregunta = ["pregunta historia 2?", "opcion1", "opcion2", "opcion3", 1]

    elif categoria == "DEPORTE":
        if nro_preg == 0:
            pregunta = ["pregunta deporte 1?", "opcion1", "opcion2", "opcion3", 1]
        elif nro_preg == 1:
            pregunta = ["pregunta deporte 2?", "opcion1", "opcion2", "opcion3", 1]

    elif categoria == "CIENCIA":
        if nro_preg == 0:
            pregunta = ["pregunta ciencia 1?", "opcion1", "opcion2", "opcion3", 1]
        elif nro_preg == 1:
            pregunta = ["pregunta ciencia 2?", "opcion1", "opcion2", "opcion3", 1]

    elif categoria == "ARTE":
        if nro_preg == 0:
            pregunta = ["pregunta arte 1?", "opcion1", "opcion2", "opcion3", 1]
        elif nro_preg == 1:
            pregunta = ["pregunta arte 2?", "opcion1", "opcion2", "opcion3", 1]

    elif categoria == "GEOGRAFIA":
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
    """Función encargada de la ejecución del juego."""
    puntos = 0
    vidas = 5
    tematica = ""

    print(
        "██████╗ ██╗███████╗███╗   ██╗██╗   ██╗███████╗███╗   ██╗██╗██████╗  ██████╗      █████╗ ██╗          █████╗ ██████╗  ██████╗ ███████╗███╗   ██╗████████╗ █████╗ ██████╗  ██████╗ ███████╗    ██╗")
    print(
        "██╔══██╗██║██╔════╝████╗  ██║██║   ██║██╔════╝████╗  ██║██║██╔══██╗██╔═══██╗    ██╔══██╗██║         ██╔══██╗██╔══██╗██╔════╝ ██╔════╝████╗  ██║╚══██╔══╝██╔══██╗██╔══██╗██╔═══██╗██╔════╝    ██║")
    print(
        "██████╔╝██║█████╗  ██╔██╗ ██║██║   ██║█████╗  ██╔██╗ ██║██║██║  ██║██║   ██║    ███████║██║         ███████║██████╔╝██║  ███╗█████╗  ██╔██╗ ██║   ██║   ███████║██║  ██║██║   ██║███████╗    ██║")
    print(
        "██╔══██╗██║██╔══╝  ██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║██║  ██║██║   ██║    ██╔══██║██║         ██╔══██║██╔══██╗██║   ██║██╔══╝  ██║╚██╗██║   ██║   ██╔══██║██║  ██║██║   ██║╚════██║    ╚═╝")
    print(
        "██████╔╝██║███████╗██║ ╚████║ ╚████╔╝ ███████╗██║ ╚████║██║██████╔╝╚██████╔╝    ██║  ██║███████╗    ██║  ██║██║  ██║╚██████╔╝███████╗██║ ╚████║   ██║   ██║  ██║██████╔╝╚██████╔╝███████║    ██╗")
    print(
        "╚═════╝ ╚═╝╚══════╝╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═╝╚═════╝  ╚═════╝     ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝    ╚═╝")
    print(" A continuacion te explicamos las reglas: ")
    print(
        "* Vas a tener seis categorias en las cuales vas a encontrar preguntas relacionadas a nuestro país, para ganar vas a tener que contestar al menos una bien en cada categoria.")
    print("* Las condiciones son: - Tenes 5 vidas en total y solo podes elegir cada categoria una vez.")
    print("                       - Una vez que elegiste una categoria no la podes cambiar.")
    print(
        "                       - Cada pregunta correcta suma 10 puntos, si es tu segundo intento o posterior suma 5. ")

    input("Para continuar presiona cualquier tecla: ")
    print("")

    while dificultad_seleccionada != "FIN":
        print("Elegí la dificultad del juego")
        imprimir_dificultades(dificultad)
        print("")
        dificultad_elegida = input("Ingresá la opcion elegida: ")
        validacion = validarDificultad(dificultad_elegida)

        while not validacion:
            print("Valor ingresado no valido. Por favor, intentá nuevamente")
            print("")   
            imprimir_dificultades(dificultad)
            dificultad_elegida = input("Dale, elegí la dificultad del juego: ")
            validacion = validarDificultad(dificultad_elegida)

        if dificultad_seleccionada == "FIN":
            print("Juego no inciiado. Saliste del juego, hasta la próxima!")
            dificultad_seleccionada = "FIN"  # Seteamos la dificultad_seleccionada a "FIN" para salir del bucle
        else:
            dificultad_seleccionada = dificultad_seleccionada(dificultad_elegida)
            print("Dificultad elegida:", dificultad_seleccionada)
        
        while tematica != "FIN" and vidas > 0 and len(categorias) > 0:
            imprimir_categorias()
            categoria_elegida = input("Ingrese la opcion elegida: ")
            validacion = validar_input(categoria_elegida)

            while validacion is False:
                print("Che, dale, elegime una opcion valida!")
                categoria_elegida = input("Ingrese la opcion elegida: ")
                validacion = validar_input(categoria_elegida)

            tematica = eleccion_categoria(categoria_elegida)
            if tematica != "FIN":
                pregunta = eleccion_preguntas(tematica)
                imprimir_pregunta(pregunta)

                opcion_elegida = int(input("Ingrese su respuesta: "))

                if opcion_elegida == pregunta[4]:
                    print("Le pegaste! Felicitaciones, sumaste 10 puntos ٩( ๑╹ ꇴ╹)۶")
                    puntos += 10
                else:
                    print("Te equivocaste pichón ಠ_ಠ")

                    while (opcion_elegida != pregunta[4]) and vidas > 0:
                        vidas -= 1

                    while tematica != "FIN" and vidas > 0 and len(categorias) > 0:

                        imprimir_categorias()
        categoria_elegida = input("Ingrese la opcion elegida: ")
        validacion = validar_input(categoria_elegida)

        while validacion is False:
            print("Che, dale, elegime una opcion valida!")
            categoria_elegida = input("Ingrese la opcion elegida: ")
            validacion = validar_input(categoria_elegida)

        tematica = eleccion_categoria(categoria_elegida)
        if tematica != "FIN":
            pregunta = eleccion_preguntas(tematica)

            imprimir_pregunta(pregunta)

            opcion_elegida = int(input("Ingrese su respuesta: "))

            if opcion_elegida == pregunta[4]:
                print("Le pegaste! Felicitaciones, sumaste 10 puntos ٩( ๑╹ ꇴ╹)۶")
                puntos += 10
            else:
                print("Te equivocaste pichón ಠ_ಠ")

                while (opcion_elegida != pregunta[4]) and vidas > 0:
                    vidas -= 1

                    if vidas > 0:
                        print("Pero igual te quedan ", vidas, "vidas. Asi que podes volver a intentar con otra "
                                                              "pregunta!")
                        pregunta = eleccion_preguntas(tematica)
                        imprimir_pregunta(pregunta)
                        opcion_elegida = int(input("Ingrese su respuesta: "))

                        if opcion_elegida == pregunta[4]:
                            print("Hasta que adivinaste!, ahora sumas 5 puntos.")
                            puntos += 5
                    else:
                        print("Te quedaste sin vidas, que mala leche!")
        if len(categorias) == 0 and vidas == 0:
            tematica = "FIN"

    imprimir_resultado(vidas, categorias, puntos)


main()