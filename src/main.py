"""
main.py

Punto de entrada principal del programa.

Desde aquí se inicia la interfaz y se
ejecuta la lógica del juego.
"""

from interfaz.interfaz_usuario import mostrar_bienvenida
from logica.logica_juego import LogicaJuego


def main():
    """
    Función principal del programa.
    """

    # Mostrar pantalla inicial
    mostrar_bienvenida()

    # Crear instancia del juego
    juego = LogicaJuego()

    # Ejecutar juego
    juego.iniciar()


# Ejecutar solamente si este archivo
# es el programa principal
if __name__ == "__main__":
    main()