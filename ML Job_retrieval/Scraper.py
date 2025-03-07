import requests
from bs4 import BeautifulSoup
import sqlite3
import json
from datetime import datetime

# Load data sources from JSON
with open('data_sources.json', 'r') as file:
    data_sources = json.load(file)

# Connect to SQLite database
conn = sqlite3.connect('jobs.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    company TEXT,
    location TEXT,
    salary TEXT,
    link TEXT,
    skills TEXT,
    timestamp TEXT
)
''')

# Function to fetch and parse job listings
def fetch_job_listings(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

# Function to save jobs to SQLite
def save_to_database(jobs):
    cursor.executemany('''
    INSERT INTO jobs (title, company, location, salary, link, skills, timestamp)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', jobs)
    conn.commit()

# Fetch jobs from each source
all_jobs = []
for source in data_sources["Data Sources"]:
    soup = fetch_job_listings(source['url'])
    jobs = []  # Extract job details based on site-specific HTML (to be expanded)
    save_to_database(jobs)

conn.close()
