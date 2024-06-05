import random

# CONSTANTES
niveles_dificultad = ["BÁSICO", "DIFÍCIL", "EXPERTO"]
inputs_validos_dificultad = ["FIN", '1', '2', '3']
inputs_validos_categorias = ["FIN", '1', '2', '3', '4', '5', '6']
inputs_validos_preguntas = ['1', '2', '3', '4']
categorias = ["HISTORIA", "DEPORTE", "CIENCIA", "ARTE", "GEOGRAFIA", "ENTRETENIMIENTO"]


# FUNCIONES

# FUNCIONES DE IMRPRESION

def imprimir_dificultades():
    """Muestra por pantalla los niveles de dificultad."""
    for i in range(len(niveles_dificultad)):
        print(i + 1, " - ", niveles_dificultad[i])
    print("O ingresá FIN para salir del juego. ")


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
        if i > 0:
            print(i, " - ", pregunta[i])
        else:
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


# FUNCIONES DE VALIDACION DE INPUTS
def validar_dificultad(eleccion):
    """Valida que la dificultad seleccionada sea un input valido."""
    dificultad_valida = eleccion in inputs_validos_dificultad
    return dificultad_valida


def validar_respuestas(eleccion):
    """Chequea que la respuesta a la pregunta seleccionada sea un input valido."""
    respuesta_valida = eleccion in inputs_validos_preguntas
    return respuesta_valida


def validar_categoria(dato_ingresado):
    """Valida que el input ingresado para las categorias este en el rango correcto de opciones disponibles.
    :return es_valido: Bool, devuelve True si es un input valido o False en caso contrario."""

    es_valido = dato_ingresado in inputs_validos_categorias

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


def eleccion_preguntas(categoria, eleccion_dificultad):
    """Según la categoria ingresada devuelve una pregunta elegida de manera random.
    :param categoria: Str, nombre de la categoria elegida.
    :param eleccion_dificultad: Str, tipo de dificultad elegida.
    :return pregunta: List, lista con la pregunta, las opciones disponibles y la opcion correcta."""
    nro_preg = random.randint(0, 9)
    if categoria == 'HISTORIA':
        if eleccion_dificultad == "BÁSICO":
            if nro_preg == 0:
                pregunta = ["pregunta historia 1?", "opcion1", "opcion2", "opcion3", 1]
            else:
                pregunta = ["pregunta historia 2?", "opcion1", "opcion2", "opcion3", 1]
        elif eleccion_dificultad == "DIFICIL":
            if nro_preg == 0:
                pregunta = ["pregunta historia 1?", "opcion1", "opcion2", "opcion3", 1]
            else:
                pregunta = ["pregunta historia 2?", "opcion1", "opcion2", "opcion3", 1]
        else:
            if nro_preg == 0:
                pregunta = ["pregunta historia 1?", "opcion1", "opcion2", "opcion3", 1]
            else:
                pregunta = ["pregunta historia 2?", "opcion1", "opcion2", "opcion3", 1]
    elif categoria == "DEPORTE":
        if eleccion_dificultad == "BÁSICO":
            # nivel basico
            if nro_preg == 0:
                pregunta = ["¿Quién es Diego Maradona?", "Un político", "Un futbolista", "Un actor", "Un cantante", 2]
            elif nro_preg == 1:
                pregunta = ["¿En qué deporte se destacó Gabriela Sabatini?", "Fútbol", "Natación", "Tenis",
                            "Baloncesto", 3]
            elif nro_preg == 2:
                pregunta = [
                    "¿Quién es la destacada nadadora argentina que ganó tres medallas en los Juegos Olímpicos de la Juventud Buenos Aires 2018?",
                    "Delfina Pignatiello", "Luciana Aymar", "Cecilia Biagioli", "Gabriela Sabatini", 1]
            elif nro_preg == 3:
                pregunta = ["¿En qué deporte se destaca Paula Pareto?", "Karate", "Taekwondo", "Judo", "Lucha libre", 3]
            elif nro_preg == 4:
                pregunta = ["¿En qué ciudad se encuentra el estadio Monumental?", "Rosario", "Córdoba", "Buenos Aires",
                            "Mendoza", 3]
            elif nro_preg == 5:
                pregunta = ["¿Qué selección ganó la Copa América 2021?", "Chile", "Brasil", "Uruguay", "Argentina", 4]
            elif nro_preg == 6:
                pregunta = ["¿Cómo se llama el equipo de rugby nacional de Argentina?", "Los Pumas", "Los Cóndores",
                            "Los Jaguares", "Los Leones", 1]
            elif nro_preg == 7:
                pregunta = ["¿En qué deporte se destacó Luciana Aymar?", "Tenis", "Hockey sobre césped", "Natación",
                            "Voleibol", 2]
            elif nro_preg == 8:
                pregunta = ["¿Qué equipo argentino de fútbol es conocido como 'La Academia'?", "San Lorenzo",
                            "Independiente", "Racing", "River Plate", 4]
            else:
                pregunta = ["¿En qué deporte se destaca Lionel Messi?", "Fútbol", "Baloncesto", "Tenis", "Rugby", 1]
        # nivel intermedio
        elif eleccion_dificultad == "DIFÍCIL":
            if nro_preg == 0:
                pregunta = ["¿Cuántas veces ha ganado Argentina la Copa Mundial de Fútbol?", "Dos", "Tres", "Cuatro",
                            "Una", 2]
            elif nro_preg == 1:
                pregunta = ["¿Cuál fue el primer club de fútbol fundado en Argentina?", "Rivel Plate", "Boca Juniors",
                            "Quilmes", "Rosario Central", 3]
            elif nro_preg == 2:
                pregunta = ["¿En qué año se retiró Diego Maradona del fútbol profesional?", "1994", "1997", "2000",
                            "2002", 2]
            elif nro_preg == 3:
                pregunta = ["¿Quién es el tenista argentino con más títulos de Grand Slam?", "David Nalbandian",
                            "Gastón Gaudio", "Guillermo Vilas", "Juan Martín del Potro", 3]
            elif nro_preg == 4:
                pregunta = ["¿Qué equipo de fútbol argentino tiene más títulos de la Copa Libertadores?",
                            "Boca Juniors", "River Plate", "Independiente", "Estudiantes de La Plata", 3]
            elif nro_preg == 5:
                pregunta = ["¿Cómo se llama el clásico entre Boca Juniors y River Plate?", "El Clásico", "THE BIG ONE",
                            "El Superclásico", "El Gran Partido", 3]
            elif nro_preg == 6:
                pregunta = [
                    "¿Quién es considerado uno de los mejores jugadores de baloncesto en la historia de Argentina?",
                    "Fabricio Oberto", "Andrés Nocioni", "Luis Scola", "Emanuel Ginóbili", 4]
            elif nro_preg == 7:
                pregunta = ["¿En qué año ganó Argentina la medalla de oro en baloncesto en los Juegos Olímpicos?",
                            "1996", "2000", "2004", "2008", 3]
            elif nro_preg == 8:
                pregunta = ["¿¿Cuál fue el primer equipo argentino en ganar la Copa Libertadores?", "Racing Club",
                            "Estudiantes de La Plata", "Boca Juniors", "Independiente", 2]
            else:
                pregunta = ["¿Quién fue la primera mujer argentina en ganar una medalla olímpica?", "Jeanette Campbell",
                            "Gabriela Sabatini", "Ninguna es correcta", "Paula Pareto", 1]
        # nivel avanzado
        else:
            if nro_preg == 0:
                pregunta = ["¿Cuál es el récord de goles de Lionel Messi en una sola temporada de La Liga?", "50", "46",
                            "54", "48", 1]
            elif nro_preg == 1:
                pregunta = ["¿Qué futbolista argentino ha jugado en más mundiales", "Diego Maradona",
                            "Javier Mascherano", "Lionel Messi", "Gabriel Batistuta", 2]
            elif nro_preg == 2:
                pregunta = ["¿Cuántos títulos de ATP ha ganado Juan Martín del Potro?", "18", "22", "25", "20", 3]
            elif nro_preg == 3:
                pregunta = ["¿En qué equipo debutó profesionalmente Juan Román Riquelme?", "River Plate",
                            "Argentinos Juniors", "Boca Juniors", "Barcelona", 2]
            elif nro_preg == 4:
                pregunta = [
                    "¿Qué atleta argentina se convirtió en la primera mujer en ganar una medalla de oro en un Mundial de Atletismo?",
                    "Jennifer Dahlgren", "Victoria Woodward", "María Luz Tesuri", "Noelia Martínez", 4]
            elif nro_preg == 5:
                pregunta = ["¿Cuántos puntos anotó Emanuel Ginóbili en su carrera en la NBA?", "10,496", "14,043",
                            "13,001", "12,572", 2]
            elif nro_preg == 6:
                pregunta = ["¿Qué jugador argentino es conocido como 'El Príncipe' en el fútbol europeo?",
                            "Juan Sebastián Verón", "Enzo Francescoli", "Gabriel Batistuta", "Hernán Crespo", 2]
            elif nro_preg == 7:
                pregunta = ["¿Cuál es el récord de victorias consecutivas del equipo de rugby Los Pumas?", "8", "11",
                            "12", "14", 3]
            elif nro_preg == 8:
                pregunta = ["¿En qué equipo de la NBA jugó Luis Scola durante más temporadas?", "Phoenix Suns",
                            "Indiana Pacers", "Houston Rockets", "Brooklyn Nets", 3]
            else:
                pregunta = ["¿Qué logro deportivo alcanzó Delfina Merino en el año 2017?", "Ganó el oro olímpico",
                            "Fue nombrada mejor jugadora de la Copa del Mundo", "Se retiró del hockey",
                            "Fue elegida mejor jugadora del mundo por la FIH", 4]
    elif categoria == "CIENCIA":
        if eleccion_dificultad == "BÁSICO":
            if nro_preg == 0:
                pregunta = ["¿Quién fue el primer científico argentino en recibir el Nobel de medicina?",
                            "Bernardo Houssay",
                            "Luis Federico Leloir", "Cesar Milstein", "Juan Carlos Fasciolo", 1]
            elif nro_preg == 1:
                pregunta = ["¿Qué institución argentina es reconocida por su contribución a la investigación "
                            "cintífica y tecnológica y fue fundada en 1958?", "CONICET (Consejo Nacional de "
                                                                              "Investigaciones Cientificas y Técnicas)",
                            "INTA (Instituto Nacional de Tecnología Agropecuaria)",
                            "INTI (Instituto Nacional de Tecnología Industrial)",
                            "CITEDEF (Instituto de Investigaciones Cientificas y Tecnicas de las FFAA)", 1]
            elif nro_preg == 2:
                pregunta = ["¿Cuál es el nombre del centro de investigación dedicado a la física y biología molecular "
                            "ubicado en Bariloche? ", "CITEDEF",
                            "INTA", "Instituto Balseiro", "Fundación Favaloro", 3]
            elif nro_preg == 3:
                pregunta = ["¿Qué científico argentino es reconocido por desarrollar la técnica del bypass coronario?",
                            "Bernardo Houssay",
                            "Rene Favaloro", "Luis Federico Leloir", "Salvador Mazza", 2]
            else:
                pregunta = ["pregunta ciencia 2?", "opcion1", "opcion2", "opcion3", 1]
        elif eleccion_dificultad == "DIFICIL":
            if nro_preg == 0:
                pregunta = ["pregunta ciencia 1?", "opcion1", "opcion2", "opcion3", 1]
            else:
                pregunta = ["pregunta ciencia 2?", "opcion1", "opcion2", "opcion3", 1]
        else:
            if nro_preg == 0:
                pregunta = ["pregunta ciencia 1?", "opcion1", "opcion2", "opcion3", 1]
            else:
                pregunta = ["pregunta ciencia 2?", "opcion1", "opcion2", "opcion3", 1]
    elif categoria == "ARTE":
        # nivel basico
        if eleccion_dificultad == "BÁSICO":
            if nro_preg == 0:
                pregunta = ["¿Quién es considerado el padre del tango?", "Carlos Gardel", "Astor Piazzolla",
                            "Aníbal Troilo", "Carlos Di Sarli", 1]
            elif nro_preg == 1:
                pregunta = ["¿Cuál de estos artistas argentinos es conocido por sus pinturas surrealistas?",
                            "Antonio Berni", "Xul Solar", "Benito Quinquela Martín", "Emilio Pettoruti", 2]
            elif nro_preg == 2:
                pregunta = ["¿Quién fue el arquitecto argentino que diseñó el Obelisco de Buenos Aires?",
                            "Francisco Salamone", "Alejandro Bustillo", "César Pelli", "Alberto Prebisch", 4]
            elif nro_preg == 3:
                pregunta = ["¿Qué escultor argentino creó la obra 'El pensador'?", "Erminio Blotta", "Lola Mora",
                            "Lucio Fontana", "Auguste Rodin", 1]
            elif nro_preg == 4:
                pregunta = ["¿En qué museo se encuentra expuesta la famosa pintura 'El Grito' de Edvard Munch?",
                            "MALBA", "Museo Nacional de Bellas Artes", "Museo de Arte Moderno de Buenos Aires",
                            "Museo de Arte Contemporáneo de Rosario", 2]
            elif nro_preg == 5:
                pregunta = ["¿Qué escritor argentino escribió la novela 'Rayuela'?", "Jorge Luis Borges",
                            "Julio Cortázar", "Adolfo Bioy Casares", "Ernesto Sabato", 2]
            elif nro_preg == 6:
                pregunta = ["¿Qué famoso muralista argentino pintó el fresco 'Ejercicio Plástico'?",
                            "David Alfaro Siqueiros", "Diego Rivera", "José Clemente Orozco", "Antonio Berni", 4]
            elif nro_preg == 7:
                pregunta = ["¿Cuál de estos artistas argentinos es conocido por su obra 'La Catedral'?",
                            "Antonio Berni", "Xul Solar", "Benito Quinquela Martín", "Emilio Pettoruti", 3]
            elif nro_preg == 8:
                pregunta = ["¿Qué famoso músico argentino es conocido por su obra 'Adiós Nonino'?", "Astor Piazzolla",
                            "Carlos Gardel", "Aníbal Troilo", "Osvaldo Pugliese", 1]
            else:
                pregunta = [
                    "¿Cuál es la danza tradicional argentina conocida por su origen en la provincia de La Rioja?",
                    "Chacarera", "Zamba", "Cueca", "Gato", 4]
        # nivel intermedio
        elif eleccion_dificultad == "DIFICIL":
            if nro_preg == 0:
                pregunta = ["¿Qué reconocido arquitecto argentino diseñó el Teatro Colón de Buenos Aires?",
                            "Alejandro Bustillo", "César Pelli", "Alberto Prebisch", "Francisco Salamone", 3]
            elif nro_preg == 1:
                pregunta = ["¿Cuál es el nombre del museo de arte contemporáneo ubicado en la Ciudad de Buenos Aires?",
                            "MALBA", "Museo Nacional de Bellas Artes", "Museo de Arte Moderno de Buenos Aires",
                            "Museo de Arte Contemporáneo de Rosario", 1]
            elif nro_preg == 2:
                pregunta = ["¿Qué pintor argentino es conocido por su obra 'Contra el quebracho'?", "Antonio Berni",
                            "Xul Solar", "Benito Quinquela Martín", "Emilio Pettoruti", 1]
            elif nro_preg == 3:
                pregunta = ["¿Quién fue el primer director de la Orquesta Filarmónica de Buenos Aires?",
                            "Astor Piazzolla", "Carlos Gardel", "Aníbal Troilo", "Alberto Ginastera", 4]
            elif nro_preg == 4:
                pregunta = ["¿Qué famoso escultor argentino es conocido por sus obras monumentales en hormigón armado?",
                            "Erminio Blotta", "Lola Mora", "Lucio Fontana", "Pablo Curatella Manes", 4]
            elif nro_preg == 5:
                pregunta = ["¿Qué escritor argentino es conocido por su obra 'Sobre héroes y tumbas'?",
                            "Jorge Luis Borges", "Julio Cortázar", "Adolfo Bioy Casares", "Ernesto Sabato", 4]
            elif nro_preg == 6:
                pregunta = ["¿Cuál de estos artistas argentinos es conocido por su obra 'El Jugador de Ajedrez'?",
                            "Antonio Berni", "Xul Solar", "Benito Quinquela Martín", "Emilio Pettoruti", 2]
            elif nro_preg == 7:
                pregunta = ["¿Qué escultor argentino creó la obra 'Monumento a la Bandera' en Rosario?",
                            "Erminio Blotta", "Lola Mora", "Lucio Fontana", "Pablo Curatella Manes", 2]
            elif nro_preg == 8:
                pregunta = ["¿Qué famoso muralista argentino pintó el fresco 'La Tortura'?", "David Alfaro Siqueiros",
                            "Diego Rivera", "José Clemente Orozco", "Antonio Berni", 1]
            else:
                pregunta = ["¿Cuál de estos artistas argentinos es conocido por su obra 'Lavanderas'?", "Antonio Berni",
                            "Xul Solar", "Benito Quinquela Martín", "Emilio Pettoruti", 3]
        # nivel avanzado
        else:
            if nro_preg == 0:
                pregunta = ["¿Qué reconocido pintor argentino es conocido por su obra 'La Furia'?", "Antonio Berni",
                            "Xul Solar", "Benito Quinquela Martín", "Emilio Pettoruti", 1]
            elif nro_preg == 1:
                pregunta = ["¿Cuál de estos artistas argentinos es conocido por su obra 'Cantos Rodados'?",
                            "Antonio Berni", "Xul Solar", "Benito Quinquela Martín", "Emilio Pettoruti", 2]
            elif nro_preg == 2:
                pregunta = ["¿Cuál de estos artistas argentinos es conocido por su obra 'La ventana'?", "Antonio Berni",
                            "Xul Solar", "Benito Quinquela Martín", "Emilio Pettoruti", 3]
            elif nro_preg == 3:
                pregunta = ["¿Qué famoso pintor argentino es conocido por su obra 'El desfile'?", "Antonio Berni",
                            "Xul Solar", "Benito Quinquela Martín", "Emilio Pettoruti", 4]
            elif nro_preg == 4:
                pregunta = ["¿Qué reconocido músico argentino es conocido por su obra 'Milonga del Ángel'?",
                            "Astor Piazzolla", "Carlos Gardel", "Aníbal Troilo", "Osvaldo Pugliese", 1]
            elif nro_preg == 5:
                pregunta = ["¿Cuál de estos artistas argentinos es conocido por su obra 'Calle de Barracas'?",
                            "Antonio Berni", "Xul Solar", "Benito Quinquela Martín", "Emilio Pettoruti", 2]
            elif nro_preg == 6:
                pregunta = ["¿Quién fue el escritor argentino ganador del Premio Nobel de Literatura en 2010?",
                            "Jorge Luis Borges", "Julio Cortázar", "Adolfo Bioy Casares", "Mario Vargas Llosa", 4]
            elif nro_preg == 7:
                pregunta = [
                    "¿Qué famoso pianista argentino es conocido por su interpretación de 'El Concierto de Aranjuez'?",
                    "Astor Piazzolla", "Martha Argerich", "Raúl Di Blasio", "Osvaldo Pugliese", 2]
            elif nro_preg == 8:
                pregunta = ["¿Cuál de estos artistas argentinos es conocido por su obra 'El solterito'?",
                            "Antonio Berni", "Xul Solar", "Benito Quinquela Martín", "Emilio Pettoruti", 3]
            else:
                pregunta = ["¿Qué reconocido poeta argentino escribió 'El Aleph'?", "Jorge Luis Borges",
                            "Julio Cortázar", "Adolfo Bioy Casares", "Ernesto Sabato", 1]
    elif categoria == "GEOGRAFIA":
        # basico
        if eleccion_dificultad == "BÁSICO":
            if nro_preg == 0:
                pregunta = ["¿Cuál es la montaña más alta de Argentina?", "Aconcagua", "Fitz Roy", "Cerro Torre",
                            "Chapelco", 1]
            elif nro_preg == 1:
                pregunta = ["¿Cuál es el río más largo de Argentina?", "Correntoso", "Paraná", "Caleufú", "Paraguay", 2]
            elif nro_preg == 2:
                pregunta = ["¿Qué famoso glaciar se encuentra en el Parque Nacional Los Glaciares?", "No existe",
                            "Glaciar Martial", "Glaciar Perito Moreno", "Glaciar Upsala", 3]
            elif nro_preg == 3:
                pregunta = ["¿En qué región de Argentina se encuentra la famosa Patagonia?", "Norte", "Centro", "Sur",
                            "Oeste", 3]
            elif nro_preg == 4:
                pregunta = ["¿Cuál es la capital de Argentina?", "Neuquén", "Buenos Aires", "Córdoba", "Rosario", 2]
            elif nro_preg == 5:
                pregunta = ["¿Qué océano baña las costas de Argentina?", "Ártico", "Pacífico", "Índico", "Atlántico", 4]
            elif nro_preg == 6:
                pregunta = ["¿Cuál es el desierto más árido del mundo, que se encuentra en Argentina?", "No hay",
                            "Kalahari", "Desierto del Monte", "Atacama", 1]
            elif nro_preg == 7:
                pregunta = ["¿En qué región de Argentina se encuentra la famosa región vinícola de Mendoza?", "Oeste",
                            "Noroeste", "Cuyo", "Patagonia", 2]
            elif nro_preg == 8:
                pregunta = ["¿Cuál es el nombre de las famosas cataratas en la provincia de Misiones?",
                            "Garganta del Diablo", "Cataratas del Iguazú", "Cataratas del Salto",
                            "Cataratas del Paraná", 2]
            else:
                pregunta = ["¿Qué famosa formación rocosa se encuentra en la provincia de Salta?", "Cerro Chaltén",
                            "Cerro de los Siete Colores", "Cerro Catedral", "Cerro Colorido", 2]
        # dificil
        elif eleccion_dificultad == "DIFICIL":
            if nro_preg == 0:
                pregunta = ["¿Cuál de las siguientes provincias argentinas no tiene costa?", "Buenos Aires", "Santa Fe",
                            "Mendoza", "Misiones", 3]
            elif nro_preg == 1:
                pregunta = ["¿En qué provincia se encuentra el Cerro Aconcagua?", "Mendoza", "Neuquén", "Santa Cruz",
                            "Río Negro", 1]
            elif nro_preg == 2:
                pregunta = ["¿Cuál de estos lagos no se encuentra en la provincia de Neuquén?", "Lago Nahuel Huapi",
                            "Lago Argentino", "Lago Traful", "Lago Hermoso", 2]
            elif nro_preg == 3:
                pregunta = [
                    "¿Cuál es el nombre de la península ubicada en la provincia de Chubut, famosa por avistamiento de ballenas?",
                    "Península Valdés", "Península Mitre", "Península San José", "Península Ballenas", 1]
            elif nro_preg == 4:
                pregunta = ["¿Cuál es el nombre de la región montañosa ubicada en la provincia de San Juan?",
                            "Cordillera de los Andes", "Cordillera de los Vientos", "Cordillera de la Costa",
                            "Cordilleta de los Alcones", 2]
            elif nro_preg == 5:
                pregunta = ["¿Cuál de las siguientes provincias limita con Bolivia?", "Jujuy", "Salta", "Corrientes",
                            "La Pampa", 2]
            elif nro_preg == 6:
                pregunta = [
                    "¿Qué famosa formación natural se encuentra en la provincia de La Rioja y es un importante destino turístico?",
                    "Valle de la Luna", "Quebrada de Humahuaca", "Cueva de las Manos", "Cueva de las aves", 1]
            elif nro_preg == 7:
                pregunta = ["¿Qué provincia argentina se caracteriza por tener una importante producción de petróleo?",
                            "Neuquén", "Córdoba", "Entre Ríos", "Santiago del Estero", 1]
            elif nro_preg == 8:
                pregunta = ["¿Cuál es el nombre del pico más alto de la provincia de Tierra del Fuego?",
                            "Cerro Fitz Roy", "Cerro Torre", "Monte Olivia", "Monte Tronador", 3]
            else:
                pregunta = ["¿Qué río forma parte de la frontera entre Argentina y Uruguay?", "Río Paraná",
                            "Río Uruguay", "Río Iguazú", "Rió Salado", 2]
        # avanzado
        else:
            if nro_preg == 0:
                pregunta = ["¿Cuál es el nombre de la región semiárida ubicada en la provincia de Buenos Aires?",
                            "Pampa Húmeda", "Chaco Austral", "Monte", "Pampa Seca", 3]
            elif nro_preg == 1:
                pregunta = ["¿Qué provincia argentina es conocida por su producción de vino Malbec?", "Mendoza",
                            "San Juan", "La Rioja", "Salta", 1]
            elif nro_preg == 2:
                pregunta = ["¿Cuál es el nombre del volcán más alto de Argentina?", "Lanín", "Copahue",
                            "Ojos del Salado", "Tronador", 3]
            elif nro_preg == 3:
                pregunta = [
                    "¿Qué parque nacional argentino es conocido por ser el hogar de una gran variedad de especies de aves?",
                    "Parque Nacional Los Glaciares", "Parque Nacional Nahuel Huapi", "Parque Nacional Iguazú",
                    "Parque Nacional El Palmar", 2]
            elif nro_preg == 4:
                pregunta = ["¿Cuál de las siguientes provincias no tiene frontera con Chile?", "Neuquén", "Mendoza",
                            "Chaco", "Formosa", 3]
            elif nro_preg == 5:
                pregunta = ["¿Qué provincia argentina es famosa por su producción de yerba mate?", "Corrientes",
                            "Misiones", "Formosa", "Entre Ríos", 2]
            elif nro_preg == 6:
                pregunta = ["¿Cuál es el nombre del río más ancho de Argentina?", "Río Paraná", "Río de la Plata",
                            "Río Uruguay", "Río Colorado", 2]
            elif nro_preg == 7:
                pregunta = ["¿Qué provincia argentina es famosa por sus formaciones geológicas y cañones multicolores?",
                            "Jujuy", "La Rioja", "San Juan", "Salta", 1]
            elif nro_preg == 8:
                pregunta = ["¿Qué cordillera atraviesa la provincia de Mendoza?", "Cordillera de los Andes",
                            "Cordillera de la Costa", "Cordillera de los Vientos", "Cordillera del Tigre", 1]
            else:
                pregunta = ["¿Qué provincia argentina limita con Paraguay y Brasil?", "Buenos Aires", "Entre Ríos",
                            "Formosa", "Corrientes", 4]
    else:
        # entretenimiento
        # nivel basico
        if eleccion_dificultad == "BÁSICO":
            if nro_preg == 0:
                pregunta = ["pregunta entretenimiento 1 ?", "opcion1", "opcion2", "opcion3", 1]
            else:
                pregunta = ["pregunta? entretenimiento 2 ?", "opcion1", "opcion2", "opcion3", 1]
        # nivel dificil
        elif eleccion_dificultad == "DIFICL":
            if nro_preg == 0:
                pregunta = ["pregunta entretenimiento 1 ?", "opcion1", "opcion2", "opcion3", 1]
            else:
                pregunta = ["pregunta? entretenimiento 2 ?", "opcion1", "opcion2", "opcion3", 1]
        # nivel experto
        else:
            if nro_preg == 0:
                pregunta = ["pregunta entretenimiento 1 ?", "opcion1", "opcion2", "opcion3", 1]
            else:
                pregunta = ["pregunta? entretenimiento 2 ?", "opcion1", "opcion2", "opcion3", 1]
    return pregunta


# FUNCION DE EJECUCION DEL JUEGO
def main():
    """Función principal del juego."""
    # El jugador arranca con 5 vidas, sin puntos y sin una categoria elegida.
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
                        print("Pero igual te quedan ", vidas, "vidas. Asi que podes volver a intentar con otra "
                                                              "pregunta!")
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
