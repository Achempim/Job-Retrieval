from apscheduler.schedulers.blocking import BlockingScheduler
from scraper import fetch_job_listings

scheduler = BlockingScheduler()

# Schedule job fetching (not storing, only refreshing)
def refresh_jobs():
    print("Refreshing job listings...")
    fetch_job_listings("Data Scientist")  # Default search example

scheduler.add_job(refresh_jobs, 'interval', hours=12)

scheduler.start()
