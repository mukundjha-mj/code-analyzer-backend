from flask import Flask, request, jsonify
from flask_cors import CORS
from analyzer import analyze_code

def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route('/analyze', methods=['POST'])
    def analyze():
        try:
            code = request.json.get('code', '')
            results = analyze_code(code)
            return jsonify(results), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return app
