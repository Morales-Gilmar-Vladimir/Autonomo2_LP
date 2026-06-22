"""
logica_juego.py

Este módulo contiene la lógica principal
del juego.

Se encarga de coordinar:
- El estado del juego.
- Los rangos.
- Los intentos.
- La interacción con el usuario.
"""

from rangos.gestor_rangos import GestorRangos
from intentos.gestor_intentos import GestorIntentos
from estado.estado_juego import EstadoJuego

from interfaz.interfaz_usuario import (
    mostrar_suposicion,
    pedir_respuesta,
    mostrar_resultado,
    mostrar_error,
    confirmar_inicio
)


class LogicaJuego:

    def __init__(self):

        # Crear objetos necesarios
        self.rangos = GestorRangos()
        self.intentos = GestorIntentos()
        self.estado = EstadoJuego()

    def iniciar(self):
        """
        Ejecuta el ciclo principal del juego.
        """

        # Esperar hasta que el usuario piense el número
        listo = False

        while not listo:

            respuesta_inicio = confirmar_inicio()

            if respuesta_inicio == "s":

                print("\nPerfecto, comenzaré a adivinar.")
                listo = True

            elif respuesta_inicio == "n":

                print(
                    "\nNo hay problema. "
                    "Te esperaré hasta que tengas "
                    "tu número pensado."
                )

            else:

                print("\nRespuesta no válida.")

        # Ciclo principal del juego
        while self.estado.juego_activo:

            suposicion = self.rangos.obtener_suposicion()

            self.intentos.sumar_intento()

            mostrar_suposicion(suposicion)

            respuesta = pedir_respuesta()

            if respuesta == "a":

                self.rangos.ajustar_minimo(suposicion)

            elif respuesta == "b":

                self.rangos.ajustar_maximo(suposicion)

            elif respuesta == "c":

                self.estado.numero_encontrado = True
                self.estado.juego_activo = False

                mostrar_resultado(
                    self.intentos.obtener_intentos()
                )

            else:

                mostrar_error()