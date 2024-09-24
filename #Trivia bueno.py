import random

# Pedimos al usuario su nombre
usuario = input("Ingrese su usuario: ")
print(f"¡Bienvenido al mejor juego de preguntas, {usuario}!")

# Diccionario y tuplas de cuestionario
cuestionario = {
    "Deportes": [
        ("¿Cuándo anotó su primer gol Messi?", 
         ("a) 1 de mayo del 2005", "b) 10 de junio de 2004", "c) 15 de enero de 2007", "d) 10 de junio de 2008"), 
         "a"),
        ("¿Cuántas copas mundiales tiene Pelé?", 
         ("a) 5 mundiales", "b) 2 mundiales", "c) 1 mundial", "d) 3 mundiales"), 
         "d"),
        ("¿Cuántos goles anotó Cristiano Ronaldo en toda su carrera?", 
         ("a) 900", "b) 850", "c) 1000", "d) 770"), 
         "b"),
        ("¿La invención del voleibol fue en?", 
         ("a) 9 de febrero de 1885", "b) 4 de enero de 1896", "c) 30 de febrero de 1987", "d) 15 de abril de 1882"), 
         "b"),
        ("Un cubo de Rubik tiene caras en rojo, naranja, verde, amarillo, azul y... ¿Qué otro color?", 
         ("a) morado", "b) negro", "c) blanco", "d) gris"), 
         "c"),
        ("¿Quién ganó el mundial de fútbol de 2010?", 
         ("a) Francia", "b) España", "c) Brasil", "d) Colombia"), 
         "b"),
        ("¿En qué posición juega el cancerbero de un equipo de fútbol?", 
         ("a) Lateral", "b) Extremo", "c) Portero", "d) Delantero"), 
         "c"),
        ("¿Quién se considera el mejor jugador de baloncesto de todos los tiempos?", 
         ("a) Michael Ballack", "b) Julian Smith", "c) Kobe Bryant", "d) Michael Jordan"), 
         "d"),
        ("¿Qué tipo de competición es el Giro de Italia?", 
         ("a) Golf", "b) Ciclismo", "c) Fútbol", "d) Baloncesto"), 
         "b"),
        ("¿Cuánto dura un partido de balonmano?", 
         ("a) 70 minutos", "b) 60 minutos", "c) 40 minutos", "d) 30 minutos"), 
         "b"),
    ],
    "Historia": [
        ("¿Cuántos años duró la Segunda Guerra Mundial?", 
         ("a) 6 años", "b) 3 años", "c) 4 años", "d) 10 años"), 
         "a"),
        ("¿Quién inventó la bombilla?", 
         ("a) Thomas Edison", "b) Nikola Tesla", "c) Alexander Graham Bell", "d) Ever Kirchhoff"), 
         "a"),
        ("¿Cuándo acabó la II Guerra Mundial?", 
         ("a) 1956", "b) 1930", "c) 1945", "d) 1940"), 
         "c"),
        ("¿En qué año se produjo la Revolución Francesa?", 
         ("a) 1740", "b) 1789", "c) 1840", "d) 1850"), 
         "b"),
        ("¿En qué año llegó Cristóbal Colón a América?", 
         ("a) 1500", "b) 1420", "c) 1492", "d) 1450"), 
         "c"),
        ("Según la Biblia, ¿cuántos años vivió Matusalén?", 
         ("a) 800 años", "b) 80 años", "c) 100 años", "d) 969 años"), 
         "d"),
        ("¿En qué país nació Adolf Hitler?", 
         ("a) Colombia", "b) Austria", "c) Rusia", "d) Inglaterra"), 
         "b"),
        ("¿Cuánto duró 'La Guerra de los Cien Años'?", 
         ("a) 100 años", "b) 116 años", "c) 50 años", "d) 120 años"), 
         "b"),
        ("¿Hace cuánto se extinguieron los dinosaurios?", 
         ("a) Hace 66 millones de años", "b) Hace 100 millones de años", "c) Hace 40 años", "d) Todas las anteriores"), 
         "a"),
        ("¿Quién fue el último faraón de Egipto?", 
         ("a) Gaviria II", "b) Amosis I", "c) Akenatón", "d) Ramsés III"), 
         "d")
    ]
}

puntuacion = 0  # controla el número de puntuación
total_preguntas = 20  # número total de preguntas

# Mantiene el control de cuántas preguntas hemos hecho
preguntas_hechas = 0

# Seleccionamos preguntas aleatoriamente cambiando de categoría cada vez
while preguntas_hechas < total_preguntas:
    # Elegimos una categoría aleatoria
    categoria = random.choice(list(cuestionario.keys()))
    
    # Si ya no hay preguntas en esa categoría, la removemos
    if len(cuestionario[categoria]) == 0:
        del cuestionario[categoria]
        continue
    
    # Escogemos una pregunta aleatoria de la categoría seleccionada
    pregunta, opciones, respuesta_correcta = random.choice(cuestionario[categoria])
    cuestionario[categoria].remove((pregunta, opciones, respuesta_correcta))  # Removemos la pregunta para no repetirla
    
    # Mostramos la categoría, la pregunta y las opciones
    print(f"\nCategoría: {categoria}")
    print("\n----------------------")
    print(pregunta)
    
    for opcion in opciones:
        print(opcion)
    
    # Validación de respuesta
    if input("Ingrese su respuesta (a, b, c, d): ") == respuesta_correcta:
        puntuacion += 1
        print("¡CORRECTO! :)")
    else:
        print(f"INCORRECTO! :(. La respuesta correcta era: {respuesta_correcta}")
    
    preguntas_hechas += 1

# Resumen del juego cuando finalice y de su resultado
print("\n----------------------")
print("-------RESUMEN-------")
print("----------------------")
print(f"Respuestas correctas: {puntuacion}")
print(f"Su puntuación es: {int((puntuacion / total_preguntas) * 100)}%")