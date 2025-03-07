from apscheduler.schedulers.blocking import BlockingScheduler
from scraper import fetch_jobs
from email_notifier import send_email

scheduler = BlockingScheduler()

# Schedule job scraping twice daily
scheduler.add_job(fetch_jobs, 'interval', hours=12)

# Schedule email notifications twice daily
scheduler.add_job(lambda: send_email("Top Job Alerts", "New job listings available!"), 'interval', hours=12)

scheduler.start()
