# Juego-con-Pygame
"Esquivar Enemigos" es un juego simple desarrollado en Python utilizando la biblioteca Pygame. El objetivo del juego es mover un círculo (el jugador) con el mouse y evitar colisionar con cuadrados rojos (enemigos) mientras recoges triángulos verdes dando click en ellos para aumentar tu puntuación.

## Requisitos
Asegúrate de tener instalada la biblioteca Pygame antes de ejecutar el juego. Puedes instalarla utilizando pip:

pip install pygame

## Controles
Haz clic con el botón izquierdo del ratón para interactuar con el juego.
Funcionalidad del programa
El código del juego consta de las siguientes partes:

## Configuración de la Pantalla
Se establece el tamaño de la ventana del juego y se configuran los colores y fuentes utilizados.

## Clases
* Jugador: Representa al círculo controlado por el jugador. Puedes moverlo con el ratón y tu objetivo es evitar a los enemigos y recolectar triángulos verdes para ganar puntos.
* Enemigo: Representa a los cuadrados rojos que se mueven aleatoriamente por la pantalla.
* Triangulo: Representa a los triángulos verdes que aparecen en la pantalla.
  
## Funciones para mostrar texto
Se proporcionan funciones (mostrar_texto) para simplificar la renderización de texto en la pantalla.

## Menú de Inicio
El juego comienza mostrando un menú de inicio que explica las instrucciones y muestra la última puntuación del jugador. Haz clic para comenzar.

## Pantalla de Pérdida
Cuando el jugador colisiona con un enemigo, se muestra una pantalla de pérdida con la puntuación final. Haz clic para continuar y volver al menú de inicio.

## Bucle Principal del Juego
El bucle principal maneja la lógica del juego y la detección de eventos. El jugador puede hacer clic para iniciar el juego, interactuar con los triángulos y evitar a los enemigos. El juego sigue ejecutándose hasta que el jugador pierde.

# ¡Diviértete esquivando enemigos y recolectando triángulos!
