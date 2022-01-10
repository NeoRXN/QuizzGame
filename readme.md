## **Descripcion de GameQuiz:**

GameQuizz es una aplicacion creada a partir del reto Tecnico de SOFKA como requisito de ingreso
a las training leagues. El juego se desarrollo en el lenguaje de programación python tomando como
punto de partido el documento Backlog y teniendo en cuenta sus respectivas historias de usuario. 
  
La aplicacion se compone de 3 archivos:  
  
- Questions.json  
- QuizzGame.py  
- scores.txt

El primer archivo Questions.json contiene las 25 preguntas requeridas por el juego, definidas en 5
categorias diferentes que son los niveles de dificultad de un grupo de 5 preguntas.  
  
El segundo archivo QuizzGame.py contiene la aplicacion y es en la cual se define la logica para utilizar 
las preguntas del archivo anteriomente nombrado.  

### NOTA: Es importante aclarar que tanto el archivo Questions.json como el archivo QuizzGame.py deben
ubicados en la misma carpeta o ruta para que la aplicacion pueda ejecutar de forma correcta.  
  
El ultimo archivo es generado dinamicamente por la aplicacion y en el se encuentra el nombre,
el puntaje, y la fecha de cada jugador que haya copmpletado el juego satisfactoriamente o que haya
decidido salir del juego antes de contestar la siguiente pregunta.  
  
La aplicación esta desarrolada como una aplicación de consola - cli la cual puede ser ejecutada en
cualquier sistema operativo. 

### Las preguntas fueron obtenidas de la pagina web (https://www.ef.com/wwen/blog/language/questions-virtual-pub-quiz/)
y su contenido pertenece exclusivamente a sus propietarios, el uso de estas preguntas fue solo para
la creacion del archivo Questions.json