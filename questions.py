import random
# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, en el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

#Inicializo el puntaje en cero
score = 0 

#Modifico y junto las 3 listas
questions_to_ask = random.choices(list(zip(questions, answers, correct_answers_index)), k = 3)

# El usuario deberá contestar 3 preguntas
for questions, possible_answers, correct_index in questions_to_ask:
    #Muestra la pregunta y las respuestas
    print(questions)
    for i, answer in enumerate(possible_answers):
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
        if user_answer.isdigit(): 
          user_answer = int(user_answer) -1
          #Verifico si el número está dentro del rango de respuestas
          if user_answer < 0 or user_answer >= len(possible_answers):
            print("Respuesta no válida")
            break
          # Se verifica si la respuesta es correcta
          if user_answer == correct_index:
            print("¡Correcto!")
            #Sumo un punto si es correcta
            score += 1
            break
          else:
            # Si el usuario no responde correctamente después de 2 intentos,
            # se muestra la respuesta correcta
            print("Incorrecto. La respuesta correcta es:")
            print(possible_answers[correct_index])
            score -=0.5
            break
        else:
          #Si el dato ingresado no es un entero, muestra error
          print("Su respuesta no es válida")
          break
        # Se imprime un blanco al final de la pregunta
        print()
#Muestro el puntaje final de la partida
print(f"Tu puntaje final es: {score:2f}")