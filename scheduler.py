from apscheduler.schedulers.blocking import BlockingScheduler
from scraper import fetch_job_listings

scheduler = BlockingScheduler()

def refresh_jobs():
    print("Refreshing job listings...")
    fetch_job_listings("Data Engineer")

scheduler.add_job(refresh_jobs, 'interval', hours=12)
scheduler.start()
