# Programación Tradicional para calcular el promedio semanal del clima

# Función para obtener temperaturas diarias
# Solicita al usuario ingresar las temperaturas de cada día y las almacena en una lista.
def ingresar_temperaturas():
    temperaturas = []
    print("Ingrese las temperaturas diarias de la semana:")
    for dia in range(7):
        temp = float(input(f"Día {dia + 1}: "))
        temperaturas.append(temp)
    return temperaturas


# Función para calcular el promedio semanal
# Recibe la lista de temperaturas y calcula el promedio dividiendo la suma total entre el número de días.
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)


# Función principal del programa
# Coordina la entrada de datos, cálculo del promedio y presentación del resultado al usuario
def main():
    # Obtener temperaturas
    temperaturas = ingresar_temperaturas()

    # Calcular promedio
    promedio = calcular_promedio(temperaturas)

    # Mostrar resultado
    print("\nEl promedio semanal de temperaturas es:", round(promedio, 2), "°C")


# Este bloque asegura que el programa solo se ejecutará cuando es llamado directamente
if __name__ == "__main__":
    main()
