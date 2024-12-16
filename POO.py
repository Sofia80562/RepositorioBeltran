# Programación Orientada a Objetos (POO) para calcular el promedio semanal del clima

class ClimaSemanal:
    def __init__(self):
        # Atributo para almacenar las temperaturas diarias
        self.temperaturas = []

    # Método para ingresar las temperaturas
    def ingresar_temperaturas(self):
        print("Ingrese las temperaturas diarias de la semana:")
        for dia in range(7):
            temp = float(input(f"Día {dia + 1}: "))
            self.temperaturas.append(temp)

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        if len(self.temperaturas) == 0:
            return 0  # Evitar errores si no hay datos
        return sum(self.temperaturas) / len(self.temperaturas)

    # Método para mostrar el resultado
    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        print("\nEl promedio semanal de temperaturas es:", round(promedio, 2), "°C")


# Función principal del programa
def main():
    # Crear una instancia de la clase ClimaSemanal
    clima = ClimaSemanal()

    # Llamar a los métodos de la clase
    clima.ingresar_temperaturas()
    clima.mostrar_promedio()


# Ejecutar programa
if __name__ == "__main__":
    main()
