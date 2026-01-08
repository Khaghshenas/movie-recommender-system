# app/main.py
from flask import Flask, request, jsonify
from model import load_resources, recommend_movies

# Initialize Flask app
app = Flask(__name__)

# Load all model resources
resources = load_resources()

# API endpoint for recommendations
@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        top_n = data.get('top_n', 5)

        if user_id is None or not isinstance(user_id, int):
            return jsonify({"error": "Invalid user_id. Must be an integer."}), 400

        recommendations = recommend_movies(resources, user_id, top_n)
        return jsonify({"user_id": user_id, "recommendations": recommendations})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "API is running"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
