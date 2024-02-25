from flask import Flask, request, jsonify
from Scraper import *


app = Flask(__name__)

@app.route('/scraper', methods=['POST'])
def s_scraper():
    data = request.json
    scraper = WebScraper(data["link"])
    scraper._get_page_content()
    product_json = scraper.to_json()
    return jsonify({'mensage': 'Datos recibidos','result':product_json})


# Endpoint que devuelve el estado del servidor
@app.route('/status', methods=['GET'])
def server_status():
    return jsonify({'status': 'Activo'})

if __name__ == '__main__':
    app.run(port=6000,debug=True)  # Inicia el servidor en modo de depuración
