"""
estado_juego.py

Este módulo almacena el estado general del juego.
Permite saber si la partida sigue activa y si el
computador ya encontró el número correcto.
"""


class EstadoJuego:

    def __init__(self):
        # Indica si el juego sigue ejecutándose
        self.juego_activo = True

        # Indica si el número fue encontrado
        self.numero_encontrado = False