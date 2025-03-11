import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from scraper import fetch_job_listings

app = Flask(__name__)
CORS(app)

@app.route('/api/jobs/search', methods=['GET'])
def search_jobs():
    query = request.args.get('q', 'Data Engineer')  # Default search
    jobs = fetch_job_listings(query)
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(debug=True)

