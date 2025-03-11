import requests
from bs4 import BeautifulSoup
import sqlite3
import json
from datetime import datetime

# Load job sources
with open('data_sources.json', 'r') as file:
    data_sources = json.load(file)

# Database connection
DB_FILE = "jobs.db"

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

# Create jobs table
def setup_database():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            company TEXT,
            location TEXT,
            salary TEXT,
            link TEXT UNIQUE,
            skills TEXT,
            timestamp TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Function to fetch job listings
def fetch_job_listings(query="Data Engineer"):
    headers = {'User-Agent': 'Mozilla/5.0'}
    jobs = []

    for source in data_sources["Data Sources"]:
        try:
            response = requests.get(source['url'], headers=headers, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            # Placeholder: Extract job postings (modify for real scraping)
            for i in range(3):
                jobs.append({
                    "title": f"{query} Job {i+1} - {source['name']}",
                    "company": source["name"],
                    "location": "Remote",
                    "salary": "$70,000 - $120,000",
                    "link": source["url"],
                    "skills": "Python, SQL, Machine Learning"
                })

        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch from {source['name']}: {e}")

    return jobs

setup_database()
