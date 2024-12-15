class Mago:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        # El mago es un tipo de personaje que tiene un libro como atributo adicional.
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        # Método para mostrar los atributos del mago, incluidos los del libro.
        super().atributos()
        print("·Libro:", self.libro)

    def daño(self, enemigo):
        # Método para calcular el daño del mago, que depende de su inteligencia y el poder de su libro.
        return self.inteligencia * self.libro - enemigo.defensa
