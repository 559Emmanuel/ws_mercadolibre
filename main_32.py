from flask import Flask, jsonify

app = Flask(__name__)

# Primer endpoint
@app.route('/primer_endpoint', methods=['GET'])
def primer_endpoint():
    return jsonify(message="Soy el primer endpoint")

# Segundo endpoint
@app.route('/segundo_endpoint', methods=['GET'])
def segundo_endpoint():
    return jsonify(message="Soy el segundo")

# Tercer endpoint
@app.route('/tercer_endpoint', methods=['GET'])
def tercer_endpoint():
    return jsonify(message="Soy el tercero")

if __name__ == '__main__':
    app.run(debug=True)
