"""
gestor_intentos.py

Este módulo administra la cantidad de intentos
realizados por el computador para adivinar
el número del usuario.
"""


class GestorIntentos:

    def __init__(self):
        # Inicialmente no existen intentos
        self.intentos = 0

    def sumar_intento(self):
        """
        Incrementa en uno el contador de intentos.
        """
        self.intentos += 1

    def obtener_intentos(self):
        """
        Devuelve la cantidad total de intentos.
        """
        return self.intentos