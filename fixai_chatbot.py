from flask import Flask, request, jsonify

app = Flask(__name__)

# Diccionario de respuestas mejorado
respuestas = {
    "pantalla azul": "Posibles causas: Fallo de memoria RAM, errores de controladores o problemas en el sistema operativo. Intenta reiniciar en modo seguro y revisar los drivers.",
    "lento": "Si tu PC está lenta, revisa el administrador de tareas y cierra programas innecesarios para mejorar el rendimiento.",
    "se apaga": "Puede ser un problema de temperatura. Limpia los ventiladores y revisa la pasta térmica del procesador.",
    "no enciende": "Revisa la fuente de poder y prueba con otro cable de corriente.",
    "usb": "Verifica que los controladores USB estén actualizados en el Administrador de dispositivos.",
    "computadora lenta": "Si tu computadora está lenta, revisa el administrador de tareas, desactiva programas innecesarios y verifica el estado del disco duro.",
    "arranque lento": "Podría ser un problema de disco duro o demasiadas aplicaciones en inicio. Prueba deshabilitar programas de inicio innecesarios."
}

# Función de diagnóstico optimizada con búsqueda flexible
def diagnostico_pc(sintoma):
    sintoma = sintoma.lower().strip()  # Convertir a minúsculas y eliminar espacios

    print(f"Procesando síntoma: {sintoma}")  # Para depuración

    # Buscar coincidencias con palabras clave en el diccionario
    for palabra, respuesta in respuestas.items():
        if palabra in sintoma:  # Si una palabra clave está en la frase del usuario
            print(f"¡Síntoma detectado!: {palabra}")  # Para depuración
            return respuesta

    return "No tengo información sobre ese problema, pero puedo ayudarte a investigarlo."

# Ruta de la API
@app.route('/diagnostico', methods=['POST'])
def diagnostico():
    data = request.get_json()
    
    # Validar si el JSON recibido tiene la clave correcta
    if not data or "sintoma" not in data:
        return jsonify({"error": "Formato incorrecto. Debes enviar un JSON con la clave 'sintoma'"}), 400
    
    sintoma = data.get("sintoma", "").strip()  # Asegurar que no haya espacios en blanco
    respuesta = diagnostico_pc(sintoma)
    
    return jsonify({"respuesta": respuesta})

# Ruta para verificar si la API está en línea
@app.route("/", methods=["GET"])
def home():
    return "FixAI está funcionando correctamente"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

