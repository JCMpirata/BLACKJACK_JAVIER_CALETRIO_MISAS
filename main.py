# BLACJACK
# Creo la baraja de poker con las puntuaciones de cada carta

cartas = {
    chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0a0): 10,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ac): 10

}

# Obtener el valor de cada carta
print("Cartas: ".format(" ".join(cartas.keys())))
print("Puntos: ".format(list(cartas.values())))

# Lista de cartas
lista_de_cartas = list(cartas)

# Cartas del jugador y su puntuacion
carta_jugador = choice(lista_de_cartas)
puntuacion_jugador = cartas[carta_jugador]
print(carta_jugador, end = " ")
carta = choice(lista_de_cartas)
puntuacion_jugador += cartas[carta]
print(carta, end = " ")
print("Has conseguido {} puntos".format(puntuacion_jugador))

# Cartas de la banca
carta_banca = sample(lista_de_cartas, 2)
puntuacion_banca = sum(cartas[carta] for carta in carta_banca)
print("La banca ha sacado {} {} por lo que tiene una puntuacion de {} puntos".format(carta_banca[0], carta_banca[1], puntuacion_banca[2]))






