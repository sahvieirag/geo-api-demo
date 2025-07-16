from flask import Flask, request, jsonify
from services import find_nearby_locations

app = Flask(__name__)

@app.route("/")
def index():
    return "Geo-Location API Demo is running!"

@app.route("/api/nearby")
def get_nearby_locations():
    """
    Endpoint para encontrar locais próximos.
    Query Params:
      - origin: o nome do local de origem (ex: 'sao_paulo_sp')
      - radius: o raio em km (ex: 10)
    """
    origin = request.args.get('origin')
    radius_str = request.args.get('radius')

    if not origin or not radius_str:
        return jsonify({"error": "Parâmetros 'origin' e 'radius' são obrigatórios."}), 400

    try:
        radius = float(radius_str)
    except ValueError:
        return jsonify({"error": "Parâmetro 'radius' deve ser um número."}), 400

    locations, error = find_nearby_locations(origin, radius)

    if error:
        return jsonify({"error": error}), 404

    return jsonify(locations)

if __name__ == "__main__":
    app.run(debug=True)