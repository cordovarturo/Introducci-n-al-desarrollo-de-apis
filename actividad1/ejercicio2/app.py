from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convertir-temperatura', methods=['POST'])
def convertir_temperatura():
    datos = request.get_json()

    # Validar que se enviaron los datos necesarios
    if not datos or 'valor' not in datos or 'escala' not in datos:
        return jsonify({"error": "Se requiere 'valor' (número) y 'escala' (Celsius o Fahrenheit)"}), 400

    valor = datos['valor']
    escala = datos['escala'].strip().capitalize()

    # Aplicar la fórmula de conversión según la escala de origen
    if escala == 'Celsius':
        resultado = (valor * 9/5) + 32
        escala_destino = 'Fahrenheit'
    elif escala == 'Fahrenheit':
        resultado = (valor - 32) * 5/9
        escala_destino = 'Celsius'
    else:
        return jsonify({"error": "Escala inválida. Use 'Celsius' o 'Fahrenheit'"}), 400

    respuesta = {
        "valor_original": valor,
        "escala_origen": escala,
        "resultado": round(resultado, 2),
        "escala_destino": escala_destino
    }

    return jsonify(respuesta), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)
