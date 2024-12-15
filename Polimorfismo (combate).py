def combate(jugador_1, jugador_2):
    # La función combate simula una pelea entre dos personajes, que pueden ser de tipos diferentes (Guerrero, Mago).
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", jugador_1.nombre, ":", sep="")
        jugador_1.atacar(jugador_2)  # El ataque es polimórfico, el método es el mismo pero el comportamiento varía.
        print(">>> Acción de ", jugador_2.nombre, ":", sep="")
        jugador_2.atacar(jugador_1)  # El ataque es polimórfico, el método es el mismo pero el comportamiento varía.
        turno += 1

    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")
