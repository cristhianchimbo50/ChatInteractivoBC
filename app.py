from flask import Flask, render_template, request, jsonify
from conocimiento import base_conocimiento, obtener_pregunta, obtener_respuesta_final

app = Flask(__name__)

@app.route("/")
def home():
    pregunta_inicial, _ = obtener_pregunta("inicio")
    return render_template("chat.html", pregunta_inicial=pregunta_inicial)

@app.route("/respuesta", methods=["POST"])
def respuesta():
    datos = request.get_json()
    estado_actual = datos.get("estado", "inicio")
    respuesta_usuario = datos.get("respuesta", "")

    opciones = base_conocimiento.get(estado_actual, {}).get("respuestas", {})
    nuevo_estado = opciones.get(respuesta_usuario)

    if nuevo_estado is None:
        return jsonify({"mensaje": "No entiendo tu respuesta. Intenta de nuevo.", "estado": estado_actual})

    mensaje, _ = obtener_pregunta(nuevo_estado)
    if mensaje is None:
        mensaje = obtener_respuesta_final(nuevo_estado)

    return jsonify({"mensaje": mensaje, "estado": nuevo_estado})

if __name__ == "__main__":
    app.run(debug=True)
