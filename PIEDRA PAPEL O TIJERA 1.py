import random

print("Bienvenido al Juego de Piedra, Papel o Tijera")

usuario = input("Elegir entre piedra, papel o tijera: ")


opciones = ["piedra", "papel", "tijera"]

computadora = random.choice(opciones)


print("Tú elegiste:" + usuario)
print("La computadora eligió: " + computadora)


if usuario == computadora:
    print("Empate")
elif (usuario == "piedra" and computadora == "tijera") or \
     (usuario == "papel" and computadora == "piedra") or \
     (usuario == "tijera" and computadora == "papel"):
    print("¡Ganaste!")
else:
    print("Perdiste.")



