from flask import Flask, jsonify, request
from utils.utils import load_model

app = Flask(__name__)


@app.route("/api", methods=['GET'])
def index():
    return "API is working!"

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    model_regression = load_model()
    prediction = model_regression.predict([data['feature_values']])
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
