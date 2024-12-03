🌍 [Read in English](README.md)

# API de Previsão de Energia

Essa API é alimentada por um modelo de machine learning que prevê o total de energia renovável com base nos dados de diferentes fontes energéticas. O objetivo principal é ajudar na análise de tendências energéticas e promover a sustentabilidade por meio de insights preditivos.

## Tecnologias

- `Python 3.x` - Linguagem utilizada.
- `Flask` - Criação da api.
- `scikit-learn` - Criação do modelo de machine learning.
- `pickle` - Serialização do modelo.
- `pandas` - Manipulação de dados.

## EndPoints da API

### `http://localhost:5000/api`

#### Método: GET

#### Descrição: Retorna informações básicas sobre a API.

#### Exemplo de Resposta:

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

#### Método: POST

#### Descrição: Recebe dados das fontes de energia e retorna a previsão do total de energia renovável.-

#### Parâmetros Esperados (via query string):

- `year (int): Ano de referência. `
- `hydroelectric_power (float): Consumo de energia hidrelétrica. `
- `geothermal_energy (float): Consumo de energia geotérmica. `
- `solar_energy (float): Consumo de energia solar. `
- `wind_energy (float): Consumo de energia eólica. `
- `biomass_energy (float): Consumo de energia de biomassa. `

#### Exemplo de Envio de Dados:

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

#### Exemplo de Resposta:

```json
{
  "Year": 2025,
  "Predicted Total Renewable Energy": 4401.9
}
```

# Como usar

1. Clone o repositorio:

```bash
git clone https://github.com/felipeclarindo/energy-predict-api.git
```

2. Entre no diretorio

```bash
cd energy-predict-api
```

3. Crie o ambiente virtual:

```bash
python -m venv .venv
```

4. Ative o ambiente virtual executando o arquivo `.bat` em `.venv/Scripts/activate.bat`

5. Instale as dependencias

```bash
pip install -r requirements.txt
```

6. Rode as celulas jupyter do arquivo `src/transition_energy_model.ipynb`

7. Rode a API:

```bash
python src/api/api.py
```

8. A Api será disponibilizada em:

- `http://localhost:5000`

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Autor

**Felipe Clarindo**

- [LinkedIn](https://www.linkedin.com/in/felipeclarindo)
- [Instagram](https://www.instagram.com/lipethecoder)
- [GitHub](https://github.com/felipeclarindo)

## Licença

Este projeto está licenciado sob a [GNU Affero License](https://www.gnu.org/licenses/agpl-3.0.html).
