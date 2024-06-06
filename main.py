import random

# CONSTANTES
niveles_dificultad = ["BÁSICO", "DIFÍCIL", "EXPERTO"]
inputs_validos_dificultad = ["FIN", "1", "2", "3"]
inputs_validos_categorias = ["FIN", "1", "2", "3", "4", "5", "6"]
inputs_validos_preguntas = ["1", "2", "3", "4"]
categorias = ["HISTORIA", "DEPORTE", "CIENCIA", "ARTE", "GEOGRAFIA", "ENTRETENIMIENTO"]


# FUNCIONES

# FUNCIONES DE IMRPRESION


def imprimir_dificultades():
    """Muestra por pantalla los niveles de dificultad."""
    for i in range(len(niveles_dificultad)):
        print(i + 1, " - ", niveles_dificultad[i])
    print("O ingresá FIN para salir del juego. ")


def imprimir_categorias():
    """Muestra por pantalla las categorias disponibles que tiene el usuario para elegir."""
    print(
        "Elegi alguna de las categorias disponibles o ingresa FIN para salir del juego: "
    )
    for i in range(len(categorias)):
        print(i + 1, " - ", categorias[i])


def imprimir_pregunta(pregunta):
    """Muestra por pantalla la pregunta y las opciones disponibles que tiene el usuario para elegir.
    :param pregunta: List, lista de cinco elementos."""

    # Imprime hasta el anteúltimo elemento, ya que el último indica la opcion
    # correcta contra la que validamos el resultado.
    for i in range(len(pregunta) - 1):
        if i > 0:
            print(i, " - ", pregunta[i])
        else:
            print(pregunta[i])


def imprimir_resultado(vidas, tematicas, puntos):
    """Muestra por pantalla el resultado del juego segun la cantidad disponible de categorias y vidas."""
    if vidas > 0 and len(tematicas) == 0:
        print("██████╗  █████╗ ███╗   ██╗ █████╗ ███████╗████████╗███████╗")
        print("██╔════╝ ██╔══██╗████╗  ██║██╔══██╗██╔════╝╚══██╔══╝██╔════╝")
        print("██║  ███╗███████║██╔██╗ ██║███████║███████╗   ██║   █████╗")
        print("██║   ██║██╔══██║██║╚██╗██║██╔══██║╚════██║   ██║   ██╔══╝")
        print("╚██████╔╝██║  ██║██║ ╚████║██║  ██║███████║   ██║   ███████╗")
        print("╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝")
        print("Vos si que sos más argentino que tener 4 presidentes en una semana!")

        print("Sumaste en total: ", puntos, "puntos.")
    elif vidas > 0 and len(tematicas) > 0:
        print(
            "█████╗ ██████╗  █████╗ ███╗   ██╗██████╗  ██████╗ ███╗   ██╗ █████╗ ███████╗████████╗███████╗"
        )
        print(
            "██╔══██╗██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔═══██╗████╗  ██║██╔══██╗██╔════╝╚══██╔══╝██╔════╝"
        )
        print(
            "███████║██████╔╝███████║██╔██╗ ██║██║  ██║██║   ██║██╔██╗ ██║███████║███████╗   ██║   █████╗"
        )
        print(
            "██╔══██║██╔══██╗██╔══██║██║╚██╗██║██║  ██║██║   ██║██║╚██╗██║██╔══██║╚════██║   ██║   ██╔══╝"
        )
        print(
            "██║  ██║██████╔╝██║  ██║██║ ╚████║██████╔╝╚██████╔╝██║ ╚████║██║  ██║███████║   ██║   ███████╗"
        )
        print(
            "╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝"
        )

        print("Que pecho frio, anda a estudiar y volve!")

    elif vidas == 0 and len(tematicas) > 0:
        print(r"PERDISTE y por eso ni un banner te hacemos ¯\_(ツ)_/¯ ")


# FUNCIONES DE VALIDACION DE INPUTS
def validar_dificultad(eleccion):
    """Valida que la dificultad seleccionada sea un input valido."""
    es_valido = False
    i = 0
    # Mientras el input no sea valido y todavia queden elementos en la lista de inputs_validos_dificultad para comparar,
    # se comparara el dato ingresado con los valores esperados.
    while es_valido is False and i < len(inputs_validos_dificultad):
        # Si el dato ingresado es igual a alguno de los datos que en la lista inputs_validos_dificultad cambia el valor
        # de es_valido a True.
        if eleccion == inputs_validos_dificultad[i]:
            es_valido = True
        i += 1

    return es_valido


def validar_respuestas(eleccion):
    """Chequea que la respuesta a la pregunta seleccionada sea un input valido."""
    es_valido = False
    i = 0
    # Mientras el input no sea valido y todavia queden elementos en la lista de inputs_validos_preguntas para comparar,
    # se comparara el dato ingresado con los valores esperados.
    while es_valido is False and i < len(inputs_validos_preguntas):
        # Si el dato ingresado es igual a alguno de los datos que en la lista inputs_validos_preguntas cambia el valor
        # de es_valido a True.
        if eleccion == inputs_validos_preguntas[i]:
            es_valido = True
        i += 1

    return es_valido


def validar_categoria(dato_ingresado):
    """Valida que el input ingresado para las categorias este en el rango correcto de opciones disponibles.
    :return es_valido: Bool, devuelve True si es un input valido o False en caso contrario.
    """

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


# FUNCIONES CON LOGICA DEL JUEGO


def dificultad_seleccionada(eleccion_dificultad):
    """Va a mostrar la dificultad correspondiente a la opción ingresada.
    :param eleccion_dificultad: es un string, por lo que
     muestra el valor correspondiente a la dificultad elegida.
    Solo acepta "FIN" o un número entre 1
    y el largo de la lista dificultad.
    :return dificultad: Str, nivel de dificultad.
    """
    if eleccion_dificultad == "1":
        dificultad = "BÁSICO"
    elif eleccion_dificultad == "2":
        dificultad = "DIFÍCIL"
    else:
        dificultad = "EXPERTO"
    return dificultad


def eleccion_categoria(categoria_elegida):
    """Devuelve la categoria correspondiente a la opción ingresada.
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


def eleccion_preguntas(categoria, eleccion_dificultad):
    """Según la categoria ingresada devuelve una pregunta elegida de manera random.
    :param categoria: Str, nombre de la categoria elegida.
    :param eleccion_dificultad: Str, tipo de dificultad elegida.
    :return pregunta: List, lista con la pregunta, las opciones disponibles y la opcion correcta.
    """
    nro_preg = random.randint(0, 9)
    if categoria == "HISTORIA":
        if eleccion_dificultad == "BÁSICO":
            if nro_preg == 0:
                pregunta = [
                    "¿En qué ciudad se firmó la Declaración de Independencia de Argentina?",
                    "Buenos Aires",
                    "Cordoba",
                    "Rosario",
                    "Tucuman",
                    4,
                ]
            elif nro_preg == 1:
                pregunta = [
                    "¿Qué importante evento se produjo en 1816 en Argentina?",
                    "La revolución de mayo",
                    "La Independencia",
                    "La Batalla de Caseros",
                    "La Constitución Nacional",
                    2,
                ]
            elif nro_preg == 2:
                pregunta = [
                    "¿Qué prócer argentino está en el billete de 100 pesos?",
                    "José de San Martín",
                    "Manuel Belgrano",
                    "Bartolomé Mitre",
                    "Eva Perón",
                    4,
                ]
            elif nro_preg == 3:
                pregunta = [
                    "¿En qué fecha se conmemora la Revolución de Mayo en Argentina?",
                    "9 de julio",
                    "25 de mayo",
                    "20 de junio",
                    "12 de octubre",
                    2,
                ]
            elif nro_preg == 4:
                pregunta = [
                    "¿Quién fue el primer presidente argentino electo democráticamente en 1983 después de la dictadura militar?",
                    "Juan Domingo Perón",
                    "Carlos Menem",
                    "Raúl Alfonsín",
                    "Fernando de la Rúa",
                    3,
                ]
            elif nro_preg == 5:
                pregunta = [
                    "¿Qué prócer argentino es conocido por crear la bandera?",
                    "José de San Martín",
                    "Manuel Belgrano",
                    "Juan Manuel de Rosas",
                    "Domingo Faustino Sarmiento",
                    2,
                ]
            elif nro_preg == 6:
                pregunta = [
                    "¿Qué política social es más asociada al peronismo?",
                    "Privatización de empresas pública",
                    "Reforma agraria",
                    "Justicia social y derechos laborales",
                    "Liberalización del comercio",
                    3,
                ]
            elif nro_preg == 7:
                pregunta = [
                    "¿En qué año se concedió el derecho al voto a las mujeres en Argentina?",
                    "1946",
                    "1947",
                    "1949",
                    "1951",
                    2,
                ]
            elif nro_preg == 8:
                pregunta = [
                    "¿Qué institución fue uno de los principales centros clandestinos de detención durante la dictadura?",
                    "ESMA (Escuela de Mecánica de la Armada)",
                    "Casa Rosada",
                    "Congreso de la Nación",
                    "Teatro Colón",
                    1,
                ]
            else:
                pregunta = [
                    "¿Qué término se utilizó para referirse al colapso financiero y social que tuvo lugar en Argentina en 2001?",
                    "La Gran Depresión",
                    "La Gran Recesión",
                    "El Corralito",
                    "La Inflación Galopante",
                    3,
                ]

        elif eleccion_dificultad == "DIFICIL":
            if nro_preg == 0:
                pregunta = [
                    "¿En qué año se aprobó la Ley de Educación Sexual Integral (ESI) en Argentina?",
                    "2006",
                    "1999",
                    "2010",
                    "2015",
                    1,
                ]
            elif nro_preg == 1:
                pregunta = [
                    "¿Qué organización de derechos humanos en Argentina lucha por la identidad y justicia de los niños nacidos en cautiverio durante la dictadura?",
                    "Abuelas de Plaza de Mayo",
                    "Madres de Plaza de Mayo",
                    "CELS",
                    "HIJOS",
                    2,
                ]

            elif nro_preg == 2:
                pregunta = [
                    "¿Qué ley estableció el matrimonio igualitario en Argentina?",
                    "Ley 26.618",
                    "Ley de Unión Civil",
                    "Ley de Género",
                    "Ley de Identidad de Género",
                    1,
                ]

            elif nro_preg == 3:
                pregunta = [
                    "¿Qué periodista y escritora fue una de las primeras en hablar sobre los derechos de las mujeres y los derechos humanos en la prensa argentina?",
                    "Victoria Ocampo",
                    "Alicia Moreau de Justo",
                    "María Elena Walsh",
                    "Eva Giberti",
                    1,
                ]

            elif nro_preg == 4:
                pregunta = [
                    "¿Qué presidente argentino fue el principal promotor del Plan de Convertibilidad?",
                    "Carlos Menem",
                    "Fernando de la Rúa",
                    "Eduardo Duhalde",
                    "Néstor Kirchner",
                    1,
                ]

            elif nro_preg == 5:
                pregunta = [
                    "¿Cuál fue el período conocido como la 'Conquista del Desierto' en Argentina?",
                    "Siglo XV",
                    "Siglo XVI",
                    "Siglo XIX",
                    "Siglo XX",
                    3,
                ]

            elif nro_preg == 6:
                pregunta = [
                    "¿Qué provincia argentina se convirtió en la primera en legalizar el cultivo de cannabis con fines medicinales en 2020?",
                    "Buenos Aires",
                    "Mendoza",
                    "Santa Fe",
                    "Jujuy",
                    4,
                ]

            elif nro_preg == 7:
                pregunta = [
                    "¿Qué hecho histórico ocurrió en Argentina el 30 de diciembre de 2020?",
                    "Legalización del aborto",
                    "Renuncia de un presidente",
                    "Aprobación de una ley importante",
                    "Celebración de un aniversario nacional",
                    1,
                ]

            elif nro_preg == 8:
                pregunta = [
                    "¿Qué importante movimiento político y social surgió en Argentina a fines del siglo XIX y principios del XX, liderado por Hipólito Yrigoyen?",
                    "Conservadurismo",
                    "Peronismo",
                    "Radicalismo",
                    "Socialismo",
                    3,
                ]

            else:
                pregunta = [
                    "¿Quién fue el presidente argentino que lideró el gobierno militar conocido como 'Revolución Libertadora' en 1955?",
                    "Juan Domingo Perón",
                    "Arturo Frondizi",
                    "Arturo Illia",
                    "Pedro Eugenio Aramburu",
                    4,
                ]

        else:
            if nro_preg == 0:
                pregunta = [
                    "¿Qué derecho laboral se consolidó con la Ley de Contrato de Trabajo de 1974?",
                    "Derecho a la huelga",
                    "Licencia por maternidad",
                    "Jornada laboral de ocho horas",
                    "Aguinaldo",
                    2,
                ]

            elif nro_preg == 1:
                pregunta = [
                    "¿Qué tratado firmó Argentina con Chile en 1984, poniendo fin al conflicto territorial en el Canal de Beagle?",
                    "Tratado de Lircay",
                    "Tratado de Madrid",
                    "Tratado de Río de Janeiro",
                    "Tratado de Paz y Amistad",
                    1,
                ]

            elif nro_preg == 2:
                pregunta = [
                    "¿Qué figura argentina fue galardonada con el Premio Nobel de la Paz en 1977 por su labor en la promoción de los derechos humanos?",
                    "Ernesto Sabato",
                    "Estela de Carlotto",
                    "Adolfo Pérez Esquivel",
                    "Hebe de Bonafini",
                    3,
                ]

            elif nro_preg == 3:
                pregunta = [
                    "¿Cuál fue el nombre del enfrentamiento militar ocurrido en Argentina en 1874 entre el gobierno nacional y las provincias rebeldes?",
                    "Revolución de Mayo",
                    "Batalla de Pavón",
                    "Guerra del Paraguay",
                    "Batalla de Caseros",
                    2,
                ]

            elif nro_preg == 4:
                pregunta = [
                    "¿Cuál fue la causa principal de la rebelión conocida como 'La Noche de los Bastones Largos' en 1966?",
                    "La intervención militar en la Universidad de Buenos Aires",
                    "La crisis económica y social provocada por la inflación",
                    "La represión contra manifestaciones estudiantiles",
                    "La nacionalización de la industria petrolera",
                    1,
                ]

            elif nro_preg == 5:
                pregunta = [
                    "¿Quién fue el líder sindical argentino que encabezó la Confederación General del Trabajo (CGT) durante la década de 1970 y fue secuestrado y desaparecido por la dictadura militar en 1977?",
                    "Juan Domingo Perón",
                    "Saúl Ubaldini",
                    "José Ignacio Rucci",
                    "Augusto Vandor",
                    3,
                ]

            elif nro_preg == 6:
                pregunta = [
                    "¿En qué año se implementó el Programa Nacional de Educación, Trabajo y Producción (PRONETT) en Argentina?",
                    "1980",
                    "1990",
                    "2000",
                    "2010",
                    2,
                ]

            elif nro_preg == 7:
                pregunta = [
                    "¿Qué líder mapuche lideró la resistencia contra la expansión del Estado argentino en el siglo XIX?",
                    "Patoruzú",
                    "Calfucurá",
                    "Pincén",
                    "Sayhueque",
                    2,
                ]

            elif nro_preg == 8:
                pregunta = [
                    "¿Cuál fue uno de los pueblos originarios más conocidos que habitó la región de la actual provincia de Buenos Aires antes de la llegada de los colonizadores europeos?",
                    "Querandíes",
                    "Mapuches",
                    "Tehuelches",
                    "Diaguitas",
                    1,
                ]

            else:
                pregunta = [
                    "¿Cuál fue el nombre del primer periódico feminista publicado en Argentina en el siglo XIX, fundado por Juana Manso?",
                    "La Nación Feminista",
                    "La Vanguardia Feminista",
                    "La Prensa Femenina",
                    "La Voz de la Mujer",
                    4,
                ]

    elif categoria == "DEPORTE":
        if eleccion_dificultad == "BÁSICO":
            # nivel basico
            if nro_preg == 0:
                pregunta = [
                    "¿Quién es Diego Maradona?",
                    "Un político",
                    "Un futbolista",
                    "Un actor",
                    "Un cantante",
                    2,
                ]
            elif nro_preg == 1:
                pregunta = [
                    "¿En qué deporte se destacó Gabriela Sabatini?",
                    "Fútbol",
                    "Natación",
                    "Tenis",
                    "Baloncesto",
                    3,
                ]
            elif nro_preg == 2:
                pregunta = [
                    "¿Quién es la destacada nadadora argentina que ganó tres medallas en los Juegos Olímpicos de la Juventud Buenos Aires 2018?",
                    "Delfina Pignatiello",
                    "Luciana Aymar",
                    "Cecilia Biagioli",
                    "Gabriela Sabatini",
                    1,
                ]
            elif nro_preg == 3:
                pregunta = [
                    "¿En qué deporte se destaca Paula Pareto?",
                    "Karate",
                    "Taekwondo",
                    "Judo",
                    "Lucha libre",
                    3,
                ]
            elif nro_preg == 4:
                pregunta = [
                    "¿En qué ciudad se encuentra el estadio Monumental?",
                    "Rosario",
                    "Córdoba",
                    "Buenos Aires",
                    "Mendoza",
                    3,
                ]
            elif nro_preg == 5:
                pregunta = [
                    "¿Qué selección ganó la Copa América 2021?",
                    "Chile",
                    "Brasil",
                    "Uruguay",
                    "Argentina",
                    4,
                ]
            elif nro_preg == 6:
                pregunta = [
                    "¿Cómo se llama el equipo de rugby nacional de Argentina?",
                    "Los Pumas",
                    "Los Cóndores",
                    "Los Jaguares",
                    "Los Leones",
                    1,
                ]
            elif nro_preg == 7:
                pregunta = [
                    "¿En qué deporte se destacó Luciana Aymar?",
                    "Tenis",
                    "Hockey sobre césped",
                    "Natación",
                    "Voleibol",
                    2,
                ]
            elif nro_preg == 8:
                pregunta = [
                    "¿Qué equipo argentino de fútbol es conocido como 'La Academia'?",
                    "San Lorenzo",
                    "Independiente",
                    "Racing",
                    "River Plate",
                    3,
                ]
            else:
                pregunta = [
                    "¿En qué deporte se destaca Lionel Messi?",
                    "Fútbol",
                    "Baloncesto",
                    "Tenis",
                    "Rugby",
                    1,
                ]
        # nivel intermedio
        elif eleccion_dificultad == "DIFÍCIL":
            if nro_preg == 0:
                pregunta = [
                    "¿Cuántas veces ha ganado Argentina la Copa Mundial de Fútbol?",
                    "Dos",
                    "Tres",
                    "Cuatro",
                    "Una",
                    2,
                ]
            elif nro_preg == 1:
                pregunta = [
                    "¿Cuál fue el primer club de fútbol fundado en Argentina?",
                    "Rivel Plate",
                    "Boca Juniors",
                    "Quilmes",
                    "Rosario Central",
                    3,
                ]
            elif nro_preg == 2:
                pregunta = [
                    "¿En qué año se retiró Diego Maradona del fútbol profesional?",
                    "1994",
                    "1997",
                    "2000",
                    "2002",
                    2,
                ]
            elif nro_preg == 3:
                pregunta = [
                    "¿Quién es el tenista argentino con más títulos de Grand Slam?",
                    "David Nalbandian",
                    "Gastón Gaudio",
                    "Guillermo Vilas",
                    "Juan Martín del Potro",
                    3,
                ]
            elif nro_preg == 4:
                pregunta = [
                    "¿Qué equipo de fútbol argentino tiene más títulos de la Copa Libertadores?",
                    "Boca Juniors",
                    "River Plate",
                    "Independiente",
                    "Estudiantes de La Plata",
                    3,
                ]
            elif nro_preg == 5:
                pregunta = [
                    "¿Cómo se llama el clásico entre Boca Juniors y River Plate?",
                    "El Clásico",
                    "THE BIG ONE",
                    "El Superclásico",
                    "El Gran Partido",
                    3,
                ]
            elif nro_preg == 6:
                pregunta = [
                    "¿Quién es considerado uno de los mejores jugadores de baloncesto en la historia de Argentina?",
                    "Fabricio Oberto",
                    "Andrés Nocioni",
                    "Luis Scola",
                    "Emanuel Ginóbili",
                    4,
                ]
            elif nro_preg == 7:
                pregunta = [
                    "¿En qué año ganó Argentina la medalla de oro en baloncesto en los Juegos Olímpicos?",
                    "1996",
                    "2000",
                    "2004",
                    "2008",
                    3,
                ]
            elif nro_preg == 8:
                pregunta = [
                    "¿¿Cuál fue el primer equipo argentino en ganar la Copa Libertadores?",
                    "Racing Club",
                    "Estudiantes de La Plata",
                    "Boca Juniors",
                    "Independiente",
                    2,
                ]
            else:
                pregunta = [
                    "¿Quién fue la primera mujer argentina en ganar una medalla olímpica?",
                    "Jeanette Campbell",
                    "Gabriela Sabatini",
                    "Ninguna es correcta",
                    "Paula Pareto",
                    1,
                ]
        # nivel avanzado
        else:
            if nro_preg == 0:
                pregunta = [
                    "¿Cuál es el récord de goles de Lionel Messi en una sola temporada de La Liga?",
                    "50",
                    "46",
                    "54",
                    "48",
                    1,
                ]
            elif nro_preg == 1:
                pregunta = [
                    "¿Qué futbolista argentino ha jugado en más mundiales",
                    "Diego Maradona",
                    "Javier Mascherano",
                    "Lionel Messi",
                    "Gabriel Batistuta",
                    2,
                ]
            elif nro_preg == 2:
                pregunta = [
                    "¿Cuántos títulos de ATP ha ganado Juan Martín del Potro?",
                    "18",
                    "22",
                    "25",
                    "20",
                    3,
                ]
            elif nro_preg == 3:
                pregunta = [
                    "¿En qué equipo debutó profesionalmente Juan Román Riquelme?",
                    "River Plate",
                    "Argentinos Juniors",
                    "Boca Juniors",
                    "Barcelona",
                    2,
                ]
            elif nro_preg == 4:
                pregunta = [
                    "¿Qué atleta argentina se convirtió en la primera mujer en ganar una medalla de oro en un Mundial de Atletismo?",
                    "Jennifer Dahlgren",
                    "Victoria Woodward",
                    "María Luz Tesuri",
                    "Noelia Martínez",
                    4,
                ]
            elif nro_preg == 5:
                pregunta = [
                    "¿Cuántos puntos anotó Emanuel Ginóbili en su carrera en la NBA?",
                    "10,496",
                    "14,043",
                    "13,001",
                    "12,572",
                    2,
                ]
            elif nro_preg == 6:
                pregunta = [
                    "¿Qué jugador argentino es conocido como 'El Príncipe' en el fútbol europeo?",
                    "Juan Sebastián Verón",
                    "Enzo Francescoli",
                    "Gabriel Batistuta",
                    "Hernán Crespo",
                    2,
                ]
            elif nro_preg == 7:
                pregunta = [
                    "¿Cuál es el récord de victorias consecutivas del equipo de rugby Los Pumas?",
                    "8",
                    "11",
                    "12",
                    "14",
                    3,
                ]
            elif nro_preg == 8:
                pregunta = [
                    "¿En qué equipo de la NBA jugó Luis Scola durante más temporadas?",
                    "Phoenix Suns",
                    "Indiana Pacers",
                    "Houston Rockets",
                    "Brooklyn Nets",
                    3,
                ]
            else:
                pregunta = [
                    "¿Qué logro deportivo alcanzó Delfina Merino en el año 2017?",
                    "Ganó el oro olímpico",
                    "Fue nombrada mejor jugadora de la Copa del Mundo",
                    "Se retiró del hockey",
                    "Fue elegida mejor jugadora del mundo por la FIH",
                    4,
                ]
    elif categoria == "CIENCIA":
        if eleccion_dificultad == "BÁSICO":
            if nro_preg == 0:
                pregunta = [
                    "¿Quién fue el primer científico argentino en recibir el Premio Nobel de Medicina?",
                    "Bernardo Houssay",
                    "Luis Federico Leloir",
                    "César Milstein",
                    "Juan Carlos Fasciolo",
                    1,
                ]

            elif nro_preg == 1:
                pregunta = [
                    "¿Qué institución argentina es reconocida por su contribución a la investigación científica y tecnológica, y fue fundada en 1958?",
                    "INTA (Instituto Nacional de Tecnología Agropecuaria)",
                    "INTI (Instituto Nacional de Tecnología Industrial)",
                    "CONICET (Consejo Nacional de Investigaciones Científicas y Técnicas)",
                    "CITEDEF (Instituto de Investigaciones Científicas y Técnicas de las Fuerzas Armadas)",
                    3,
                ]
            elif nro_preg == 2:
                pregunta = [
                    "¿Cuál es el nombre del centro de investigación dedicado a la física y la biología molecular, ubicado en Bariloche?",
                    "CITEDEF",
                    "INTA",
                    "Instituto Balseiro",
                    "Fundación Favaloro",
                    3,
                ]
            elif nro_preg == 3:
                pregunta = [
                    "¿Qué científico argentino es conocido por desarrollar la técnica del bypass coronario?",
                    "René Favaloro",
                    "Bernardo Houssay",
                    "Luis Federico Leloir",
                    "Salvador Mazza",
                    1,
                ]

            elif nro_preg == 4:
                pregunta = [
                    "¿Cuál es el objetivo principal del Banco Nacional de Datos Genéticos?",
                    "Conservar el ADN de los ciudadanos argentinos",
                    "Facilitar la identificación de personas desaparecidas durante la dictadura militar",
                    "Realizar estudios genéticos sobre enfermedades hereditarias",
                    "Proveer datos genéticos para investigaciones científicas",
                    2,
                ]

            elif nro_preg == 5:
                pregunta = [
                    "¿Qué programa del gobierno argentino promueve la formación de programadores y fue lanzado en 2020?",
                    "Plan 111 Mil",
                    "Argentina Programa",
                    "Plan Conectar Igualdad",
                    "Plan Sumar",
                    2,
                ]

            elif nro_preg == 6:
                pregunta = [
                    "¿Qué empresa tecnológica argentina es famosa por su enfoque en la transformación digital y servicios de software?",
                    "Auth0",
                    "Trello",
                    "Globant",
                    "Despegar",
                    3,
                ]
            elif nro_preg == 7:
                pregunta = [
                    "¿Qué ingeniero argentino inventó el bolígrafo, también conocido como birome, junto con su hermano?",
                    "Ladislao Biro",
                    "Juan Vucetich",
                    "Ramón Carrillo",
                    "Quirino Cristiani",
                    1,
                ]

            elif nro_preg == 8:
                pregunta = [
                    "¿Qué importante logro científico del CONICET fue reconocido internacionalmente en el campo de la paleontología?",
                    "Desarrollo de vacunas para enfermedades tropicales",
                    "Creación del primer satélite argentino",
                    "Estudios sobre cambio climático en la Antártida",
                    "Descubrimiento de nuevas especies de dinosaurios en la Patagonia",
                    4,
                ]

            else:
                pregunta = [
                    "¿Qué tipo de investigaciones financia el CONICET?",
                    "Ciencias Exactas y Naturales",
                    "Ciencias Sociales y Humanidades",
                    "Ciencias Médicas y de la Salud",
                    "Todas las anteriores",
                    4,
                ]

        elif eleccion_dificultad == "DIFICIL":
            if nro_preg == 0:
                pregunta = [
                    "¿Qué físico argentino fue co-descubridor de los agujeros negros de masa intermedia y es conocido por su trabajo en el LIGO (Observatorio de Ondas Gravitacionales por Interferometría Láser)?",
                    "Juan Martín Maldacena",
                    "Mario Bunge",
                    "Alberto Rojo",
                    "Gabriela González",
                    4,
                ]

            elif nro_preg == 1:
                pregunta = [
                    "¿Qué presidente argentino creó el CONICET?",
                    "Juan Domingo Perón",
                    "Raúl Alfonsín",
                    "Arturo Frondizi",
                    "Néstor Kirchner",
                    3,
                ]

            elif nro_preg == 2:
                pregunta = [
                    "¿Qué científico argentino es conocido por su trabajo pionero en el campo de la neurociencia y la plasticidad cerebral?",
                    "René Favaloro",
                    "Fernando Nottebohm",
                    "Rita Levi-Montalcini",
                    "Facundo Manes",
                    2,
                ]

            elif nro_preg == 3:
                pregunta = [
                    "¿Cuál fue el primer satélite argentino lanzado al espacio?",
                    "SAC-B",
                    "SAC-A",
                    "ARSAT-1",
                    "Nahuel 1A",
                    3,
                ]

            elif nro_preg == 4:
                pregunta = [
                    "¿Qué agencia espacial argentina es responsable del desarrollo y lanzamiento de satélites?",
                    "CONAE",
                    "INVAP",
                    "INTA",
                    "CONICET",
                    1,
                ]

            elif nro_preg == 5:
                pregunta = [
                    "¿Qué programa del gobierno argentino promueve la formación de programadores y fue lanzado en 2020?",
                    "Plan 111 Mil",
                    "Plan Conectar Igualdad",
                    "Argentina Programa",
                    "Plan Sumar",
                    3,
                ]

            elif nro_preg == 6:
                pregunta = [
                    "¿Qué proyecto de código abierto argentino es conocido por ser una solución integral de ERP (Enterprise Resource Planning) y CRM (Customer Relationship Management)?",
                    "OpenBravo",
                    "Dolibarr",
                    "Odoo",
                    "Tryton",
                    1,
                ]

            elif nro_preg == 7:
                pregunta = [
                    "¿Qué ley, aprobada en 2001, establece el marco para la promoción y financiamiento de la ciencia, tecnología e innovación en Argentina?",
                    "Ley de Promoción de la Ciencia y la Tecnología",
                    "Ley de Innovación Tecnológica",
                    "Ley de Financiamiento Educativo",
                    "Ley de Educación Nacional",
                    2,
                ]

            elif nro_preg == 8:
                pregunta = [
                    "¿En qué año se creó el Ministerio de Ciencia, Tecnología e Innovación Productiva en Argentina?",
                    "2001",
                    "2012",
                    "2007",
                    "2015",
                    3,
                ]

            else:
                pregunta = [
                    "¿Cuál fue un hallazgo destacado en la historia argentina a través del estudio de la antropología forense?",
                    "La identificación de restos fósiles de dinosaurios",
                    "La identificación de víctimas de la dictadura militar",
                    "La reconstrucción de la dieta de las poblaciones prehistóricas",
                    "La datación de artefactos arqueológicos precolombinos",
                    2,
                ]

        else:
            if nro_preg == 0:
                pregunta = [
                    "¿Qué técnica genética ha sido fundamental en la labor del BNDG para la identificación de nietos apropiados?",
                    "Secuenciación de nueva generación (NGS)",
                    "Análisis de microsatélites (STR)",
                    "Electroforesis en gel",
                    "Southern blot",
                    2,
                ]

            elif nro_preg == 1:
                pregunta = [
                    "¿Qué investigadora argentina en el campo de la biotecnología fue pionera en el desarrollo de bioproductos y es cofundadora de la empresa Bioceres?",
                    "Silvia Gold",
                    "Gabriela Aguirre",
                    "Andrea Gamarnik",
                    "Norma Sánchez",
                    1,
                ]

            elif nro_preg == 2:
                pregunta = [
                    "¿Qué ingeniero argentino desarrolló la primer computadora en América Latina, conocida como Clementina?",
                    "Enrique Gaviola",
                    "Juan Maldacena",
                    "Manuel Sadosky",
                    "Luis von Ahn",
                    3,
                ]

            elif nro_preg == 3:
                pregunta = [
                    "¿Quién fue la primera física argentina en recibir el Premio Nobel en Física?",
                    "Cecilia Grierson",
                    "Marta Lynch",
                    "Luisa Vehil",
                    "María Florentina Gómez Miranda",
                    4,
                ]

            elif nro_preg == 4:
                pregunta = [
                    "¿Qué inventor argentino es conocido por desarrollar la primera máquina para realizar transfusiones de sangre con la técnica de citrato?",
                    "Luis Agote",
                    "Luis Federico Leloir",
                    "René Favaloro",
                    "Bernardo Houssay",
                    1,
                ]

            elif nro_preg == 5:
                pregunta = [
                    "¿Qué proyecto argentino de software libre está destinado a la gestión integral de bibliotecas y es utilizado en varios países de América Latina?",
                    "Koha",
                    "ABCD",
                    "Biblio",
                    "OpenBravo",
                    2,
                ]

            elif nro_preg == 6:
                pregunta = [
                    "¿Qué iniciativa del gobierno argentino tiene como objetivo financiar la investigación en áreas estratégicas y emergentes?",
                    "PROFIET",
                    "FONPLATA",
                    "FONARSEC",
                    "PICTO",
                    3,
                ]

            elif nro_preg == 7:
                pregunta = [
                    "¿Qué estudio sociológico argentino investigó las migraciones internas y la urbanización del país en el siglo XX?",
                    "Informe PISA",
                    "Encuesta Permanente de Hogares (EPH)",
                    "Encuesta Nacional de Hogares (ENH)",
                    "Estudio Di Tella",
                    4,
                ]

            elif nro_preg == 8:
                pregunta = [
                    "¿Qué descubrimiento en arqueología argentina reveló importantes vestigios de la cultura inca en el noroeste del país?",
                    "Ruinas de Shincal de Quimivil",
                    "Ruinas de Quilmes",
                    "Ruinas de Tafi",
                    "Ruinas de Humahuaca",
                    1,
                ]

            else:
                pregunta = [
                    "¿Cuál fue el campo de estudio de la científica argentina Carolina Trossero, reconocida con el Premio Nobel en 2009?",
                    "Matemáticas",
                    "Biología molecular",
                    "Física",
                    "Química",
                    1,
                ]

    elif categoria == "ARTE":
        # nivel basico
        if eleccion_dificultad == "BÁSICO":
            if nro_preg == 0:
                pregunta = [
                    "¿Quién es considerado el padre del tango?",
                    "Carlos Gardel",
                    "Astor Piazzolla",
                    "Aníbal Troilo",
                    "Carlos Di Sarli",
                    1,
                ]
            elif nro_preg == 1:
                pregunta = [
                    "¿Cuál de estos artistas argentinos es conocido por sus pinturas surrealistas?",
                    "Antonio Berni",
                    "Xul Solar",
                    "Benito Quinquela Martín",
                    "Emilio Pettoruti",
                    2,
                ]
            elif nro_preg == 2:
                pregunta = [
                    "¿Quién fue el arquitecto argentino que diseñó el Obelisco de Buenos Aires?",
                    "Francisco Salamone",
                    "Alejandro Bustillo",
                    "César Pelli",
                    "Alberto Prebisch",
                    4,
                ]
            elif nro_preg == 3:
                pregunta = [
                    "¿Qué escultor argentino creó la obra 'El pensador'?",
                    "Erminio Blotta",
                    "Lola Mora",
                    "Lucio Fontana",
                    "Auguste Rodin",
                    1,
                ]
            elif nro_preg == 4:
                pregunta = [
                    "¿En qué museo se encuentra expuesta la famosa pintura 'El Grito' de Edvard Munch?",
                    "MALBA",
                    "Museo Nacional de Bellas Artes",
                    "Museo de Arte Moderno de Buenos Aires",
                    "Museo de Arte Contemporáneo de Rosario",
                    2,
                ]
            elif nro_preg == 5:
                pregunta = [
                    "¿Qué escritor argentino escribió la novela 'Rayuela'?",
                    "Jorge Luis Borges",
                    "Julio Cortázar",
                    "Adolfo Bioy Casares",
                    "Ernesto Sabato",
                    2,
                ]
            elif nro_preg == 6:
                pregunta = [
                    "¿Qué famoso muralista argentino pintó el fresco 'Ejercicio Plástico'?",
                    "David Alfaro Siqueiros",
                    "Diego Rivera",
                    "José Clemente Orozco",
                    "Antonio Berni",
                    4,
                ]
            elif nro_preg == 7:
                pregunta = [
                    "¿Cuál de estos artistas argentinos es conocido por su obra 'La Catedral'?",
                    "Antonio Berni",
                    "Xul Solar",
                    "Benito Quinquela Martín",
                    "Emilio Pettoruti",
                    3,
                ]
            elif nro_preg == 8:
                pregunta = [
                    "¿Qué famoso músico argentino es conocido por su obra 'Adiós Nonino'?",
                    "Astor Piazzolla",
                    "Carlos Gardel",
                    "Aníbal Troilo",
                    "Osvaldo Pugliese",
                    1,
                ]
            else:
                pregunta = [
                    "¿Cuál es la danza tradicional argentina conocida por su origen en la provincia de La Rioja?",
                    "Chacarera",
                    "Zamba",
                    "Cueca",
                    "Gato",
                    4,
                ]
        # nivel intermedio
        elif eleccion_dificultad == "DIFICIL":
            if nro_preg == 0:
                pregunta = [
                    "¿Qué reconocido arquitecto argentino diseñó el Teatro Colón de Buenos Aires?",
                    "Alejandro Bustillo",
                    "César Pelli",
                    "Alberto Prebisch",
                    "Francisco Salamone",
                    3,
                ]
            elif nro_preg == 1:
                pregunta = [
                    "¿Cuál es el nombre del museo de arte contemporáneo ubicado en la Ciudad de Buenos Aires?",
                    "MALBA",
                    "Museo Nacional de Bellas Artes",
                    "Museo de Arte Moderno de Buenos Aires",
                    "Museo de Arte Contemporáneo de Rosario",
                    1,
                ]
            elif nro_preg == 2:
                pregunta = [
                    "¿Qué pintor argentino es conocido por su obra 'Contra el quebracho'?",
                    "Antonio Berni",
                    "Xul Solar",
                    "Benito Quinquela Martín",
                    "Emilio Pettoruti",
                    1,
                ]
            elif nro_preg == 3:
                pregunta = [
                    "¿Quién fue el primer director de la Orquesta Filarmónica de Buenos Aires?",
                    "Astor Piazzolla",
                    "Carlos Gardel",
                    "Aníbal Troilo",
                    "Alberto Ginastera",
                    4,
                ]
            elif nro_preg == 4:
                pregunta = [
                    "¿Qué famoso escultor argentino es conocido por sus obras monumentales en hormigón armado?",
                    "Erminio Blotta",
                    "Lola Mora",
                    "Lucio Fontana",
                    "Pablo Curatella Manes",
                    4,
                ]
            elif nro_preg == 5:
                pregunta = [
                    "¿Qué escritor argentino es conocido por su obra 'Sobre héroes y tumbas'?",
                    "Jorge Luis Borges",
                    "Julio Cortázar",
                    "Adolfo Bioy Casares",
                    "Ernesto Sabato",
                    4,
                ]
            elif nro_preg == 6:
                pregunta = [
                    "¿Cuál de estos artistas argentinos es conocido por su obra 'El Jugador de Ajedrez'?",
                    "Antonio Berni",
                    "Xul Solar",
                    "Benito Quinquela Martín",
                    "Emilio Pettoruti",
                    2,
                ]
            elif nro_preg == 7:
                pregunta = [
                    "¿Qué escultor argentino creó la obra 'Monumento a la Bandera' en Rosario?",
                    "Erminio Blotta",
                    "Lola Mora",
                    "Lucio Fontana",
                    "Pablo Curatella Manes",
                    2,
                ]
            elif nro_preg == 8:
                pregunta = [
                    "¿Qué famoso muralista argentino pintó el fresco 'La Tortura'?",
                    "David Alfaro Siqueiros",
                    "Diego Rivera",
                    "José Clemente Orozco",
                    "Antonio Berni",
                    1,
                ]
            else:
                pregunta = [
                    "¿Cuál de estos artistas argentinos es conocido por su obra 'Lavanderas'?",
                    "Antonio Berni",
                    "Xul Solar",
                    "Benito Quinquela Martín",
                    "Emilio Pettoruti",
                    3,
                ]
        # nivel avanzado
        else:
            if nro_preg == 0:
                pregunta = [
                    "¿Qué reconocido pintor argentino es conocido por su obra 'La Furia'?",
                    "Antonio Berni",
                    "Xul Solar",
                    "Benito Quinquela Martín",
                    "Emilio Pettoruti",
                    1,
                ]
            elif nro_preg == 1:
                pregunta = [
                    "¿Cuál de estos artistas argentinos es conocido por su obra 'Cantos Rodados'?",
                    "Antonio Berni",
                    "Xul Solar",
                    "Benito Quinquela Martín",
                    "Emilio Pettoruti",
                    2,
                ]
            elif nro_preg == 2:
                pregunta = [
                    "¿Cuál de estos artistas argentinos es conocido por su obra 'La ventana'?",
                    "Antonio Berni",
                    "Xul Solar",
                    "Benito Quinquela Martín",
                    "Emilio Pettoruti",
                    3,
                ]
            elif nro_preg == 3:
                pregunta = [
                    "¿Qué famoso pintor argentino es conocido por su obra 'El desfile'?",
                    "Antonio Berni",
                    "Xul Solar",
                    "Benito Quinquela Martín",
                    "Emilio Pettoruti",
                    4,
                ]
            elif nro_preg == 4:
                pregunta = [
                    "¿Qué reconocido músico argentino es conocido por su obra 'Milonga del Ángel'?",
                    "Astor Piazzolla",
                    "Carlos Gardel",
                    "Aníbal Troilo",
                    "Osvaldo Pugliese",
                    1,
                ]
            elif nro_preg == 5:
                pregunta = [
                    "¿Cuál de estos artistas argentinos es conocido por su obra 'Calle de Barracas'?",
                    "Antonio Berni",
                    "Xul Solar",
                    "Benito Quinquela Martín",
                    "Emilio Pettoruti",
                    2,
                ]
            elif nro_preg == 6:
                pregunta = [
                    "¿Quién fue el escritor argentino ganador del Premio Nobel de Literatura en 2010?",
                    "Jorge Luis Borges",
                    "Julio Cortázar",
                    "Adolfo Bioy Casares",
                    "Mario Vargas Llosa",
                    4,
                ]
            elif nro_preg == 7:
                pregunta = [
                    "¿Qué famoso pianista argentino es conocido por su interpretación de 'El Concierto de Aranjuez'?",
                    "Astor Piazzolla",
                    "Martha Argerich",
                    "Raúl Di Blasio",
                    "Osvaldo Pugliese",
                    2,
                ]
            elif nro_preg == 8:
                pregunta = [
                    "¿Cuál de estos artistas argentinos es conocido por su obra 'El solterito'?",
                    "Antonio Berni",
                    "Xul Solar",
                    "Benito Quinquela Martín",
                    "Emilio Pettoruti",
                    3,
                ]
            else:
                pregunta = [
                    "¿Qué reconocido poeta argentino escribió 'El Aleph'?",
                    "Jorge Luis Borges",
                    "Julio Cortázar",
                    "Adolfo Bioy Casares",
                    "Ernesto Sabato",
                    1,
                ]
    elif categoria == "GEOGRAFIA":
        # basico
        if eleccion_dificultad == "BÁSICO":
            if nro_preg == 0:
                pregunta = [
                    "¿Cuál es la montaña más alta de Argentina?",
                    "Aconcagua",
                    "Fitz Roy",
                    "Cerro Torre",
                    "Chapelco",
                    1,
                ]
            elif nro_preg == 1:
                pregunta = [
                    "¿Cuál es el río más largo de Argentina?",
                    "Correntoso",
                    "Paraná",
                    "Caleufú",
                    "Paraguay",
                    2,
                ]
            elif nro_preg == 2:
                pregunta = [
                    "¿Qué famoso glaciar se encuentra en el Parque Nacional Los Glaciares?",
                    "No existe",
                    "Glaciar Martial",
                    "Glaciar Perito Moreno",
                    "Glaciar Upsala",
                    3,
                ]
            elif nro_preg == 3:
                pregunta = [
                    "¿En qué región de Argentina se encuentra la famosa Patagonia?",
                    "Norte",
                    "Centro",
                    "Sur",
                    "Oeste",
                    3,
                ]
            elif nro_preg == 4:
                pregunta = [
                    "¿Cuál es la capital de Argentina?",
                    "Neuquén",
                    "Buenos Aires",
                    "Córdoba",
                    "Rosario",
                    2,
                ]
            elif nro_preg == 5:
                pregunta = [
                    "¿Qué océano baña las costas de Argentina?",
                    "Ártico",
                    "Pacífico",
                    "Índico",
                    "Atlántico",
                    4,
                ]
            elif nro_preg == 6:
                pregunta = [
                    "¿Cuál es el apodo de Salta?",
                    "La Bella",
                    "La Grande",
                    "La Linda",
                    "La Colorida",
                    1,
                ]
            elif nro_preg == 7:
                pregunta = [
                    "¿En qué región de Argentina se encuentra la famosa región vinícola de Mendoza?",
                    "Oeste",
                    "Noroeste",
                    "Cuyo",
                    "Patagonia",
                    2,
                ]
            elif nro_preg == 8:
                pregunta = [
                    "¿Cuál es el nombre de las famosas cataratas en la provincia de Misiones?",
                    "Garganta del Diablo",
                    "Cataratas del Iguazú",
                    "Cataratas del Salto",
                    "Cataratas del Paraná",
                    2,
                ]
            else:
                pregunta = [
                    "¿Qué famosa formación rocosa se encuentra en la provincia de Salta?",
                    "Cerro Chaltén",
                    "Cerro de los Siete Colores",
                    "Cerro Catedral",
                    "Cerro Colorido",
                    2,
                ]
        # dificil
        elif eleccion_dificultad == "DIFICIL":
            if nro_preg == 0:
                pregunta = [
                    "¿Cuál de las siguientes provincias argentinas no tiene costa?",
                    "Buenos Aires",
                    "Santa Fe",
                    "Mendoza",
                    "Misiones",
                    3,
                ]
            elif nro_preg == 1:
                pregunta = [
                    "¿En qué provincia se encuentra el Cerro Aconcagua?",
                    "Mendoza",
                    "Neuquén",
                    "Santa Cruz",
                    "Río Negro",
                    1,
                ]
            elif nro_preg == 2:
                pregunta = [
                    "¿Cuál de estos lagos no se encuentra en la provincia de Neuquén?",
                    "Lago Nahuel Huapi",
                    "Lago Argentino",
                    "Lago Traful",
                    "Lago Hermoso",
                    2,
                ]
            elif nro_preg == 3:
                pregunta = [
                    "¿Cuál es el nombre de la península ubicada en la provincia de Chubut, famosa por avistamiento de ballenas?",
                    "Península Valdés",
                    "Península Mitre",
                    "Península San José",
                    "Península Ballenas",
                    1,
                ]
            elif nro_preg == 4:
                pregunta = [
                    "¿Cuál es el nombre de la región montañosa ubicada en la provincia de San Juan?",
                    "Cordillera de los Andes",
                    "Cordillera de los Vientos",
                    "Cordillera de la Costa",
                    "Cordilleta de los Alcones",
                    2,
                ]
            elif nro_preg == 5:
                pregunta = [
                    "¿Cuál de las siguientes provincias limita con Bolivia?",
                    "Jujuy",
                    "Salta",
                    "Corrientes",
                    "La Pampa",
                    2,
                ]
            elif nro_preg == 6:
                pregunta = [
                    "¿Qué famosa formación natural se encuentra en la provincia de La Rioja y es un importante destino turístico?",
                    "Valle de la Luna",
                    "Quebrada de Humahuaca",
                    "Cueva de las Manos",
                    "Cueva de las aves",
                    1,
                ]
            elif nro_preg == 7:
                pregunta = [
                    "¿Qué provincia argentina se caracteriza por tener una importante producción de petróleo?",
                    "Neuquén",
                    "Córdoba",
                    "Entre Ríos",
                    "Santiago del Estero",
                    1,
                ]
            elif nro_preg == 8:
                pregunta = [
                    "¿Cuál es el nombre del pico más alto de la provincia de Tierra del Fuego?",
                    "Cerro Fitz Roy",
                    "Cerro Torre",
                    "Monte Olivia",
                    "Monte Tronador",
                    3,
                ]
            else:
                pregunta = [
                    "¿Qué río forma parte de la frontera entre Argentina y Uruguay?",
                    "Río Paraná",
                    "Río Uruguay",
                    "Río Iguazú",
                    "Rió Salado",
                    2,
                ]
        # avanzado
        else:
            if nro_preg == 0:
                pregunta = [
                    "¿Cuál es el nombre de la región semiárida ubicada en la provincia de Buenos Aires?",
                    "Pampa Húmeda",
                    "Chaco Austral",
                    "Monte",
                    "Pampa Seca",
                    3,
                ]
            elif nro_preg == 1:
                pregunta = [
                    "¿Qué provincia argentina es conocida por su producción de vino Malbec?",
                    "Mendoza",
                    "San Juan",
                    "La Rioja",
                    "Salta",
                    1,
                ]
            elif nro_preg == 2:
                pregunta = [
                    "¿Cuál es el nombre del volcán más alto de Argentina?",
                    "Lanín",
                    "Copahue",
                    "Ojos del Salado",
                    "Tronador",
                    3,
                ]
            elif nro_preg == 3:
                pregunta = [
                    "¿Qué parque nacional argentino es conocido por ser el hogar de una gran variedad de especies de aves?",
                    "Parque Nacional Los Glaciares",
                    "Parque Nacional Nahuel Huapi",
                    "Parque Nacional Iguazú",
                    "Parque Nacional El Palmar",
                    2,
                ]
            elif nro_preg == 4:
                pregunta = [
                    "¿Cuál de las siguientes provincias no tiene frontera con Chile?",
                    "Neuquén",
                    "Mendoza",
                    "Chaco",
                    "Formosa",
                    3,
                ]
            elif nro_preg == 5:
                pregunta = [
                    "¿Qué provincia argentina es famosa por su producción de yerba mate?",
                    "Corrientes",
                    "Misiones",
                    "Formosa",
                    "Entre Ríos",
                    2,
                ]
            elif nro_preg == 6:
                pregunta = [
                    "¿Cuál es el nombre del río más ancho de Argentina?",
                    "Río Paraná",
                    "Río de la Plata",
                    "Río Uruguay",
                    "Río Colorado",
                    2,
                ]
            elif nro_preg == 7:
                pregunta = [
                    "¿Qué provincia argentina es famosa por sus formaciones geológicas y cañones multicolores?",
                    "Jujuy",
                    "La Rioja",
                    "San Juan",
                    "Salta",
                    1,
                ]
            elif nro_preg == 8:
                pregunta = [
                    "¿Qué cordillera atraviesa la provincia de Mendoza?",
                    "Cordillera de los Andes",
                    "Cordillera de la Costa",
                    "Cordillera de los Vientos",
                    "Cordillera del Tigre",
                    1,
                ]
            else:
                pregunta = [
                    "¿Qué provincia argentina limita con Paraguay y Brasil?",
                    "Buenos Aires",
                    "Entre Ríos",
                    "Formosa",
                    "Corrientes",
                    4,
                ]
    else:
        # entretenimiento
        # nivel basico
        if eleccion_dificultad == "BÁSICO":
            if nro_preg == 0:
                pregunta = [
                    "¿Qué famosa modelo y conductora argentina fue noticia en 2020 por su divorcio con el futbolista Mauro Icardi?",
                    "Zaira Nara",
                    "Nicole Neumann",
                    "Wanda Nara",
                    "Paula Chaves",
                    3,
                ]
            elif nro_preg == 1:
                pregunta = [
                    "¿Qué conductor de televisión argentino fue muy criticado en 2019 por sus comentarios misóginos durante su programa en vivo?",
                    "Jorge Rial",
                    "Marcelo Tinelli",
                    "Alejandro Fantino",
                    "Santiago del Moro",
                    1,
                ]

            elif nro_preg == 2:
                pregunta = [
                    "¿Qué pareja de la farándula argentina se separó en 2018 tras más de 10 años juntos, generando una gran cobertura mediática?",
                    "Pedro Alfonso y Paula Chaves",
                    "Mariano Martínez y Lali Espósito",
                    "Nicolás Cabré y Eugenia Suárez",
                    "Pampita y Benjamin Vicuña",
                    4,
                ]

            elif nro_preg == 3:
                pregunta = [
                    "¿Cuál es la famosa frase de Moria Casán que utiliza para referirse a las personas que la critican?",
                    "¿Qué te pasa, Clarín?",
                    "Si querés llorar, llorá",
                    "Si querés, seguime, y si no, te bloqueo",
                    "¿Algún problema? ¡Arreglate!",
                    2,
                ]

            elif nro_preg == 4:
                pregunta = [
                    "¿Qué serie argentina disponible en Netflix se centra en la historia de un fiscal y un pastor en un contexto de corrupción política?",
                    "El Recluso",
                    "El Reino",
                    "Apache: La vida de Carlos Tevez",
                    "Estocolmo",
                    2,
                ]

            elif nro_preg == 5:
                pregunta = [
                    "¿Cuál es el nombre de la productora de televisión fundada por Marcelo Tinelli?",
                    "Pol-Ka",
                    "Underground Producciones",
                    "Ideas del Sur",
                    "Endemol Argentina",
                    3,
                ]

            elif nro_preg == 6:
                pregunta = [
                    "¿Qué humorista argentino era conocido por su personaje 'Pepe Argento' en 'Casados con Hijos'?",
                    "Guillermo Francella",
                    "Adrián Suar",
                    "Diego Peretti",
                    "Ricardo Darín",
                    1,
                ]

            elif nro_preg == 7:
                pregunta = [
                    "¿Cuál de estos programas de televisión argentinos fue conducido por Mario Pergolini?",
                    "Caiga Quien Caiga",
                    "Susana Giménez",
                    "Almorzando con Mirtha Legrand",
                    "VideoMatch",
                    1,
                ]

            elif nro_preg == 8:
                pregunta = [
                    "¿Qué futbolista argentino se casó con Antonela Roccuzzo en 2017?",
                    "Sergio Agüero",
                    "Lionel Messi",
                    "Paulo Dybala",
                    "Gonzalo Higuaín",
                    2,
                ]
            else:
                pregunta = [
                    "¿Qué famoso humorista es conocido por ser fanático de Boca Juniors?",
                    "Migue Granados",
                    "Diego Korol",
                    "Larry De Clay",
                    "Jose Maria Listorti",
                    3,
                ]
        # nivel dificil
        elif eleccion_dificultad == "DIFICL":
            if nro_preg == 0:
                pregunta = [
                    "¿En qué situación Moria Casán dijo la frase 'No me vas a correr con la vaina'?",
                    "Durante una pelea con Susana Giménez",
                    "Durante una discusión con Graciela Alfano",
                    "En una entrevista con Jorge Rial",
                    "En una gala del 'Bailando por un Sueño'",
                    2,
                ]

            elif nro_preg == 1:
                pregunta = [
                    "¿Cuál fue la primera serie original de Netflix producida en Argentina?",
                    "El Marginal",
                    "Apache: La vida de Carlos Tevez",
                    "Puerta 7",
                    "Go! Vive a tu manera",
                    4,
                ]

            elif nro_preg == 2:
                pregunta = [
                    "¿En qué plataforma de streaming se puede ver la serie argentina 'Monzón: La Serie', basada en la vida del boxeador Carlos Monzón?",
                    "Amazon Prime Video",
                    "Netflix",
                    "Hulu",
                    "Disney+",
                    1,
                ]

            elif nro_preg == 3:
                pregunta = [
                    "¿Cuál fue la causa principal del conflicto entre Marcelo Tinelli y el grupo Clarín en 2013?",
                    "La cancelación de su programa",
                    "La venta de Ideas del Sur",
                    "Disputas por derechos de transmisión",
                    "Críticas a la línea editorial del grupo",
                    2,
                ]

            elif nro_preg == 4:
                pregunta = [
                    "¿Qué programa de televisión argentino popularizó la frase '¡Y pegue, y pegue!'?",
                    "Showmatch",
                    "Polémica en el Bar",
                    "VideoMatch",
                    "Grande Pa!",
                    3,
                ]

            elif nro_preg == 5:
                pregunta = [
                    "¿Qué conductor de televisión argentino es conocido por haberle realizado una autopsia a un extraterrestre?",
                    "Alejandro Fantino",
                    "Samuel 'Chiche' Gelblung",
                    "Jorge Lanata",
                    "Beto Casella",
                    2,
                ]

            elif nro_preg == 6:
                pregunta = [
                    "¿Quién es la famosa vedette argentina conocida como 'La One'?",
                    "Moria Casán",
                    "Susana Giménez",
                    "Graciela Alfano",
                    "Carmen Barbieri",
                    1,
                ]

            elif nro_preg == 7:
                pregunta = [
                    "¿Qué futbolista argentino protagonizó un escándalo en 2017 al ser expulsado de un partido y mostrar el cu** a los espectadores?",
                    "Sergio Agüero",
                    "Gonzalo Higuaín",
                    "Carlos Tevez",
                    "Ezequiel Lavezzi",
                    4,
                ]

            elif nro_preg == 8:
                pregunta = [
                    "¿Cuál es el nombre del personaje interpretado por Federico D'Elía en 'Los Simuladores'?",
                    "Mario Santos",
                    "Gabriel Medina",
                    "Emilio Ravenna",
                    "Pablo Lamponne",
                    1,
                ]

            else:
                pregunta = [
                    "¿Qué tipo de cliente acude al equipo de Los Simuladores en cada episodio?",
                    "Alguien en busca de venganza",
                    "Alguien con un problema difícil de resolver",
                    "Alguien que necesita planificar un robo",
                    "Alguien que quiere iniciar un negocio",
                    2,
                ]

        # nivel experto
        else:
            if nro_preg == 0:
                pregunta = [
                    "¿Qué actor argentino protagoniza la serie 'El Jardín de Bronce', disponible en HBO Max?",
                    "Joaquín Furriel",
                    "Diego Peretti",
                    "Ricardo Darín",
                    "Leonardo Sbaraglia",
                    1,
                ]

            elif nro_preg == 1:
                pregunta = [
                    "¿Qué actriz argentina protagoniza la serie de Netflix 'Puerta 7', que trata sobre la violencia en el fútbol?",
                    "Mercedes Morán",
                    "Dolores Fonzi",
                    "Juana Viale",
                    "Mónica Ayos",
                    2,
                ]

            elif nro_preg == 2:
                pregunta = [
                    "¿En qué año Marcelo Tinelli debutó como conductor de televisión?",
                    "1983",
                    "1987",
                    "1990",
                    "1995",
                    3,
                ]

            elif nro_preg == 3:
                pregunta = [
                    "¿Qué famoso escándalo mediático protagonizó Marcelo Tinelli en 2009, relacionado con una supuesta pelea en su programa?",
                    "La pelea con Susana Giménez",
                    "El escándalo con Ricardo Fort",
                    "La pelea entre Graciela Alfano y Aníbal Pachano",
                    "El enfrentamiento con Jorge Rial",
                    3,
                ]

            elif nro_preg == 4:
                pregunta = [
                    "¿Qué conductor argentino fue famoso por su programa 'Sábado Bus'?",
                    "Marcelo Tinelli",
                    "Nicolás Repetto",
                    "Jorge Rial",
                    "Juan Alberto Badía",
                    2,
                ]

            elif nro_preg == 5:
                pregunta = [
                    "¿En qué año se emitió por primera vez el programa de televisión 'Tato Bores, el regreso'?",
                    "1988",
                    "1991",
                    "1993",
                    "1996",
                    3,
                ]

            elif nro_preg == 6:
                pregunta = [
                    "¿Qué futbolista argentino fue arrestado en 2014 en una redada por participar en un juego de "
                    "póker ilegal en un hotel de Buenos Aires?",
                    "Lionel Messi",
                    "Sergio Agüero",
                    "Carlos Tevez",
                    "Ezequiel Lavezzi",
                    3,
                ]

            elif nro_preg == 7:
                pregunta = [
                    "¿Cuál de los siguientes actores NO formaba parte del elenco principal de 'Los Simuladores'?",
                    "Alejandro Fiore",
                    "Diego Peretti",
                    "Martín Seefeld",
                    "Diego Torres",
                    4,
                ]
            elif nro_preg == 8:
                pregunta = [
                    "¿En que ciudad estaba ubicado el hotel desde donde Charly Garcia se tiro del noveno piso?",
                    "CABA",
                    "Mendoza",
                    "Mar del Plata",
                    "Bahia Blanca",
                    2,
                ]
            else:
                pregunta = [
                    "¿En que año hizo su debut como conductor Guido kaczka?",
                    "1999",
                    "1989",
                    "2000",
                    "2002",
                    1,
                ]
    return pregunta


# FUNCION DE EJECUCION DEL JUEGO
def main():
    """Función principal del juego."""
    # El jugador arranca con 5 vidas, sin puntos y sin una categoria elegida.
    puntos = 0
    vidas = 5
    tematica = ""

    print(
        "██████╗ ██╗███████╗███╗   ██╗██╗   ██╗███████╗███╗   ██╗██╗██████╗  ██████╗      █████╗ ██╗          █████╗ ██████╗  ██████╗ ███████╗███╗   ██╗████████╗ █████╗ ██████╗  ██████╗ ███████╗    ██╗"
    )
    print(
        "██╔══██╗██║██╔════╝████╗  ██║██║   ██║██╔════╝████╗  ██║██║██╔══██╗██╔═══██╗    ██╔══██╗██║         ██╔══██╗██╔══██╗██╔════╝ ██╔════╝████╗  ██║╚══██╔══╝██╔══██╗██╔══██╗██╔═══██╗██╔════╝    ██║"
    )
    print(
        "██████╔╝██║█████╗  ██╔██╗ ██║██║   ██║█████╗  ██╔██╗ ██║██║██║  ██║██║   ██║    ███████║██║         ███████║██████╔╝██║  ███╗█████╗  ██╔██╗ ██║   ██║   ███████║██║  ██║██║   ██║███████╗    ██║"
    )
    print(
        "██╔══██╗██║██╔══╝  ██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║██║  ██║██║   ██║    ██╔══██║██║         ██╔══██║██╔══██╗██║   ██║██╔══╝  ██║╚██╗██║   ██║   ██╔══██║██║  ██║██║   ██║╚════██║    ╚═╝"
    )
    print(
        "██████╔╝██║███████╗██║ ╚████║ ╚████╔╝ ███████╗██║ ╚████║██║██████╔╝╚██████╔╝    ██║  ██║███████╗    ██║  ██║██║  ██║╚██████╔╝███████╗██║ ╚████║   ██║   ██║  ██║██████╔╝╚██████╔╝███████║    ██╗"
    )
    print(
        "╚═════╝ ╚═╝╚══════╝╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═╝╚═════╝  ╚═════╝     ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝    ╚═╝"
    )
    print(" A continuacion te explicamos las reglas: ")
    print(
        "* Vas a tener seis categorias en las cuales vas a encontrar preguntas relacionadas a nuestro país, para ganar vas a tener que contestar al menos una bien en cada categoria."
    )
    print(
        "* Las condiciones son: - Tenes 5 vidas en total y solo podes elegir cada categoria una vez."
    )
    print(
        "                       - Una vez que elegiste una categoria no la podes cambiar."
    )
    print(
        "                       - Cada pregunta correcta suma 10 puntos, si es tu segundo intento o posterior suma 5. "
    )

    input("Para continuar presiona cualquier tecla: ")
    print("")

    # Le mostramos las dificultades a elegir y el usuario elige la dificultad del juego
    print("Elegí la dificultad del juego")
    imprimir_dificultades()
    print("")
    eleccion = input("Ingresá la dificultad que deseas: ")

    # Validamos que la dificultad elegida sea valida
    while not validar_dificultad(eleccion):
        print("Valor ingresado no valido. Por favor, intentá nuevamente")
        print("")
        eleccion = input("Dale, elegí la dificultad del juego: ")

    # Si elige salir del juego mostramos un msj de no iniciado
    if eleccion == "FIN":
        print("Juego no iniciado. Saliste del juego, hasta la próxima!")
    # Caso contrario le mostramos la dificultad elegida
    else:
        eleccion = dificultad_seleccionada(eleccion)
        print("Dificultad elegida:", eleccion)
    # Mientras la categoria elegida sea diferente de FIN, tenga vidas y tematicas para elegir se va a ejecutar el juego
    while tematica != "FIN" and eleccion != "FIN" and vidas > 0 and len(categorias) > 0:
        # Mostramos por pantalla las categorias disponibles
        imprimir_categorias()
        categoria_elegida = input("Ingrese la opcion elegida: ")
        validacion = validar_categoria(categoria_elegida)

        # Validamos que la categoria ingresada sea correcta
        while validacion is False:
            print("Che, dale, elegime una opcion valida!")
            categoria_elegida = input("Ingrese la opcion elegida: ")
            validacion = validar_categoria(categoria_elegida)

        tematica = eleccion_categoria(categoria_elegida)

        # Si la tematica elegida es distinta a FIN seguimos con el juego
        if tematica != "FIN":
            # Segun la tematica y la dificultad elegimos de manera random una pregunta
            pregunta = eleccion_preguntas(tematica, eleccion)
            # y la mostramos por pantalla
            imprimir_pregunta(pregunta)

            opcion_elegida = input("Ingrese su respuesta: ")

            validacion = validar_respuestas(opcion_elegida)

            # Validamos que la categoria ingresada sea correcta
            while validacion is False:
                print("Che, dale, elegime una opcion valida!")
                opcion_elegida = input("Ingrese la opcion elegida: ")
                validacion = validar_respuestas(opcion_elegida)

            # Validamos que el input sea igual a la respuesta predefinida como correcta
            if int(opcion_elegida) == pregunta[-1]:
                print("Le pegaste! Felicitaciones, sumaste 10 puntos ٩( ๑╹ ꇴ╹)۶")
                puntos += 10
            else:
                print("Te equivocaste pichón ಠ_ಠ")
                # Mientras la respuesta no sea correcta y le queden vidas

                while (int(opcion_elegida) != pregunta[-1]) and vidas > 0:

                    # Restamos una vida
                    vidas -= 1

                    # Y si le quedan vidas volvemos a preguntar y a validar su respuesta
                    if vidas > 0:
                        print(
                            "Pero igual te quedan ",
                            vidas,
                            "vidas. Asi que podes volver a intentar con otra "
                            "pregunta!",
                        )
                        pregunta = eleccion_preguntas(tematica, eleccion)
                        imprimir_pregunta(pregunta)
                        opcion_elegida = input("Ingrese su respuesta: ")
                        validacion = validar_respuestas(opcion_elegida)

                        # Validamos que la categoria ingresada sea correcta
                        while validacion is False:
                            print("Che, dale, elegime una opcion valida!")
                            opcion_elegida = input("Ingrese la opcion elegida: ")
                            validacion = validar_respuestas(opcion_elegida)

                        if int(opcion_elegida) == pregunta[-1]:
                            print("Hasta que adivinaste!, ahora sumas 5 puntos.")
                            puntos += 5
                        else:
                            print("Te equivocaste pichón ಠ_ಠ")
                    else:
                        print("Te quedaste sin vidas, que mala leche!")
        # Si se queda sin categorias o sin vidas asignamos automaticamente que la categoria es FIN para terminar con
        # la ejecucion del while
        if len(categorias) == 0 or vidas == 0:
            tematica = "FIN"
    # Le mostramos por pantalla si gano, perdio o abandono
    imprimir_resultado(vidas, categorias, puntos)


main()
