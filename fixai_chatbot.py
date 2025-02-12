from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Función para diagnosticar problemas comunes de PC
def diagnostico_pc(sintoma):
    respuestas = {
        "pantalla azul": "Posibles causas: Fallo de memoria RAM, errores de controladores o problemas en el sistema operativo. Intenta reiniciar en modo seguro y revisar los drivers.",
        "lento": "Si tu PC está lenta, revisa si tienes programas en segundo plano consumiendo recursos o un disco duro saturado.",
        "se apaga solo": "Puede ser un problema de temperatura. Limpia los ventiladores y revisa la pasta térmica del procesador.",
        "no enciende": "Revisa la fuente de poder y prueba con otro cable de corriente. También verifica si el botón de encendido está funcionando.",
        "no reconoce usb": "Verifica que los controladores USB estén actualizados en el Administrador de dispositivos.",
        "computadora lenta": "Revisa el administrador de tareas y cierra programas innecesarios para mejorar el rendimiento.",
        "se demora en encender": "Podría ser un problema de disco duro o demasiadas aplicaciones en inicio. Prueba deshabilitar programas de inicio innecesarios."
    }

    sintoma = sintoma.lower()
    for clave in respuestas.keys():
        if clave in sintoma:
            return respuestas[clave]

    return "No tengo información sobre ese problema, pero puedo ayudarte a investigarlo."

# Ruta raíz para verificar si la API está activa
@app.route("/", methods=["GET"])
def home():
    return "FixAI está funcionando correctamente"

# Ruta para el diagnóstico
@app.route("/diagnostico", methods=["POST"])
def diagnostico():
    data = request.get_json()
    sintoma = data.get("sintoma", "").lower()
    respuesta = diagnostico_pc(sintoma)
    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
