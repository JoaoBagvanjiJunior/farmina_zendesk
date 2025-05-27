from flask import Flask, render_template, request, jsonify
import requests
from requests.auth import HTTPBasicAuth
from base64 import b64encode

app = Flask(__name__)

# Configurações da API
API_BASE_URL = "https://gw-c.petgenius.info/wfservice/z1"
PRODUCTS_API = f"{API_BASE_URL}/nutritionalplans/products/list"
SPECIAL_CARES_API = f"{API_BASE_URL}/specialcares/list"
API_AUTH = HTTPBasicAuth('wsfarmina_zendesk', 'test')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/specialcares', methods=['POST'])
def get_special_cares():
    data = request.json
    species = data.get('species')
    
    if not species:
        return jsonify({"error": "Espécie não especificada"}), 400
    
    payload = {
        "species": species,
        "country": "MA",
        "languageId": "1",
        "type": "dietetic"
    }
    
    try:
        response = requests.post(
            SPECIAL_CARES_API,
            json=payload,
            auth=API_AUTH
        )
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/products', methods=['POST'])
def get_products():
    data = request.json
    
    # Validação básica
    if not data.get('productType') or not data.get('type'):
        return jsonify({"error": "Tipo de alimento e tipo de pet são obrigatórios"}), 400
    
    # Construir payload padrão
    payload = {
        "country": "MA",
        "languageId": "20",
        "appsAndEshop": True,
        **data
    }
    
    # Converter string 'true'/'false' para boolean
    if 'gestation' in payload:
        payload['gestation'] = payload['gestation'] == 'true'
    if 'lactation' in payload:
        payload['lactation'] = payload['lactation'] == 'true'
    
    try:
        response = requests.post(
            PRODUCTS_API,
            json=payload,
            auth=API_AUTH
        )
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)