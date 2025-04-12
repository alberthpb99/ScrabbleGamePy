# ScrabbleGamePy

Este juego tipo Scrabble en **Python** fue desarrollado como proyecto final del curso **“Curso completo de Python, de la A a la Z”** de la plataforma educativa [Frogames](https://www.frogames.es/).

Este proyecto involucra programación orientada a objetos, uso de módulos personalizados, manipulación de archivos externos y visualización de datos con Matplotlib para crear una experiencia interactiva del juego.

---

## Objetivo del proyecto

Desarrollar un juego de tablero interactivo que permita:

- Simular una partida tipo Scrabble
- Visualizar el tablero con colores, letras y puntajes
- Actualizar el tablero dinámicamente a medida que se introducen nuevas palabras
- Usar archivos externos para configurar fichas, palabras y multiplicadores
- Poner en práctica el manejo de **clases, objetos y estructuras modulares** en Python
- Aplicar lógica de juego y estructuras de control para organizar el flujo de la partida

---

## Tecnologías utilizadas

- `Python 3`
- `Matplotlib` para la visualización del tablero
- `Pandas` y `NumPy` para el manejo interno de datos
- `Google Colab` como entorno de desarrollo

---

##  Descripción de archivos

**Archivo principal:**

- `ApylabradosModule.py`: contiene todas las clases que conforman la lógica del juego (fichas, palabras, tablero, diccionario, etc.).  

**Notebook:**

- `main.ipynb`: Establece la conexión con los diferentes archivos y ejecuta el juego 

**Carpeta `data`:**

- `bag_of_pawns.csv`: define cuántas fichas de cada letra hay en la bolsa del juego.
- `dictionary.txt`: lista de palabras válidas que se pueden formar y validar durante la partida.
- `multiplier_board.csv`: define los multiplicadores de casillas en el tablero (x2 letra, x3 palabra, etc.).
- `xycolor_board.csv`: indica qué color debe tener cada casilla del tablero en función del tipo de multiplicador.
- `options_message.txt`: muestra las opciones iniciales del menú antes de colocar la primera palabra.
- `options_plus_message.txt`: muestra las opciones del menú una vez la partida ha comenzado.
- `instructions_message.txt`: contiene las instrucciones del juego que se muestran al inicio.
- `welcome_message.txt`: contiene el mensaje de bienvenida al jugador al iniciar el juego.
