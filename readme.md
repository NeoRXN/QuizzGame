## **Descripcion de GameQuiz:**

GameQuizz es una aplicacion creada a partir del reto Tecnico de SOFKA como requisito de ingreso
a las Training Leagues. El juego se desarrollo en el lenguaje de programación python tomando como
punto de partida el documento Backlog y teniendo en cuenta sus respectivas historias de usuario. 
  
La aplicacion se compone de 3 archivos:  
  
- Questions.json  
- QuizzGame.py  
- scores.txt

El primer archivo Questions.json contiene las 25 preguntas requeridas por el juego, definidas en 5
categorias diferentes que son los niveles de dificultad de un grupo de 5 preguntas.  
  
El segundo archivo QuizzGame.py contiene la aplicación y es en la cual se define la lógica para utilizar 
las preguntas del archivo anteriomente nombrado.  

### NOTA: Es importante aclarar que tanto el archivo Questions.json como el archivo QuizzGame.py deben estar ubicados en la misma carpeta o ruta para que la aplicacion pueda ejecutar de forma correcta.  
  
El ultimo archivo es generado dinamicamente por la aplicación y en el se encuentra el nombre,
el puntaje, y la fecha en que cada jugador haya completado el juego satisfactoriamente o que haya
decidido salir del juego antes de contestar la siguiente pregunta.  
  
La aplicación esta desarrollada como una aplicación de consola - cli la cual puede ser ejecutada en
cualquier sistema operativo. 

### Las preguntas fueron obtenidas de la pagina web (https://www.ef.com/wwen/blog/language/questions-virtual-pub-quiz/) y su contenido pertenece exclusivamente a sus propietarios, el uso de estas preguntas fue solo para la creacion del archivo Questions.json  
  
Tanto la interfaz del juego asi como cada una de las preguntas y los mensajes al usuario fueron realizados en ingles,
sin un objetivo especial mas alla de que las preguntas originales estan en ingles y me parece que es una buena
practica del idioma.