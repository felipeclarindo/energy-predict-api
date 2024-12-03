from flask import Flask, jsonify, request
from modules.load_model import load_model
from pathlib import Path

app = Flask(__name__)

# Caminho para o modelo
model_path = 'models/model_energy.pkl'
model = load_model(Path(__file__).parent.parent / model_path)

@app.route("/api", methods=['GET'])
def index():
    return jsonify({
        "status": "API is running",
        "description": "API de previsões de energia renovável por um modelo de machine learning",
        "version": "1.0.0",
        "creation_date": "2024-10-25",
        "technologies": [
            "Python 3.x",
            "Flask"
        ],
        "endpoints": {
            "/api/": "Informações sobre a API (GET)",
            "/api/predict/": "Predição de energia renovável (POST)"
        }
    })

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        # Obter dados do corpo da requisição
        data = request.json
        if not data:
            return jsonify({'error': 'No input data provided'}), 400

        # Obter os parâmetros necessários
        year = data.get('year')
        hydro = data.get('hydroelectric_power')
        geo = data.get('geothermal_energy')
        solar = data.get('solar_energy')
        wind = data.get('wind_energy')
        biomass = data.get('biomass_energy')

        # Verificar se algum valor está ausente
        if None in [year, hydro, geo, solar, wind, biomass]:
            return jsonify({'error': 'Missing input values'}), 400

        # Converter os dados para números
        try:
            features = [[
                float(year),
                float(hydro),
                float(geo),
                float(solar),
                float(wind),
                float(biomass)
            ]]
        except ValueError:
            return jsonify({'error': "Insira valores validos"}), 400

        # Fazer a predição
        if not model:
            return jsonify({'error': 'Failed to load model, run transition_energy_model.ipynb'}), 500
        prediction = model.predict(features)

        # Retornar a predição como resposta JSON
        return jsonify({
            'Year': year,
            'Predicted Total Renewable Energy': prediction[0]
        })

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
