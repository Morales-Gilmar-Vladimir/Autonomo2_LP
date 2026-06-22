"""
gestor_rangos.py

Este módulo administra los límites mínimo y máximo
que utiliza el computador para realizar sus
suposiciones.

El algoritmo utiliza búsqueda binaria para
encontrar rápidamente el número correcto.
"""


class GestorRangos:

    def __init__(self):

        # Rango inicial definido en el juego
        self.minimo = 1
        self.maximo = 100

    def obtener_suposicion(self):
        """
        Calcula el valor medio del rango actual.

        Retorna:
            int: número sugerido por el computador.
        """
        return (self.minimo + self.maximo) // 2

    def ajustar_minimo(self, numero):
        """
        Actualiza el límite inferior cuando
        el usuario indica que el número es mayor.
        """
        self.minimo = numero + 1

    def ajustar_maximo(self, numero):
        """
        Actualiza el límite superior cuando
        el usuario indica que el número es menor.
        """
        self.maximo = numero - 1

    def obtener_rango(self):
        """
        Devuelve el rango actual del juego.
        """
        return self.minimo, self.maximo