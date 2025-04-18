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

            # If there's a syntax error, return with 200 so frontend can handle it
            return jsonify(results), 200
        except Exception as e:
            app.logger.error(f"Error analyzing code: {e}")
            return jsonify({'error': str(e)}), 500

    return app

# Optional: only used for dev testing
if __name__ == '__main__':
    app = create_app()
    app.run(port=5050, debug=True)
