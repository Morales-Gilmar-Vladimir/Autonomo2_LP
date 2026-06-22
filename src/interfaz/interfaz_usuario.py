"""
interfaz_usuario.py

Este módulo contiene todas las funciones
relacionadas con la interacción entre
el usuario y el programa.
"""


def mostrar_bienvenida():

    print("\n================================")
    print("      ADIVINA EL NUMERO")
    print("================================")
    print("Piensa un numero entre 1 y 100.")
    print("Intentare adivinarlo.\n")

def confirmar_inicio():
    """
    Pregunta al usuario si ya tiene pensado
    su número para comenzar el juego.
    """

    print("\n¿Ya pensaste tu número?")
    print("s -> Sí, comenzar juego")
    print("n -> Todavía no")

    return input("Respuesta: ").lower()

def mostrar_suposicion(numero):
    """
    Muestra la suposición actual
    realizada por el computador.
    """

    print(f"\nMi suposicion es: {numero}")


def pedir_respuesta():
    """
    Solicita al usuario una respuesta
    para indicar si la suposición es correcta.

    Retorna:
        str: opcion ingresada por el usuario.
    """

    print("\nSelecciona una opcion:")
    print("a -> Mi numero es mas alto")
    print("b -> Mi numero es mas bajo")
    print("c -> Correcto")

    return input("Respuesta: ").lower()


def mostrar_resultado(intentos):
    """
    Muestra el resultado final del juego.
    """

    print("\n================================")
    print("¡Numero encontrado!")
    print(f"Intentos utilizados: {intentos}")
    print("================================")


def mostrar_error():
    """
    Muestra un mensaje cuando el usuario
    ingresa una opcion invalida.
    """

    print("\nError: opcion no valida.")