from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/mensaje", methods=["GET"])
def obtener_mensaje():
    return jsonify({
        "mensaje": "✅ Conexión exitosa desde el Backend Flask! Todo funciona con Docker y DevOps."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)