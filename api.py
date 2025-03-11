import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from scraper import fetch_job_listings

app = Flask(__name__)
CORS(app)

# Read the default search query from environment variables
DEFAULT_JOB_QUERY = os.getenv("DEFAULT_JOB_QUERY", "Data Engineer")

@app.route('/api/jobs/search', methods=['GET'])
def search_jobs():
    # If no query is provided, use the default one from environment variables
    query = request.args.get('q', DEFAULT_JOB_QUERY)
    jobs = fetch_job_listings(query)
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(debug=True)
