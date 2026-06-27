# Adivina el Número

## Nombre del estudiante
Gilmar Vladimir Morales Rivadeneira

## Objetivo del sistema
Desarrollar un juego interactivo en Python donde el computador intenta adivinar un número pensado por el usuario, aplicando lógica de programación, estructuras condicionales, estructuras repetitivas y el algoritmo de búsqueda binaria.

## Descripción del proyecto
El proyecto consiste en un sistema donde el usuario piensa un número dentro de un rango definido y el computador realiza intentos para adivinarlo. Después de cada intento, el usuario indica si el número propuesto es mayor, menor o correcto. Con esta información, el programa ajusta el rango de búsqueda hasta encontrar la respuesta correcta.

## Funcionalidades
- Permite definir un rango de búsqueda.
- El computador realiza intentos automáticos.
- El usuario proporciona pistas sobre cada intento.
- Aplica búsqueda binaria para optimizar el proceso.
- Controla el número de intentos realizados.
- Organiza el código de forma modular.
- Gestiona el estado del juego durante la ejecución.

## Estructura del proyecto
- `estado/`: gestión del estado del juego.
- `intentos/`: control y registro de intentos.
- `interfaz/`: interacción con el usuario.
- `logica/`: lógica principal del juego.
- `rangos/`: manejo de límites y actualización del rango.
- `src/main.py`: archivo principal de ejecución.

## Tecnologías utilizadas
- Python
- GitHub
- Git

## Ejecución
Para ejecutar el proyecto, usar el siguiente comando:

```bash
python src/main.py