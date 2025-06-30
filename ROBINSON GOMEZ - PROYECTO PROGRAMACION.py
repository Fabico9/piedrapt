
# Importamos la librería random para que la computadora haga elecciones aleatorias
import random


# FUNCIONES

# Mostrar el menú principal
def mostrar_menu():
    print("Menú de opciones para Jugar")
    print("1. Contra la computadora")
    print("2. Multijugador (2 jugadores)")
    print("3. Ver estadísticas de las partidas")
    print("4. Salir")

# Jugar una partida entre dos jugadores (o contra la computadora)
def jugar_partida(jugador1, jugador2, contra_computadora=False):
    opciones = ["piedra", "papel", "tijera"]
    
    # Jugador 1 elige
    jugada1 = input(f"{jugador1}, elige entre piedra, papel o tijera: ").lower()
    
    # Jugador 2 (puede ser la computadora)
    if contra_computadora:
        jugada2 = random.choice(opciones)
        print(f"{jugador2} eligió: {jugada2}")
    else:
        jugada2 = input(f"{jugador2}, elige entre piedra, papel o tijera: ").lower()

    # Determinar el resultado
    if jugada1 == jugada2:
        resultado = "empate"
    elif (jugada1 == "piedra" and jugada2 == "tijera") or \
         (jugada1 == "papel" and jugada2 == "piedra") or \
         (jugada1 == "tijera" and jugada2 == "papel"):
        resultado = jugador1
    else:
        resultado = jugador2

    return jugada1, jugada2, resultado

# Mostrar el resumen y estadísticas de las partidas
def mostrar_estadisticas(historial, jugador1, jugador2):
    print("Resumen:")
    print(F"Número de partidas realizadas: {len(historial)}")
    
    for i, partida in enumerate(historial):
        print(f"Partida {i+1}: {jugador1} eligió {partida[0]} - {jugador2} eligió {partida[1]} -> Resultado: ", end="")
        if partida[2] == "empate":
            print("Empate")
        elif partida[2] == jugador1:
            print(f"{jugador1} ganó")
        else:
            print(f"{jugador2} ganó")

    # Calcular estadísticas
    estadisticas = {
        jugador1: {"ganadas": 0, "perdidas": 0, "empatadas": 0},
        jugador2: {"ganadas": 0, "perdidas": 0, "empatadas": 0} }

    for partida in historial:
        if partida[2] == "empate":
            estadisticas[jugador1]["empatadas"] += 1
            estadisticas[jugador2]["empatadas"] += 1
        elif partida[2] == jugador1:
            estadisticas[jugador1]["ganadas"] += 1
            estadisticas[jugador2]["perdidas"] += 1
        else:
            estadisticas[jugador2]["ganadas"] += 1
            estadisticas[jugador1]["perdidas"] += 1

    print("Estadísticas:")
    for jugador in [jugador1, jugador2]:
        e = estadisticas[jugador]
        print(f"{jugador}: ganó {e['ganadas']} partidas, perdió {e['perdidas']} partidas, empató {e['empatadas']} partidas")


# PROGRAMA PRINCIPAL


historial_partidas = []

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1" or opcion == "2":
        jugador1 = input("Nombre del Jugador 1: ")
        if opcion == "1":
            jugador2 = "Computadora"
            contra_computadora = True
        else:
            jugador2 = input("Nombre del Jugador 2: ")
            contra_computadora = False

        # Preguntar si se quiere definir un número fijo de partidas
        definir_numero = input("¿Deseas definir un número de partidas a jugar? (Sí/No): ").lower()
        if definir_numero in ["sí", "si"]:
            num_partidas = int(input("¿Cuántas partidas deseas jugar?: "))
            for _ in range(num_partidas):
                jugada1, jugada2, resultado = jugar_partida(jugador1, jugador2, contra_computadora)
                historial_partidas.append((jugada1, jugada2, resultado))
        else:
            while True:
                jugada1, jugada2, resultado = jugar_partida(jugador1, jugador2, contra_computadora)
                historial_partidas.append((jugada1, jugada2, resultado))
                continuar = input("¿Deseas jugar otra partida? (Sí/No): ").lower()
                if continuar not in ["sí", "si"]:
                    break

        mostrar_estadisticas(historial_partidas, jugador1, jugador2)

    elif opcion == "3":
        if historial_partidas:
            mostrar_estadisticas(historial_partidas, jugador1, jugador2)
        else:
            print("No hay partidas registradas aún.")

    elif opcion == "4":
        print("¡Gracias por jugar!")
        break

    else:
        print("Opción no válida. Intenta nuevamente.")
        
