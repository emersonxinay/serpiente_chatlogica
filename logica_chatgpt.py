# Base de conocimientos del chatbot (preguntas y respuestas)
base_conocimientos = {
    "¿Cómo estás?": "Estoy bien, gracias por preguntar.",
    "¿Cuál es tu nombre?": "Soy un chatbot simple.",
    "¿Qué hora es?": "Lo siento, no tengo acceso a la hora actual.",
    "Salir": "Adiós. ¡Que tengas un buen día!"
}

# Función para obtener una respuesta a una pregunta
def obtener_respuesta(pregunta):
    respuesta = base_conocimientos.get(pregunta, "No entiendo la pregunta.")
    return respuesta

# Bucle principal del chatbot
while True:
    entrada_usuario = input("Tú: ")
    
    if entrada_usuario.lower() == "salir":
        print("Chatbot: Adiós.")
        break
    
    respuesta = obtener_respuesta(entrada_usuario)
    print("Chatbot:", respuesta)
