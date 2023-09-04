from flask import Flask, render_template, request

import openai

app = Flask(__name__)

# Configura tu API Key de OpenAI
openai.api_key = "tu-apikey-de-openai"

@app.route("/", methods=["GET", "POST"])
def home():
    respuesta_generada = None

    if request.method == "POST":
        texto_entrada = request.form["texto_entrada"]
        
        # Llamada a la API para generar texto
        respuesta = openai.Completion.create(
            engine="text-davinci-002",  # El modelo GPT-3.5
            prompt=texto_entrada,
            max_tokens=50  # Cantidad máxima de tokens en la respuesta
        )
        
        # Extrae la respuesta generada por el modelo
        respuesta_generada = respuesta.choices[0].text

    return render_template("index.html", respuesta_generada=respuesta_generada)

if __name__ == "__main__":
    app.run(debug=True)
