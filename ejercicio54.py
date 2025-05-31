import random

def sacar_carta():
    cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    carta_aleatoria = random.choice(cartas)
    return carta_aleatoria

def calcular_puntuaje_mano(cartas):
    if sum(cartas) == 21 and len(cartas) == 2:
        return 0
    if 11 in cartas and sum(cartas) > 21:
        cartas.remove(11)
        cartas.append(1)
    return sum(cartas)

def comparar_puntuajes(suma_cartas_usuario, suma_cartas_casa):
    if suma_cartas_usuario == suma_cartas_casa:
        return "Empate"
    elif suma_cartas_casa == 0:
        return "La casa gana, tiene BLACKJACK"
    elif suma_cartas_usuario == 0:
        return "El jugador gana, tiene BLACKJACK"
    elif suma_cartas_usuario > 21:
        return "Lo siento te has pasado del 21"
    elif suma_cartas_casa > 21:
        return "GANASTE"
    elif suma_cartas_usuario > suma_cartas_casa:
        return "Felicidades, le ha ganado a la casa"
    else:
        return "Haz perdido"

def jugar_blackjack():
    cartas_usuario = []
    cartas_casa = []
    juego_terminado = False

    for _ in range(2):
        cartas_usuario.append(sacar_carta())
        cartas_casa.append(sacar_carta())

    while not juego_terminado:
        suma_cartas_usuario = calcular_puntuaje_mano(cartas_usuario)
        suma_cartas_casa = calcular_puntuaje_mano(cartas_casa)

        print(f"Tus cartas son: {cartas_usuario}, con puntaje {suma_cartas_usuario}")
        print(f"La segunda carta de la casa es: {cartas_casa[1]}")

        if suma_cartas_usuario == 0 or suma_cartas_casa == 0 or suma_cartas_usuario > 21:
            juego_terminado = True
        else:
            usuario_deberia = input("¿Desea otra carta o desea quedarse? ")
            if usuario_deberia.lower() == "otra":
                cartas_usuario.append(sacar_carta())
            else:
                juego_terminado = True

    while suma_cartas_casa != 0 and suma_cartas_casa < 17:
        cartas_casa.append(sacar_carta())
        suma_cartas_casa = calcular_puntuaje_mano(cartas_casa)

    print(f"Tu mano fue {cartas_usuario}, la mano de la casa fue {cartas_casa}")
    print(f"Tu suma fue {suma_cartas_usuario} y la casa tuvo {suma_cartas_casa}")
    print(comparar_puntuajes(suma_cartas_usuario, suma_cartas_casa))

while input("¿Quieres jugar de nuevo? Si o No: ") == "Si":
    jugar_blackjack()