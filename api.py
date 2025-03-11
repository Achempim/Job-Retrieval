from flask import Flask, jsonify, request
from flask_cors import CORS
from scraper import fetch_job_listings

app = Flask(__name__)
CORS(app)  # Allow frontend to access API

# 📍 API Endpoint: Fetch jobs dynamically based on search query
@app.route('/api/jobs/search', methods=['GET'])
def search_jobs():
    query = request.args.get('q', '')

    if not query:
        return jsonify({"error": "Query parameter 'q' is required"}), 400

    jobs = fetch_job_listings(query)
    return jsonify(jobs)

# Run Flask API
if __name__ == '__main__':
    app.run(debug=True)
