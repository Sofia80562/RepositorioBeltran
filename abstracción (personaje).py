# La clase Personaje es una representación abstracta de un personaje en el juego.
# Esta clase contiene los atributos básicos de un personaje, como fuerza, inteligencia, defensa, y vida.
# También incluye métodos para realizar acciones comunes, como atacar, morir y verificar si está vivo.

class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        # Constructor para inicializar los atributos del personaje.
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        # Método para imprimir los atributos del personaje.
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        # Método para subir el nivel del personaje, aumentando sus atributos.
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    def esta_vivo(self):
        # Método que devuelve si el personaje está vivo (si su vida es mayor que 0).
        return self.vida > 0

    def morir(self):
        # Método que establece la vida del personaje a 0, indicando que ha muerto.
        self.vida = 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):
        # Método para calcular el daño que inflige el personaje al enemigo.
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        # Método para realizar un ataque al enemigo.
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

