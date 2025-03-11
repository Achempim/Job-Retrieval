import requests
from bs4 import BeautifulSoup
import json

# Load job sources
with open('data_sources.json', 'r') as file:
    data_sources = json.load(file)

# Function to fetch job listings from a given source
def fetch_job_listings(search_query):
    jobs = []
    headers = {'User-Agent': 'Mozilla/5.0'}

    for source in data_sources["Data Sources"]:
        try:
            response = requests.get(source['url'], headers=headers, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            # **Extract jobs dynamically (customize per website)**
            # For now, we simulate sample results
            for i in range(5):  # Mock 5 job results per source
                jobs.append({
                    "title": f"{search_query} Job {i+1} - {source['name']}",
                    "company": source["name"],
                    "location": "Remote",
                    "salary": "$70,000 - $120,000",
                    "link": source["url"]
                })

        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch from {source['name']}: {e}")

    return jobs