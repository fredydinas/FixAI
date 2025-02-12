from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Diccionario de respuestas mejorado
respuestas = {
    "pantalla azul": "Posibles causas: Fallo de memoria RAM, errores de controladores o problemas en el sistema operativo. Intenta reiniciar en modo seguro y revisar los drivers.",
    "lento": "Si tu PC está lenta, revisa el administrador de tareas y cierra programas innecesarios para mejorar el rendimiento.",
    "se apaga solo": "Puede ser un problema de temperatura. Limpia los ventiladores y revisa la pasta térmica del procesador.",
    "no enciende": "Revisa la fuente de poder y prueba con otro cable de corriente. También verifica si el botón de encendido está funcionando.",
    "no reconoce usb": "Verifica que los controladores USB estén actualizados en el Administrador de dispositivos.",
    "computadora lenta": "Si tu computadora está lenta, revisa el administrador de tareas, desactiva programas innecesarios y verifica el estado del disco duro.",
    "se demora en encender": "Podría ser un problema de disco duro o demasiadas aplicaciones en inicio. Prueba deshabilitar programas de inicio innecesarios."
}

# Función de diagnóstico mejorada
def diagnostico_pc(sintoma):
    sintoma = sintoma.lower()

    # Verificar palabras clave dentro del síntoma
    for clave in respuestas.keys():
        if clave in sintoma:
            return respuestas[clave]

    # Más variaciones de frases comunes
    if any(kw in sintoma for kw in ["lenta", "computadora lenta", "pc lenta", "va muy despacio"]):
        return respuestas["computadora lenta"]
    
    if any(kw in sintoma for kw in ["no enciende", "no prende", "no inicia"]):
        return respuestas["no enciende"]

    return "No tengo información sobre ese problema, pero puedo ayudarte a investigarlo."

# Ruta de la API
@app.route('/diagnostico', methods=['POST'])
def diagnostico():
    data = request.get_json()
    sintoma = data.get("sintoma", "").strip()
    respuesta = diagnostico_pc(sintoma)
    return jsonify({"respuesta": respuesta})

# Ruta para verificar si la API está en línea
@app.route("/", methods=["GET"])
def home():
    return "FixAI está funcionando correctamente"

if __name__ == "__main__":
    app.run(debug=True)

