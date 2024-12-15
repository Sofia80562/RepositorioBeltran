class Guerrero:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        # El guerrero es un tipo de personaje que tiene una espada como atributo adicional.
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        # Método para cambiar el arma del guerrero entre dos opciones.
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10"))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Número de arma incorrecta")

    def atributos(self):
        # Método para mostrar los atributos del guerrero, incluidos los de la espada.
        super().atributos()
        print("·Espada:", self.espada)

    def daño(self, enemigo):
        # Método para calcular el daño de un guerrero, que depende de su fuerza y el daño del arma.
        return self.fuerza * self.espada - enemigo.defensa
