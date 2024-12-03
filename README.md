🌍 [Leia em Português](README.pt-BR.md)

# Energy Prediction API

This API is powered by a machine learning model that predicts total renewable energy based on data from different energy sources. The main objective is to help in the analysis of energy trends and promote sustainability through predictive insights.

## Tecnologias

- `Python 3.x` - Language used.
- `Flask` - Creation of api.
- `scikit-learn` - Creation of the machine learning model.
- `pickle` - Serialization of the model.
- `pandas` - Data handling.

## API Endpoints

### `http://localhost:5000/api`

#### Method: GET

#### Description: Return base description of api.

#### Response example:

```json
{
  "status": "API is running",
  "description": "API para previsão de energia renovável",
  "version": "1.0.0",
  "creation_date": "2024-10-25",
  "technologies": ["Python 3.x", "Flask"],
  "endpoints": {
    "/api/": "Informações sobre a API (GET)",
    "/api/predict/": "Predição de energia renovável (POST)"
  }
}
```

### `http://localhost:5000/api/predict`

#### Method: POST

#### Description: Receives data from energy sources and returns the forecast of total renewable energy.-

#### Expected Parameters (via query string):

- `year (int): Ano de referência. `
- `hydroelectric_power (float): Consumo de energia hidrelétrica. `
- `geothermal_energy (float): Consumo de energia geotérmica. `
- `solar_energy (float): Consumo de energia solar. `
- `wind_energy (float): Consumo de energia eólica. `
- `biomass_energy (float): Consumo de energia de biomassa. `

#### Example of Data Submission:

```json
{
  "year": 2025,
  "hydroeletric_power": 1500.5,
  "geothermal_energy": 300.7,
  "solar_energy": 800.0,
  "wind_energy": 1200.4,
  "biomass_energy": 600.3
}
```

#### Response Example

```json
{
  "Year": 2025,
  "Predicted Total Renewable Energy": 4401.9
}
```

# Steps for installing and running.

1. Clone the repository:

```bash
git clone https://github.com/felipeclarindo/energy-predict-api.git
```

2. Enter directory:

```bash
cd energy-predict-api
```

3. Create Virtual Environment:

```bash
python -m venv .venv
```

4. Activate the Environment running `.bat` file: `.venv/Scripts/activate.bat`

5. Install the dependencies:

```bash
pip install -r requirements.txt
```

6. Rotate the jupyter cells from the file `src/transition_energy_model.ipynb`

7. Run the api:

```bash
python src/api/api.py
```

8. Api will be available at:

- `http://localhost:5000`

## Contribution

Contributions are welcome! If you have suggestions for improvements, feel free to open an issue or submit a pull request.

## Author

**Felipe Clarindo**

- [LinkedIn](https://www.linkedin.com/in/felipeclarindo)
- [Instagram](https://www.instagram.com/lipethecoder)
- [GitHub](https://github.com/felipeclarindo)

## License

This project is licensed under the [GNU Affero License](https://www.gnu.org/licenses/agpl-3.0.html).
