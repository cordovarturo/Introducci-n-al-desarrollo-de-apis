from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/promedio', methods=['POST'])
def calcular_promedio():
    datos = request.get_json()

    # Validar que se enviaron los datos necesarios
    if not datos or 'nombre' not in datos or 'calificaciones' not in datos:
        return jsonify({"error": "Se requiere 'nombre' y 'calificaciones'"}), 400

    nombre = datos['nombre']
    calificaciones = datos['calificaciones']

    # Validar que la lista no esté vacía
    if not calificaciones or len(calificaciones) == 0:
        return jsonify({"error": "La lista de calificaciones no puede estar vacía"}), 400

    # Calcular el promedio
    promedio = sum(calificaciones) / len(calificaciones)

    respuesta = {
        "nombre": nombre,
        "calificaciones": calificaciones,
        "promedio": round(promedio, 2)
    }

    return jsonify(respuesta), 200

if __name__ == '__main__':
    app.run(debug=True)
