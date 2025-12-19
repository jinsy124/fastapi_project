from celery import Celery
from src.config import Config
import time
import logging

logging.basicConfig(level=logging.INFO)

# Initialize Celery
c_app = Celery("tasks", broker=Config.REDIS_URL)

@c_app.task
def send_email_task(recipients: list[str], subject: str, body: str):
    """Mock email sending task."""
    # Simulate delay
    time.sleep(2)
    # Print to terminal
    logging.info(f"[CELERY TASK] Email sent to {recipients} with subject '{subject}' and body: {body}")
