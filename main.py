import random  # Importamos la librería random
import time    #Importamos la librería time
# Para implementar puntajes, crearemos una nueva variable llamada 

iniciar_trivia = True  # Iniciamos la variable en True
intentos = 0  # variable que almacenará el número de veces que el usuario intenta nuestra trivia.

#Creamos nuestras constantes para darle color a nuestro programa
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

#Agrego la bienvenida a nuestro programa
print(RED+"Bienvenidos a mi trivia sobre conocimientos de programación en Python"+RESET)
time.sleep(1) #Espera 1 segundo antes de continuar
print("Pondremos a prueba tus conocimientos.")

#Pido que ingrese su nombre
nombre=input("Ingresa su nombre: ")

#  Mientras iniciar_trivia sea True, repite:
while iniciar_trivia == True:
  intentos += 1
  # "puntaje" la que inicializamos en un valor aleatorio entre 0 y 10.
  puntaje = random.randint(0, 10)
  print("\nIntento número:", intentos)
  print("Te daremos un puntaje al azar comprendido entre 0 y 10.")
  print(f"Tienes {puntaje} puntos.")



  print(f"\n Hola {nombre} responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")

  print(BLUE+"Esperemos 5 segundos antes de la primera pregunta."+RESET)
  for numero_carga in range(5, 0, -1):
    print(BLUE+f"{numero_carga} segundos"+RESET)
    time.sleep(1)

  print("\n")
  #PREGUNTA1
  print (YELLOW+"1) ¿Quién fue el creador de Python?\n"+RESET)
  time.sleep(1)
  print (GREEN+"a) Guido Van Rossum"+RESET)
  print (GREEN+"b) Bill Gates"+RESET)
  print (GREEN+"c) Mark Zuckerberg"+RESET)
  print (GREEN+"d) Dennis Ritchie"+RESET)

# Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_1 = input("\nTu respuesta es: ")

  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente su respuesta")

  # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
  if respuesta_1 == "d":
    print(f"Incorrecto,{nombre}! Dennis Ritchie creó el lenguaje C.")
    puntaje -= 2
    print(MAGENTA+f"Se te restará dos puntos de tu puntaje actual.\nTienes {puntaje} puntos actualmente."+RESET)
  elif respuesta_1 == "b":
    print(f"Incorrecto,{nombre}! Bill Gates es el creador de Microsoft.")
    puntaje -= 2
    print(MAGENTA+f"Se te restará dos puntos de tu puntaje actual.\nTienes {puntaje} puntos actualmente."+RESET)
  elif respuesta_1 == "c":
    print(f"Incorrecto, {nombre}! Mark Zuckerberg es el creador de Facebook.")
    puntaje -= 2
    print(MAGENTA+f"Se te restará dos puntos de tu puntaje actual.\nTienes {puntaje} puntos actualmente."+RESET)
  else:
    puntaje += 5
    print(MAGENTA+f"Muy bien {nombre}! Se te sumará a tu puntaje 5 puntos.\nTu puntaje actual es de {puntaje} puntos.\n"+RESET)

  #PREGUNTA 2
  time.sleep(2)
  print(YELLOW+"2) ¿Cuales de las siguientes alternativas es un bucle en Python?\n"+RESET)
  time.sleep(1)
  print (GREEN+"a) if"+RESET)
  print (GREEN+"b) randint"+RESET)
  print (GREEN+"c) while"+RESET)
  print (GREEN+"d) print"+RESET)

  # Almacenamos la respuesta del usuario en la variable "respuesta_2"
  respuesta_2 = input("\nTu respuesta es: ")
  while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

  # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
  if respuesta_2 == "a":
    print(f"Incorrecto,{nombre}! El if es una condicional")
    puntaje -= 2
    print(MAGENTA+f"Se te restará dos puntos de tu puntaje actual.\nTienes {puntaje} puntos actualmente."+RESET)
  elif respuesta_2 == "b":
    print(f"Incorrecto,{nombre}! El comando randint se usa para generar números aleatorios dentro de un rango.")
    puntaje -= 2
    print(MAGENTA+f"Se te restará dos puntos de tu puntaje actual.\nTienes {puntaje} puntos actualmente."+RESET)
  elif respuesta_2 == "d":
    print(f"Incorrecto, {nombre}! La función print se usa para imprimir un mensaje en pantalla.")
    puntaje -= 2
    print(MAGENTA+f"Se te restará dos puntos de tu puntaje actual.\nTienes {puntaje} puntos actualmente."+RESET)
  else:
    puntaje += 5
    print(MAGENTA+f"Muy bien {nombre}! Se te sumará a tu puntaje 5 puntos.\nTu puntaje actual es de {puntaje} puntos.\n"+RESET)
    
  #PREGUNTA 3
  time.sleep(2)
  print(YELLOW+"3) ¿Cuales de las siguientes alternativas define la función if?\n"+RESET)
  time.sleep(1)
  print (GREEN+"a) Establece la variable iteradora en cada valor de una lista, arreglo o cadena proporcionada y repite el código en el cuerpo del bucle para cada valor de la variable iteradora."+RESET)
  print (GREEN+"b) Evalúa una condición y luego ejecuta un bloque de código si la condición es verdadera. El bloque de código se ejecuta repetidamente hasta que la condición llega ser o es falsa."+RESET)
  print (GREEN+"c) Esta función permite obtener el texto escrito por el usuario."+RESET)
  print (GREEN+"d) Se usa para tomar decisiones, este evaluá básicamente una operación lógica, es decir una expresión que de como resultado True o False , y ejecuta la pieza de código siguiente siempre y cuando el resultado sea verdadero."+RESET)

  # Almacenamos la respuesta del usuario en la variable "respuesta_3"
  respuesta_3 = input("\nTu respuesta es: ")
  while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

  # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
  if respuesta_3 == "a":
    print(f"Incorrecto,{nombre}! Esta es la definición de la función for.")
    puntaje -= 2
    print(MAGENTA+f"Se te restará dos puntos de tu puntaje actual.\nTienes {puntaje} puntos actualmente."+RESET)
  elif respuesta_3 == "b":
    print(f"Incorrecto,{nombre}! Esta es la definición de la función while.")
    puntaje -= 2
    print(MAGENTA+f"Se te restará dos puntos de tu puntaje actual.\nTienes {puntaje} puntos actualmente."+RESET)
  elif respuesta_3 == "c":
    print(f"Incorrecto, {nombre}! Esta es la definición de la función print.")
    puntaje -= 2
    print(MAGENTA+f"Se te restará dos puntos de tu puntaje actual.\n Tienes {puntaje} puntos actualmente."+RESET)
  else:
    puntaje += 5
    print(MAGENTA+f"Muy bien {nombre}! Se te sumará a tu puntaje 5 puntos.\nTu puntaje actual es de {puntaje} puntos.\n"+RESET)

  #PREGUNTA 4
  time.sleep(2)
  print(YELLOW+"4) ¿Cuales de las siguientes alternativas es la más acertada sobre que es una lista?\n"+RESET)
  time.sleep(1)
  print (GREEN+"a) Es una colección de datos."+RESET)
  print (GREEN+"b) Es un tipo de dato compuesto de python, ya que puede almacenar más de un valor en su interior. "+RESET)
  print (GREEN+"c) Es un tipo de bucle."+RESET)
  print (GREEN+"d) Es una constante."+RESET)
  # Almacenamos la respuesta del usuario en la variable "respuesta_4"
  respuesta_4 = input("\nTu respuesta es: ")
  while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

  # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
  if respuesta_3 == "a":
    print(f"Incorrecto,{nombre}! Es acertada la respuesta pero en otra alternativa tiene una definición más completa.")
    puntaje -= 2
    print(MAGENTA+f"Se te restará dos puntos de tu puntaje actual.\nTienes {puntaje} puntos actualmente."+RESET)
  elif respuesta_3 == "c":
    print(f"Incorrecto,{nombre}! Las listas no son bucles.")
    puntaje -= 2
    print(MAGENTA+f"Se te restará dos puntos de tu puntaje actual.\nTienes {puntaje} puntos actualmente."+RESET)
  elif respuesta_3 == "d":
    print(f"Incorrecto, {nombre}! Una lista no es una constante.")
    puntaje -= 2
    print(MAGENTA+f"Se te restará dos puntos de tu puntaje actual.\nTienes {puntaje} puntos actualmente."+RESET)
  else:
    puntaje += 5
    print(MAGENTA+f"Muy bien {nombre}! Se te sumará a tu puntaje 5 puntos.\nTu puntaje actual es de {puntaje} puntos.\n"+RESET)
    
  

  print (f"Gracias {nombre} por jugar mi trivia, alcanzaste {puntaje} puntos")

  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
  puntaje=0
  print("\n \n \n")
  if repetir_trivia != "si":  
    print(f"\nEspero {nombre} que lo hayas pasado bien, hasta pronto!")
    iniciar_trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.

 