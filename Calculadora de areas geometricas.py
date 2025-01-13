# Tarea semana 5 Beltrán
# Programa que calcula el área de diferentes figuras geométricas.
# El usuario puede elegir entre círculo, cuadrado o rectángulo y el programa realizará el cálculo basado en las entradas proporcionadas.

import math  # Importamos el módulo math para utilizar la constante pi y la función sqrt


# Función para calcular el área de un círculo
def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    Formula: área = pi * radio^2
    """
    area = math.pi * radio ** 2  # Fórmula del área del círculo
    return area


# Función para calcular el área de un cuadrado
def calcular_area_cuadrado(lado):
    """
    Calcula el área de un cuadrado dado el tamaño de uno de sus lados.
    Formula: área = lado^2
    """
    area = lado ** 2  # Fórmula del área del cuadrado
    return area


# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo dado su base y altura.
    Formula: área = base * altura
    """
    area = base * altura  # Fórmula del área del rectángulo
    return area


# Función principal para interactuar con el usuario
def main():
    print("Bienvenido a la calculadora de áreas geométricas.")

    # Solicitar al usuario elegir la figura geométrica
    print("Elija una figura para calcular el área:")
    print("1. Círculo")
    print("2. Cuadrado")
    print("3. Rectángulo")

    # Obtener la opción del usuario
    opcion = int(input("Ingrese el número de la figura: "))

    # Validación de la opción
    if opcion == 1:
        # Cálculo del área de un círculo
        radio = float(input("Ingrese el radio del círculo: "))  # Entrada del radio
        area_circulo = calcular_area_circulo(radio)
        print(f"El área del círculo es: {area_circulo:.2f} unidades cuadradas")

    elif opcion == 2:
        # Cálculo del área de un cuadrado
        lado = float(input("Ingrese el lado del cuadrado: "))  # Entrada del lado
        area_cuadrado = calcular_area_cuadrado(lado)
        print(f"El área del cuadrado es: {area_cuadrado:.2f} unidades cuadradas")

    elif opcion == 3:
        # Cálculo del área de un rectángulo
        base = float(input("Ingrese la base del rectángulo: "))  # Entrada de la base
        altura = float(input("Ingrese la altura del rectángulo: "))  # Entrada de la altura
        area_rectangulo = calcular_area_rectangulo(base, altura)
        print(f"El área del rectángulo es: {area_rectangulo:.2f} unidades cuadradas")

    else:
        # Si la opción es inválida
        print("Opción no válida. Por favor, ingrese un número entre 1 y 3.")


# Llamada a la función principal
if __name__ == "__main__":
    main()
